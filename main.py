import easygui
import converter

inputFolder = easygui.diropenbox(msg='選擇欲轉檔之資料夾')
print(inputFolder)
if inputFolder is None:
    print('skip execution')
else:
    result, msg = converter.convert(inputFolder)
    print(f"result={result}, msg={msg}")
