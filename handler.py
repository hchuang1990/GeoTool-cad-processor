# import easygui
# import converter
# import dwg2dxf
# import dwg2pdf
# import dwg2jpg
import dwg2tiff
from qtapp import Ui_Dialog
from os.path import join


def handle(config, app: Ui_Dialog):
    print("config", config)
    try:
        for folder in config["folders"]:
            for dwg in config["dwgs"]:
                result, msg = dwg2tiff.convert(join(config["source_path"], folder), dwg, config)
                app.label_log_path.setText(f"{join(config['source_path'], folder)}, {result}, {msg}")
    except Exception as e:
        print(e)
