# import easygui
# import converter
# import dwg2dxf
# import dwg2pdf
# import dwg2jpg
# import dwg2tiff

from qtapp import Ui_Dialog
from os.path import join
import win32com.client
import pythoncom
import printer


def handle(config, app: Ui_Dialog):
    print("config", config)
    for folder in config["folders"]:
        for dwg in config["dwgs"]:
            success = False
            message = ''
            try:
                acad = win32com.client.Dispatch("AutoCAD.Application")
                doc = acad.ActiveDocument.Application.Documents.Open(f"{folder}\\{dwg}")
                layout = doc.layouts.item('Model')
                path = join(config["source_path"], folder)
                if config["explode"] is True:
                    pass
                if config["saveAs"] is True:
                    if config["format"] == 'dwg':
                        pass
                    elif config["format"] == 'dxf':
                        pass
                    elif config["format"] == 'pdf':
                        pass
                    elif config["format"] == 'tiff':
                        success, message = printer.exportFile(acad=acad, doc=doc, path=path, file_name=dwg,
                                                              config=config)
                        pass
                    elif config["format"] == 'jpg':
                        pass
            except Exception as e:
                print(e)
            finally:
                try:
                    doc.Close(False)
                except:
                    pass
                app.label_log_path.setText(f"{join(config['source_path'], folder)}, {success}, {message}")
