#!/usr/bin/env python
# -*- coding: utf-8 -*-

import win32com.client
import pythoncom
import array
import comtypes.client
paper = 'A4'


def APoint(x, y):
    """坐标点转化为浮点数"""
    # 需要两个点的坐标
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, (x, y))

acad = win32com.client.Dispatch("AutoCAD.Application")
# 文件
doc = acad.ActiveDocument.Application.Documents.Open(f"D:\\事業體\\05_可宸數位科技\\00_Project\\1111008_dwg2shp\\projects\A020027\\A020027_83年地形套疊圖.dwg")
# 圖紙
layout = doc.ActiveLayout
# 打印機
ACADPref = doc.Application.preferences.Files
originalValue = ACADPref.PrinterConfigPath \
    = r"C:\Users\hhc\AppData\Roaming\Autodesk\AutoCAD 2014\R19.1\cht\Plotters"

doc.SetVariable("BACKGROUNDPLOT", 0)
doc.Application.ZoomExtents()
doc.Plot.QuietErrorMode = True

layout.ConfigName = "PublishToWeb JPG.pc3"
layout.CenterPlot = True

# print(doc.ModelSpace.Layout.GetCanonicalMediaNames())


# layout.CanonicalMediaName = 'ISO_full_bleed_A4_(297.00_x_210.00_MM)'  # 图纸大小这里选择A4
layout.CanonicalMediaName = 'Sun_Hi-Res_(1280.00_x_1600.00_Pixels)'  # 图纸大小这里选择A4
layout.UseStandardScale=True #选用标准的比例
layout.StandardScale= win32com.client.constants.acScaleToFit

oplot = doc.PlotConfigurations.Add("JPG", layout.ModelType)

# set windows

# for entity in acad.ActiveDocument.ModelSpace:
#     name = entity.EntityName
#     if name == 'AcDbPolyline':
#         print(entity.Layer)
#         lowerLeft, underRight = entity.GetBoundingBox()
#         print("lowerLeft", lowerLeft)
#         print("underRight", underRight)
# doc.ActiveLayout.SetWindowToPlot([[300027.3037, 2776341.1088],[300175.8037, 2776446.1088]])
# doc.ActiveLayout.SetWindowToPlot(array.array('d',frame[1]),array.array('d',frame[2]))
#
#
doc.Plot.PlotToFile("D:\\事業體\\05_可宸數位科技\\00_Project\\1111008_dwg2shp\\projects\A020027\\" + "test" + ".jpg")
#
# oplot.Delete()
# oplot = None
# obj = doc.GetVariable("DBMOD")
# print(obj)
doc.Close(False)

