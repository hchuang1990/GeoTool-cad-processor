# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from os import listdir
from os.path import isfile, isdir, join
import glob

formats = ["dxf", "pdf", "tiff", "jpg"]
printers = ["DWG To PDF", "DWG To TIFF6", "PublishToWeb JPG"]
papers = ["ISO_full_bleed_A2_(594.00_x_420.00_MM)", "ISO full bleed A3 (420.00 x 297.00 MM)",
         "ISO full bleed A4 (297.00 x 210.00 MM)"]
# dwgs = ["58年地形套疊圖.dwg", "77年正射影像套疊圖.dwg", "77年地形套疊圖.dwg", "83年正射影像套疊圖.dwg", "83年地形套疊圖.dwg", "相關位置圖(107年地形圖).dwg"]
# folders = ["A020027", "A020028", "A020029", "A020030"]
folders = []
dwgs = []

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.resize(632, 741)
        Dialog.setWindowTitle("CAD批次作業")
        self.source_path = "E:chiao_studyprojectscad2shptestrun..."
        self.log_path = "E:chiao_studyprojectscad2shptestrun..."

        self.groupBox = QtWidgets.QGroupBox(Dialog, title="來源")
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 471, 391))
        self.label = QtWidgets.QLabel(self.groupBox, text="路徑")
        self.label.setGeometry(QtCore.QRect(20, 30, 58, 16))
        self.label_2 = QtWidgets.QLabel(self.groupBox, text="檔案")
        self.label_2.setGeometry(QtCore.QRect(250, 60, 121, 16))
        self.label_4 = QtWidgets.QLabel(self.groupBox, text="資料夾")
        self.label_4.setGeometry(QtCore.QRect(20, 60, 81, 16))

        self.listWidget_folder = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_folder.setGeometry(QtCore.QRect(20, 90, 211, 281))
        self.updateFolderList()

        self.listWidget_file = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_file.setGeometry(QtCore.QRect(250, 90, 201, 281))
        self.updateFileList()

        self.label_source_path = QtWidgets.QLabel(self.groupBox, text=self.source_path)
        self.label_source_path.setGeometry(QtCore.QRect(70, 30, 219, 15))


        self.btn_choose_folder = QtWidgets.QPushButton(self.groupBox, text="選擇")
        self.btn_choose_folder.setGeometry(QtCore.QRect(360, 28, 93, 25))
        self.btn_choose_folder.clicked.connect(self.onSourceBtnClick)

        self.btn_run = QtWidgets.QPushButton(Dialog, text="執行")
        self.btn_run.setGeometry(QtCore.QRect(510, 29, 93, 25))

        self.btn_cancel = QtWidgets.QPushButton(Dialog, text="取消")
        self.btn_cancel.setGeometry(QtCore.QRect(510, 60, 93, 25))
        self.btn_cancel.clicked.connect(self.btn_cancel_clicked)

        self.groupBox_2 = QtWidgets.QGroupBox(Dialog, title="動作")
        self.groupBox_2.setGeometry(QtCore.QRect(20, 420, 471, 251))

        self.cb_explode = QtWidgets.QCheckBox(self.groupBox_2, text="炸裂")
        self.cb_explode.setGeometry(QtCore.QRect(20, 37, 85, 18))

        self.btn_explode_logic = QtWidgets.QPushButton(self.groupBox_2, text="設定邏輯")
        self.btn_explode_logic.setGeometry(QtCore.QRect(140, 30, 311, 27))

        self.selectPaper = QtWidgets.QComboBox(self.groupBox_2)
        self.selectPaper.setGeometry(QtCore.QRect(140, 203, 311, 21))
        self.updateSelectPaper()

        self.label_11 = QtWidgets.QLabel(self.groupBox_2, text="紙張大小")
        self.label_11.setGeometry(QtCore.QRect(40, 203, 91, 16))

        self.selectFormat = QtWidgets.QComboBox(self.groupBox_2)
        self.selectFormat.setGeometry(QtCore.QRect(140, 120, 311, 21))
        self.updateSelectFormat()

        self.selectPrinter = QtWidgets.QComboBox(self.groupBox_2)
        self.selectPrinter.setGeometry(QtCore.QRect(140, 163, 201, 21))
        self.updateSelectPrinter()

        self.label_10 = QtWidgets.QLabel(self.groupBox_2, text="印表機")
        self.label_10.setGeometry(QtCore.QRect(40, 163, 91, 16))

        self.cb_saveAs = QtWidgets.QCheckBox(self.groupBox_2, text="另存新檔")
        self.cb_saveAs.setGeometry(QtCore.QRect(20, 80, 85, 18))

        self.label_12 = QtWidgets.QLabel(self.groupBox_2, text="格式")
        self.label_12.setGeometry(QtCore.QRect(41, 122, 91, 16))

        self.btn_definePrinter = QtWidgets.QPushButton(self.groupBox_2, text="連結")
        self.btn_definePrinter.setGeometry(QtCore.QRect(360, 161, 93, 25))

        self.log_path = QtWidgets.QLabel(Dialog, text=self.log_path)
        self.log_path.setGeometry(QtCore.QRect(150, 688, 219, 15))

        self.label_7 = QtWidgets.QLabel(Dialog, text="記錄檔保存位置")
        self.label_7.setGeometry(QtCore.QRect(20, 690, 105, 15))

        self.btn_log_path = QtWidgets.QPushButton(Dialog, text="變更")
        self.btn_log_path.setGeometry(QtCore.QRect(400, 682, 93, 28))

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def btn_cancel_clicked(self):
        self.exit()

    def exit(self):
        sys.exit(app.exec_())

    def onSourceBtnClick(self):
        try:
            global folders
            global dwgs
            folder_path_choose = QtWidgets.QFileDialog.getExistingDirectory(self.btn_choose_folder,
                                                                            "Open folder",
                                                                            "./")  # start path
            print(folder_path_choose)
            if folder_path_choose == "":
                self.windowAlert(title="系統提醒", message="取消選擇")
                return

            # update important variable: source_path, folders, files
            self.source_path = folder_path_choose
            arr = listdir(folder_path_choose)
            tmpFolderArr = []
            for f in arr:
                if isdir(join(folder_path_choose, f)):
                    tmpFolderArr.append(f)
            print("tmpFolderArr", tmpFolderArr)

            tmpFileArr = []
            for folder in tmpFolderArr:
                arr = listdir(join(folder_path_choose, folder))
                for f in arr:
                    if isfile(join(folder_path_choose, folder, f)) and ".DWG" in f:
                        tmpFileArr.append(f)
            print("tmpFileArr", tmpFileArr)

            if len(tmpFileArr) is 0 or len(tmpFolderArr) is 0:
                self.windowAlert(title="系統提醒", message="無有效資料夾或檔案")
                return

            folders = tmpFolderArr
            dwgs = tmpFileArr

            # update ui
            self.label_source_path.setText(folder_path_choose)
            self.updateFolderList()
            self.updateFileList()
        except Exception as e:
            self.windowAlert(title="系統提醒", message=str(e))

    def updateFolderList(self):
        self.listWidget_folder.clear()
        for folder in folders:
            item = QtWidgets.QListWidgetItem(folder)
            item.setCheckState(QtCore.Qt.Checked)
            self.listWidget_folder.addItem(item)

    def updateFileList(self):
        self.listWidget_file.clear()
        for dwg in dwgs:
            item = QtWidgets.QListWidgetItem(dwg)
            item.setCheckState(QtCore.Qt.Checked)
            self.listWidget_file.addItem(item)

    def updateSelectPrinter(self):
        for printer in printers:
            self.selectPrinter.addItem(printer)

    def updateSelectFormat(self):
        for format in formats:
            self.selectFormat.addItem(format)

    def updateSelectPaper(self):
        for paper in papers:
            self.selectPaper.addItem(paper)

    def windowAlert(self, title, message):
        QtWidgets.QMessageBox.information(None, title, message)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())
