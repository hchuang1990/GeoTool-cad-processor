import json
import sys
from easygui import *
from os import listdir
from os.path import isfile, isdir, join

app_name = 'CAD2Shp批次預處理器'
try:
    output = ccbox(title=app_name,
                   msg='CAD轉SHP的批次預處理器，可以協助GIS轉換的過程，將標註點位校正及炸裂圖塊。\n\n'
                       '使用說明:\n\n'
                       '1. 定義轉檔對象:\n'
                       '1-1. 選擇檔案所在資料夾(資料夾內應包含數個xx年地形套疊圖檔)\n'
                       '1-2. 選取要轉檔的對象(可複選)\n\n'
                       '2. 定義批次對象\n'
                       '2-1. 選擇批次資料夾所在路徑(每個資料夾內，皆應包含數個xx年地形套疊圖檔)\n'
                       '2-1. 選取要批次的資料夾(可複選)'
                   )
    if output is False or output is None:
        sys.exit(0)

    # 01 Step01 Template Define
    path = diropenbox(title=app_name, msg='選擇檔案所在資料夾(資料夾內應包含數個xx年地形套疊圖檔)')
    print('path', path)
    if path is None:
        sys.exit(0)

    files = listdir(path)
    template_choices = []
    activate_template = []
    for f in files:
        fullpath = join(path, f)
        if isfile(fullpath) and '年地形套疊圖' in f:
            template_choices.append(f)

    if len(template_choices) == 0:
        raise Exception('資料夾內沒有目標資料，資料夾內應至少包含數個xx年地形套疊圖檔')

    activate_template = multchoicebox(title=app_name,
                                      msg='選取要轉檔的對象(可複選)',
                                      choices=template_choices)

    if activate_template is None:
        sys.exit(0)

    if len(activate_template)<=0:
        raise Exception('未定義轉檔對象')

    # Step02 Batch Folder Define
    path = diropenbox(title=app_name,
                      msg='選擇批次資料夾所在路徑(每個資料夾內，皆應包含數個xx年地形套疊圖檔)')
    if path is None:
        sys.exit(0)

    files = listdir(path)
    batch_folder_choices = []
    active_batch_folder = []

    for f in files:
        fullpath = join(path, f)
        if isdir(fullpath):
            batch_folder_choices.append(f)

    if len(active_batch_folder) <= 0:
        raise Exception('資料夾內沒有任何可供轉檔的批次對象')

    active_batch_folder = multchoicebox(title=app_name,
                                        msg=f'選取要批次的資料夾(可複選)\n 請確認資料夾內包含以下檔案: {json.dumps(activate_template)}',
                                        choices=batch_folder_choices)

    if active_batch_folder is None:
        sys.exit(0)

    if len(active_batch_folder):
        raise Exception('未定義轉檔資料夾')

except Exception as e:
    # ccbox(msg=str(e))
    exceptionbox(title=app_name, msg=str(e))

import easygui
# import converter

# inputFolder = easygui.diropenbox(msg='選擇欲轉檔之資料夾')
# print(inputFolder)
# if inputFolder is None:
#     print('skip execution')
# else:
#     result, msg = converter.convert(inputFolder)
#     print(f"result={result}, msg={msg}")


# import wx
#
# class MyFrame(wx.Frame):
#     def __init__(self):
#         super().__init__(parent=None, title='CAD Processor')
#         panel = wx.Panel(self)
#
#         # self.text_ctrl = wx.TextCtrl(panel, pos=(5, 5))
#         # my_btn = wx.Button(panel, label='Press Me', pos=(5, 55))
#
#         wx.StaticText(panel, -1, "第三個論點是flag。如果你願意，你實際上可以傳入多個標誌，只要你用豎線字符分隔它們：|。wxPython 工具包使用|一系列按位或來添加標誌。")
#         self.Show()
#
# if __name__ == '__main__':
#     app = wx.App()
#     frame = MyFrame()
#     app.MainLoop()
