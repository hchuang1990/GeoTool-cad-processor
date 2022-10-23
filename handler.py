# import easygui
# import converter
# import dwg2dxf
# import dwg2pdf
# import dwg2jpg
# import dwg2tiff

# from qtapp import Ui_Dialog
from os.path import join
import win32com.client
import core
import time
from datetime import datetime

def handle(config):
    print("config", config)
    for folder in config["folders"]:
        for dwg in config["dwgs"]:
            start_time = datetime.now()
            success = False
            message = ''
            path = join(config["source_path"], folder)
            file_path = join(path, dwg)
            print(f"========================================")
            print(f"{file_path} start")
            acad = win32com.client.Dispatch("AutoCAD.Application")
            doc = None
            try:
                doc = acad.ActiveDocument.Application.Documents.Open(file_path)
                layout = doc.layouts.item('Model')
                if config["explode"] is True:
                    pass
                if config["saveAs"] is True:
                    if config["format"] == 'dwg':
                        success, message = core.saveAsDwg(acad=acad, layout=layout, doc=doc, path=path, file_name=dwg,
                                                          config=config)
                        pass
                    elif config["format"] == 'dxf':
                        success, message = core.saveAsDxf(acad=acad, layout=layout, doc=doc, path=path, file_name=dwg,
                                                          config=config)
                        pass
                    elif config["format"] == 'tiff' or config["format"] == 'pdf' or config["format"] == 'jpg':
                        success, message = core.exportFile(acad=acad, layout=layout, doc=doc, path=path, file_name=dwg,
                                                           config=config)
                        pass
            except Exception as e:
                print(e)
            finally:
                try:
                    doc.Close(False)
                except:
                    pass
            end_time = datetime.now()
            print(f"{file_path} end, {success}, {message}, time_consuming={end_time-start_time}")
            time.sleep(0.5)
                # app.label_log_path.setText(f"{join(config['source_path'], folder)}, {success}, {message}")


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
