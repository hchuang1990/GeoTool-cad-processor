#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
import win32com.client

acad = win32com.client.Dispatch("AutoCAD.Application")

files = ['58年地形套疊圖', '77年地形套疊圖', '83年地形套疊圖']


def convert(folder):
    t = folder.split("\\")
    project_name = t[len(t) - 1]
    print(f'project_name={project_name}')
    try:
        start_time = datetime.now()
        print(f'start_time={start_time}')
        for file in files:
            acad.ActiveDocument.Application.Documents.Open(f"{folder}\\{project_name}_{file}.dwg")

            for entity in acad.ActiveDocument.ModelSpace:
                name = entity.EntityName
                if name == 'AcDbBlockReference':
                    entity.Explode()

            for entity in acad.ActiveDocument.ModelSpace:
                name = entity.EntityName
                if name == 'AcDbText':
                    if '房屋樓層註記' in entity.Layer:
                        print(
                            f'text: {entity.TextString} at {entity.InsertionPoint}, layer={entity.Layer}, Alignment = {entity.Alignment}')
                        print('update for building')
                        entity.Alignment = 0
                    if 'LDASHAP' in entity.Layer:
                        print(
                            f'text: {entity.TextString} at {entity.InsertionPoint}, layer={entity.Layer}, Alignment = {entity.Alignment}')
                        print('update for lands')
                        entity.Alignment = 0

            acad.ActiveDocument.SaveAs(f"{folder}\\{project_name}_{file}_fixed", 12)

        end_time = datetime.now()
        print(f'end_time={end_time}')
        print(f"time consuming={end_time - start_time}")
        return True, ""
    except Exception as e:
        return False, e
