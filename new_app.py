# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx


# import wx.xrc


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY,
                          title='CAD2Shp批次預處理器',
                          pos=wx.DefaultPosition,
                          size=wx.Size(600, 500))

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY,
                                           'CAD轉SHP的批次預處理器，可以協助GIS轉換的過程，將標註點位校正及炸裂圖塊。\n\n'
                                           '使用說明:\n\n'
                                           '1. 定義轉檔對象:\n'
                                           '1-1. 選擇檔案所在資料夾(資料夾內應包含數個xx年地形套疊圖檔)\n'
                                           '1-2. 選取要轉檔的對象(可複選)\n\n'
                                           '2. 定義批次對象\n'
                                           '2-1. 選擇批次資料夾所在路徑(每個資料夾內，皆應包含數個xx年地形套疊圖檔)\n'
                                           '2-1. 選取要批次的資料夾(可複選)',
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        self.m_staticText1.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        bSizer1.Add(self.m_staticText1, 0, wx.ALL, 5)

        self.m_staticline1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer1.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        gbSizer1 = wx.GridBagSizer(0, 0)
        gbSizer1.SetFlexibleDirection(wx.BOTH)
        gbSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"選擇資料夾", wx.Point(-1, -1), wx.DefaultSize, 0)
        gbSizer1.Add(self.m_button2, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"01 定義轉檔對象", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        gbSizer1.Add(self.m_staticText6, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        bSizer1.Add(gbSizer1, 1, wx.EXPAND, 5)

        gbSizer2 = wx.GridBagSizer(0, 0)
        gbSizer2.SetFlexibleDirection(wx.BOTH)
        gbSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"02 定義批次對象", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        gbSizer2.Add(self.m_staticText7, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"選擇資料夾", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer2.Add(self.m_button3, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        bSizer1.Add(gbSizer2, 1, wx.EXPAND, 5)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"開始轉換", wx.DefaultPosition, wx.Size(-1, -1), 0)
        bSizer1.Add(self.m_button4, 0, wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


# class MainApp(wx.App):
#     def OnInit(self):
#         mainFrame = MyFrame1(None)
#         mainFrame.show(True)
#         return True


if __name__ == '__main__':
    # app = MainApp()
    # app.MainLoop()
    app = wx.App()
    frame = MyFrame1(
        parent=None,  # 父層元件（已是頂層視窗，故無父層元件）
    )
    frame.Show()
    app.MainLoop()
