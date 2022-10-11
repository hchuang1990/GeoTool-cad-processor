#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
import win32com.client

project_name = 'A020027'

acad = win32com.client.Dispatch("AutoCAD.Application")

start_time = datetime.now()
acad.ActiveDocument.Application.Documents.Open(f"D:\\事業體\\05_可宸數位科技\\00_Project\\1111008_dwg2shp\\projects\\{project_name}\\{project_name}_83年地形套疊圖.dwg")

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

acad.ActiveDocument.SaveAs(f"D:\\事業體\\05_可宸數位科技\\00_Project\\1111008_dwg2shp\\projects\\{project_name}\\{project_name}_83年地形套疊圖_fixed", 12)

end_time = datetime.now()
print(f"{end_time-start_time}")