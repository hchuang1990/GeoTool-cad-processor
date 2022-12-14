#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from os.path import join

import win32com.client
import pythoncom
import os
import logging

logger = logging.getLogger()

def APoint(x, y):
    """坐标点转化为浮点数"""
    # 需要两个点的坐标
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, (x, y))


def explode(acad, doc, layout, path, file_name, config):
    try:
        # 炸裂
        for entity in acad.ActiveDocument.ModelSpace:
            name = entity.EntityName
            if name == 'AcDbBlockReference':
                entity.Explode()
        success = True
        message = 'Completed'
    except Exception as e:
        print(e)
        logger.error(e)
        success = False
        message = str(e)

    return success, message

def adjust(acad, doc, layout, path, file_name, config):
    try:
        # 點位校正
        for entity in acad.ActiveDocument.ModelSpace:
            name = entity.EntityName
            if name == 'AcDbText':
                if '房屋樓層註記' in entity.Layer:
                    print(
                        f'update for building point: {entity.TextString} at {entity.InsertionPoint}, layer={entity.Layer}, Alignment = {entity.Alignment}')
                    entity.Alignment = config["adjust_direction"]
                if 'LDASHAP' in entity.Layer:
                    print(
                        f'update for lands point: {entity.TextString} at {entity.InsertionPoint}, layer={entity.Layer}, Alignment = {entity.Alignment}')
                    entity.Alignment = config["adjust_direction"]
        success = True
        message = 'Completed'
    except Exception as e:
        print(e)
        logger.error(e)
        success = False
        message = str(e)

    return success, message

def saveAsDwg(acad, doc, layout, path, file_name, config):
    try:
        if config["explode"] is True:
            output = get_dir_fixed(path, file_name, config)
        else:
            output = get_dir(path, file_name, config)
        print("print file in Dir = ", output[1])
        logger.info(f"print file in Dir = {output[1]}")
        del_old_dir(output[1])
        doc.SaveAs(output[1], 12)
        success = True
        message = 'Completed'
    except Exception as e:
        print(e)
        logger.error(e)
        success = False
        message = str(e)

    return success, message


def saveAsDxf(acad, doc, layout, path, file_name, config):
    try:
        if config["explode"] is True:
            output = get_dir_fixed(path, file_name, config)
        else:
            output = get_dir(path, file_name, config)
        print("print file in Dir = ", output[1])
        logger.info(f"print file in Dir = {output[1]}")
        del_old_dir(output[1])
        doc.SaveAs(output[1], 13)
        success = True
        message = 'Completed'
    except Exception as e:
        print(e)
        logger.error(e)
        success = False
        message = str(e)

    return success, message


def exportFile(acad, doc, layout, path, file_name, config):
    try:
        # doc.Application.ZoomExtents()
        doc.SetVariable("BACKGROUNDPLOT", 0)
        doc.Plot.QuietErrorMode = True

        Scale = 1
        # set windows
        lowerLeft = None
        underRight = None
        for entity in acad.ActiveDocument.ModelSpace:
            if entity.EntityName == 'AcDbPolyline' and entity.Area > 15500 and entity.Layer == "圖框":
                # print("Layer", entity.Layer)
                # print("Area", entity.Area)
                lowerLeft, underRight = entity.GetBoundingBox()

        print("lowerLeft", [lowerLeft[0], lowerLeft[1]], "underRight", [underRight[0], underRight[1]])
        # logger.info("lowerLeft", [lowerLeft[0], lowerLeft[1]], "underRight", [underRight[0], underRight[1]])

        # 打印機

        layout.ConfigName = config["printer"]
        try:
            layout.CanonicalMediaName = config["papper"]  # 图纸大小这里选择A4
        except Exception as ee:
            pass
        # layout.PaperUnits = 1  # 图纸单位，1为毫米
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
        # layout.PlotType = 3.5
        if config["explode"] is True:
            output = get_dir_fixed(path, file_name, config)
        else:
            output = get_dir(path, file_name, config)
        del_old_dir(output[1])
        print("print file in Dir = ", output[1])
        logger.info(f"print file in Dir = {output[1]}")
        doc.Plot.PlotToFile(output[1])
        success = True
        message = 'Completed'

    except Exception as e:
        print(e)
        logger.error(e)
        success = False
        message = str(e)

    return success, message

def exportDgn(acad, doc, layout, path, file_name, config):
    try:
        if config["explode"] is True:
            output = get_dir_fixed(path, file_name, config)
        else:
            output = get_dir(path, file_name, config)
        del_old_dir(output[1])
        doc.SendCommand("-DGNEXPORT"+chr(13)+"V8"+chr(13)+f"{output[1]}"+chr(13)+"Y"+chr(13)+"Y"+chr(13)+"M"+chr(13)+chr(13)+chr(13))
        success = True
        message = 'Completed'
    except Exception as e:
        success = False
        message = str(e)
    return success, message

def get_dir(path, file_name, config):
    output_path = os.path.join(path, "output", config['format'])
    output_path_file = f"{output_path}\\{file_name.split('.')[0]}.{config['format']}"
    try:
        os.mkdir(os.path.join(path, "output"))
    except:
        pass
    try:
        os.mkdir(output_path)
    except:
        pass
    return [output_path, output_path_file]


def get_dir_fixed(path, file_name, config):
    output_path = os.path.join(path)
    output_path_file = f"{output_path}\\{file_name.split('.')[0]}_fixed.{config['format']}"
    return [output_path, output_path_file]

def del_old_dir(outputpath):
    if os.path.isfile(outputpath):
        os.unlink(outputpath)
        print(f"Clean the old file.The path is {outputpath}")
        logger.info(f"Clean the old file.The path is {outputpath}")