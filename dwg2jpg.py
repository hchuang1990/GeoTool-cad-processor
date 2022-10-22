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
layout = doc.layouts.item('Model')
# 打印機
ACADPref = doc.Application.preferences.Files
originalValue = ACADPref.PrinterConfigPath \
    = r"C:\Users\hhc\AppData\Roaming\Autodesk\AutoCAD 2014\R19.1\cht\Plotters"

# doc.Application.ZoomExtents()
doc.SetVariable("BACKGROUNDPLOT", 0)
doc.Plot.QuietErrorMode = True

Scale = 1
# set windows
lowerLeft = None
underRight = None
for entity in acad.ActiveDocument.ModelSpace:
    if entity.EntityName == 'AcDbPolyline' and entity.Area > 15500 and entity.Layer == "圖框":
        print("Layer", entity.Layer)
        print("Area", entity.Area)
        lowerLeft, underRight = entity.GetBoundingBox()

print("lowerLeft", [lowerLeft[0], lowerLeft[1]])
print("underRight", [underRight[0], underRight[1]])

layout.PaperUnits = 1  # 图纸单位，1为毫米
layout.PlotRotation = 0  # 横向打印
layout.StandardScale = 0  # 图纸打印比例
layout.CenterPlot = True  # 居中打印
layout.PlotWithPlotStyles = True  # 依照样式打印
layout.PlotHidden = False  # 隐藏图纸空间对象
layout.CanonicalMediaName = 'ISO_full_bleed_A2_(594.00_x_420.00_MM)'
# layout.CanonicalMediaName = 'Sun_Hi-Res_(1280.00_x_1600.00_Pixels)'  # 图纸大小这里选择A4
layout.UseStandardScale=True #选用标准的比例
layout.ConfigName = "PublishToWeb JPG.pc3"
layout.CenterPlot = True

po1 = APoint( lowerLeft[0] * Scale - 1, lowerLeft[1] * Scale)
po2 = APoint( underRight[0] * Scale - 1 + 11880, underRight[1] * Scale + 8400) # 左下点和右上点
layout.SetWindowToPlot(po1,po2)

# p1=acad.GetPoint()
# p2=acad.GetPoint()
# layout.SetWindowToPlot(VtFloat(p1[:2]),VtFloat(p2[:2]))
# layout.PlotType=win32com.client.constants.acWindow

doc.Plot.PlotToFile("D:\\事業體\\05_可宸數位科技\\00_Project\\1111008_dwg2shp\\projects\A020027\\" + "test" + ".jpg")
#
# oplot.Delete()
# oplot = None
# obj = doc.GetVariable("DBMOD")
# print(obj)
doc.Close(False)

