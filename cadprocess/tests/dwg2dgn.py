#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import join

import win32com.client


def convert(folder, file, config):
    success = False
    message = ''
    path = join(folder, file)
    print(path)
    try:
        acad = win32com.client.Dispatch("AutoCAD.Application")
        doc = acad.ActiveDocument.Application.Documents.Open(path)
        doc.SendCommand("-DGNEXPORT"+chr(13)+"V8"+chr(13)+chr(13)+"Y"+chr(13)+"Y"+chr(13)+"M"+chr(13)+chr(13)+chr(13))
        success = True
    except Exception as e:
        success = False
        message = str(e)
    finally:
        try:
            doc.Close(False)
        except:
            pass
    print(success, message)
    return success, message