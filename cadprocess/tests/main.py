import easygui
import converter
import dwg2dxf
import dwg2pdf
import dwg2jpg
import dwg2tiff

inputFolder = easygui.diropenbox(msg='選擇欲轉檔之資料夾')
print(inputFolder)
if inputFolder is None:
    print('skip execution')
else:
    result, msg = dwg2tiff.convert(inputFolder)
    print(f"result={result}, msg={msg}")
