#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pythoncom
import win32com.client

printType = 'DWG To PDF.pc3'


def APoint(x, y):
    """坐标点转化为浮点数"""
    # 需要两个点的坐标
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, (x, y))


def convert(folder):
    success = False
    message = ''
    try:
        acad = win32com.client.Dispatch("AutoCAD.Application")
        # 文件
        doc = acad.ActiveDocument.Application.Documents.Open(f"{folder}\\A020027_83年地形套疊圖.dwg")
        # 圖紙
        layout = doc.layouts.item('Model')

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

        # 打印機
        layout.ConfigName = printType
        layout.CanonicalMediaName = 'ISO_full_bleed_A2_(594.00_x_420.00_MM)'
        layout.PaperUnits = 1  # 图纸单位，1为毫米
        layout.PlotRotation = 0  # 横向打印
        layout.StandardScale = 0  # 图纸打印比例
        layout.CenterPlot = True  # 居中打印
        layout.PlotWithPlotStyles = True  # 依照样式打印
        layout.PlotHidden = False  # 隐藏图纸空间对象
        layout.CenterPlot = True
        layout.UseStandardScale = True  # 选用标准的比例

        po1 = APoint(lowerLeft[0] * Scale - 1, lowerLeft[1] * Scale)
        po2 = APoint(underRight[0] * Scale - 1 + 11880, underRight[1] * Scale + 8400)  # 左下点和右上点
        layout.SetWindowToPlot(po1, po2)

        doc.Plot.PlotToFile(f"{folder}\\_test.pdf")

        success = True

    except Exception as e:
        success = False
        message = str(e)
    finally:
        try:
            doc.Close(False)
        except:
            pass
    return success, message
