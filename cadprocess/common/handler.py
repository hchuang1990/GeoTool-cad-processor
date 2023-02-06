# import easygui
# import converter
# import dwg2dxf
# import dwg2pdf
# import dwg2jpg
# import dwg2tiff

# from qtapp import Ui_Dialog
import os
from os.path import join
import win32com.client
import cadprocess.common.core as core
import time
from datetime import datetime
import logging

logger = logging.getLogger()

def  handle(config):
    # print("config", config)
    acad = win32com.client.Dispatch("AutoCAD.Application")
    print(f"==================run===================")
    logger.info(f"==================run===================")
    for folder in config["folders"]:
        for dwg in config["dwgs"]:
            start_time = datetime.now()
            success = False
            message = ''
            path = join(config["source_path"], folder)
            file_name = f"{folder}_{dwg.split('_')[1]}"
            file_path = join(path, file_name)
            print(f"========================================")
            print(f"{file_path} start")
            logger.info(f"========================================")
            logger.info(f"{file_path} start")
            try:
                if not os.path.exists(file_path):
                    logger.info(f"skip open {file_path} due to file is not exist")
                    continue
                opened = False
                doc = None
                while opened is False:
                    try:
                        doc = acad.ActiveDocument.Application.Documents.Open(file_path)
                        layout = doc.layouts.item('Model')
                        opened = True
                    except Exception as e:
                        print(f"open {file_path} error, retry after 1 second")
                        logger.error(f"open {file_path} error, retry after 1 second")
                        try:
                            doc.Close(False)
                        except:
                            pass
                        time.sleep(1)
                if config["explode"] is True:
                    print(f"{file_path} run explode...")
                    logger.info(f"{file_path} run explode...")
                    success, message = core.explode(acad=acad, layout=layout, doc=doc, path=path, file_name=file_name,
                                                          config=config)
                    pass
                if config["adjust"] is True:
                    print(f"{file_path} run adjust...")
                    logger.info(f"{file_path} run adjust...")
                    success, message = core.adjust(acad=acad, layout=layout, doc=doc, path=path, file_name=file_name,
                                                    config=config)
                    pass
                if config["saveAs"] is True:
                    print(f"{file_path} run saveAs...")
                    logger.info(f"{file_path} run saveAs...")
                    if config["format"] == 'dwg':
                        success, message = core.saveAsDwg(acad=acad, layout=layout, doc=doc, path=path, file_name=file_name,
                                                          config=config)
                        pass
                    elif config["format"] == 'dxf':
                        success, message = core.saveAsDxf(acad=acad, layout=layout, doc=doc, path=path, file_name=file_name,
                                                          config=config)
                        pass
                    elif config["format"] == 'tiff' or config["format"] == 'pdf' or config["format"] == 'jpg':
                        success, message = core.exportFile(acad=acad, layout=layout, doc=doc, path=path, file_name=file_name,
                                                           config=config)
                        pass
                    elif config["format"] == 'dgn':
                        success, message = core.exportDgn(acad=acad, layout=layout, doc=doc, path=path,
                                                           file_name=file_name,
                                                           config=config)
            except Exception as e:
                print(e)
                logger.error(f"Unexpected {e}")
            finally:
                try:
                    time.sleep(0.5)
                    doc.Close(False)
                except:
                    pass
            end_time = datetime.now()
            print(f"{file_path} end, {success}, {message}, time_consuming={end_time-start_time}")
            logger.info(f"{file_path} end, {success}, {message}, time_consuming={end_time-start_time}")
                # app.label_log_path.setText(f"{join(config['source_path'], folder)}, {success}, {message}")
    print(f"==================completed===================")
    logger.info(f"==================completed===================")

# dummy_data = {'source_path': 'E:/chiao_study/projects/cad2shp', 'folders': ['A020027'],
#               'dwgs': ['A020027_58年地形套疊圖.DWG', 'A020027_77年地形套疊圖.DWG', 'A020027_77年正射影像套疊圖.DWG', 'A020027_83年地形套疊圖.DWG',
#                        'A020027_83年正射影像套疊圖.DWG', 'A020027_相關位置圖(107年地形圖).DWG'], 'explode': False, 'saveAs': True,
#               'format': 'jpg', 'printer': 'PublishToWeb JPG.pc3', 'papper': 'ISO_full_bleed_A2_(594.00_x_420.00_MM)',
#               'log_path': 'E:chiao_studyprojectscad2shptestrun...'}

# {'source_path': 'E:/chiao_study/projects/cad2shp', 'folders': ['A020027'],
#  'dwgs': ['A020027_58年地形套疊圖.DWG', 'A020027_77年地形套疊圖.DWG', 'A020027_77年正射影像套疊圖.DWG', 'A020027_83年地形套疊圖.DWG',
#           'A020027_83年正射影像套疊圖.DWG', 'A020027_相關位置圖(107年地形圖).DWG'], 'explode': False, 'saveAs': True, 'format': 'dxf',
#  'printer': '', 'papper': 'ISO_full_bleed_A2_(594.00_x_420.00_MM)',
#  'log_path': 'E:chiao_studyprojectscad2shptestrun...'}
# handle(dummy_data)
