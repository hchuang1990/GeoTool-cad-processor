# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import sys
from os import listdir
from os.path import isfile, isdir, join
from cadprocess.common import handler
import logging
import datetime

# import cadprocess.common.handler as handler
# from cadprocess.common.handler import handler
# import cadprocess.common.handler as handler

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s',
    datefmt='%Y%m%d %H:%M:%S')

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)

log_dir = os.path.join(os.path.normpath(os.getcwd() + os.sep), 'logs')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
log_filename = os.path.join(log_dir,datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S.log"))

fh = logging.FileHandler(log_filename)
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)
    

# formats = ["dwg", "dxf", "pdf", "tiff", "jpg", "dgn"]
formats = ["dwg", "dxf", "tiff", "jpg", "dgn"]
printers = ["DWG To PDF", "DWG To TIFF6", "PublishToWeb JPG"]
papers = ["ISO_full_bleed_A2_(594.00_x_420.00_MM)", "ISO full bleed A3 (420.00 x 297.00 MM)",
          "ISO full bleed A4 (297.00 x 210.00 MM)"]
# dwgs = ["58年地形套疊圖.dwg", "77年正射影像套疊圖.dwg", "77年地形套疊圖.dwg", "83年正射影像套疊圖.dwg", "83年地形套疊圖.dwg", "相關位置圖(107年地形圖).dwg"]
# folders = ["A020027", "A020028", "A020029", "A020030"]
defaultPrinterPath = ""
printers = []
folders = []
dwgs = []
folderCheck = []
dwgCheck = []


class Ui_Dialog(object):

    def setupUi(self, dialog):
        global defaultPrinterPath
        try:
            logger.info('Start reading filepath of plot.config...')
            f = open('cadprocess/config/plot.config')
            text = f.read()
            print(text)
            logger.info(text)
            defaultPrinterPath = text
            f.close
            logger.info('Finished reading plot.config file.')
        except Exception as e:
            logger.error(f"Unexpected {e=}, {type(e)=}")
        dialog.setFixedSize(632, 800)
        dialog.setWindowTitle("CAD批次作業 - Powered by ZackHuang")
        self.source_path = "D:\\事業體\\05_可宸數位科技\\00_Project\\1111008_dwg2shp\\projects"
        self.log_path = "D:\\事業體\\05_可宸數位科技\\00_Project\\1111008_dwg2shp\\projects"

        self.groupBox = QtWidgets.QGroupBox(dialog, title="來源")
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 471, 391))
        self.label = QtWidgets.QLabel(self.groupBox, text="路徑")
        self.label.setGeometry(QtCore.QRect(20, 30, 58, 16))
        self.label_2 = QtWidgets.QLabel(self.groupBox, text="檔案")
        self.label_2.setGeometry(QtCore.QRect(250, 60, 121, 16))
        self.label_4 = QtWidgets.QLabel(self.groupBox, text="資料夾")
        self.label_4.setGeometry(QtCore.QRect(20, 60, 81, 16))

        self.listWidget_folder = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_folder.setGeometry(QtCore.QRect(20, 90, 211, 281))
        self.listWidget_folder.itemClicked.connect(self.onFolderItemChanged)
        self.updateFolderList()

        self.listWidget_dwg = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_dwg.setGeometry(QtCore.QRect(250, 90, 201, 281))
        self.listWidget_dwg.itemClicked.connect(self.onDwgItemChanged)
        self.updateDwgList()

        self.label_source_path = QtWidgets.QLabel(self.groupBox, text=self.source_path)
        self.label_source_path.setGeometry(QtCore.QRect(70, 30, 219, 15))

        self.btn_choose_folder = QtWidgets.QPushButton(self.groupBox, text="選擇")
        self.btn_choose_folder.setGeometry(QtCore.QRect(360, 28, 93, 25))
        self.btn_choose_folder.clicked.connect(self.onSourceBtnClick)

        self.btn_run = QtWidgets.QPushButton(dialog, text="執行")
        self.btn_run.setGeometry(QtCore.QRect(510, 29, 93, 25))
        self.btn_run.clicked.connect(self.btn_run_clicked)

        self.btn_cancel = QtWidgets.QPushButton(dialog, text="取消")
        self.btn_cancel.setGeometry(QtCore.QRect(510, 60, 93, 25))
        self.btn_cancel.clicked.connect(self.btn_cancel_clicked)

        self.groupBox_2 = QtWidgets.QGroupBox(dialog, title="動作")
        self.groupBox_2.setGeometry(QtCore.QRect(20, 420, 471, 270))

        self.groupBox_3 = QtWidgets.QGroupBox(dialog, title="記錄檔")
        self.groupBox_3.setGeometry(QtCore.QRect(20, 700, 471, 80))

        self.cb_explode = QtWidgets.QCheckBox(self.groupBox_2, text="炸裂")
        self.cb_explode.setGeometry(QtCore.QRect(20, 37, 85, 18))

        self.cb_adjust = QtWidgets.QCheckBox(self.groupBox_2, text="點校正")
        self.cb_adjust.setGeometry(QtCore.QRect(20, 77, 200, 18))

        self.selectAdjust = QtWidgets.QComboBox(self.groupBox_2)
        self.selectAdjust.setGeometry(QtCore.QRect(140, 77, 311, 21))
        self.selectAdjust.addItems(
            ["acAlignmentLeft",
             "acAlignmentCenter",
             "acAlignmentRight",
             "acAlignmentAligned",
             "acAlignmentMiddle",
             "acAlignmentFit",
             "acAlignmentTopLeft",
             "acAlignmentTopCenter",
             "acAlignmentTopRight",
             "acAlignmentMiddleLeft",
             "acAlignmentMiddleCenter",
             "acAlignmentMiddleRight",
             "acAlignmentBottomLeft",
             "acAlignmentBottomCenter",
             "acAlignmentBottomRight"]
        )

        self.selectPaper = QtWidgets.QComboBox(self.groupBox_2)
        self.selectPaper.setGeometry(QtCore.QRect(140, 230, 311, 21))
        self.updateSelectPaper()

        self.label_11 = QtWidgets.QLabel(self.groupBox_2, text="紙張大小")
        self.label_11.setGeometry(QtCore.QRect(40, 230, 91, 16))


        self.selectFormat = QtWidgets.QComboBox(self.groupBox_2)
        self.selectFormat.setGeometry(QtCore.QRect(140, 150, 311, 21))
        self.updateSelectFormat()
        self.selectFormat.currentTextChanged.connect(self.onOnFormatChanged)

        self.selectPrinter = QtWidgets.QComboBox(self.groupBox_2)
        self.selectPrinter.setGeometry(QtCore.QRect(140, 190, 201, 21))
        self.updateSelectPrinter()

        self.label_10 = QtWidgets.QLabel(self.groupBox_2, text="印表機")
        self.label_10.setGeometry(QtCore.QRect(40, 190, 91, 16))

        self.cb_saveAs = QtWidgets.QCheckBox(self.groupBox_2, text="另存新檔")
        self.cb_saveAs.setGeometry(QtCore.QRect(20, 117, 85, 18))
        self.cb_saveAs.clicked.connect(self.onSaveAsClick)
        self.onSaveAsClick()

        self.label_12 = QtWidgets.QLabel(self.groupBox_2, text="格式")
        self.label_12.setGeometry(QtCore.QRect(41, 150, 91, 16))

        self.btn_definePrinter = QtWidgets.QPushButton(self.groupBox_2, text="連結")
        self.btn_definePrinter.setGeometry(QtCore.QRect(360, 188, 93, 25))
        self.btn_definePrinter.clicked.connect(self.onPrinterPathClick)

        self.label_log_path = QtWidgets.QLabel(dialog, text=self.log_path)
        self.label_log_path.setGeometry(QtCore.QRect(120, 740, 219, 15))

        self.label_7 = QtWidgets.QLabel(dialog, text="保存位置")
        self.label_7.setGeometry(QtCore.QRect(40, 740, 105, 15))

        self.btn_log_path = QtWidgets.QPushButton(dialog, text="變更")
        self.btn_log_path.setGeometry(QtCore.QRect(380, 730, 93, 28))

        QtCore.QMetaObject.connectSlotsByName(dialog)

    def btn_run_clicked(self):
        actionObject = {
            "source_path": self.source_path,
            "folders": folderCheck,
            "dwgs": dwgCheck,
            "explode": self.cb_explode.isChecked(),
            "saveAs": self.cb_saveAs.isChecked(),
            "format": self.selectFormat.currentText(),
            "printer": self.selectPrinter.currentText(),
            "papper": self.selectPaper.currentText(),
            "log_path": self.log_path,
            "adjust": self.cb_adjust.isChecked(),
            "adjust_direction": self.selectAdjust.currentIndex()
        }
        print(actionObject)
        logger.info(actionObject)
        if len(folderCheck) is 0 or len(dwgCheck) is 0:
            self.windowAlert(title="系統提醒", message="請選取有效的資料")
            return
        if self.cb_saveAs.isChecked() and self.selectFormat in ["pdf", "tiff", "jpg"]:
            if self.selectPrinter.currentText() == '' or self.selectPaper.currentText() == '':
                self.windowAlert(title="系統提醒", message="請選擇正確的存檔設定")
                return
        if self.cb_saveAs.isChecked() is False and self.cb_explode.isChecked() is False and self.cb_adjust.isChecked() is False:
            self.windowAlert(title="系統提醒", message="請至少選擇一個的動作")
            return
        handler.handle(actionObject)
        # print(json.dumps(actionObject))

    def onOnFormatChanged(self, value):
        self.selectPrinter.setEnabled(value in ["pdf", "tiff", "jpg"])
        self.selectPaper.setEnabled(value in ["pdf", "tiff", "jpg"])

    def btn_cancel_clicked(self):
        self.exit()

    def exit(self):
        sys.exit(app.exec_())

    def onSaveAsClick(self):
        self.selectFormat.setEnabled(self.cb_saveAs.isChecked())
        self.onOnFormatChanged(formats[0])

    def onPrinterPathClick(self):
        global defaultPrinterPath
        try:
            folder_path_choose = QtWidgets.QFileDialog.getExistingDirectory(self.btn_definePrinter,
                                                                            "Choose Autodesk Plotter",
                                                                            "C:\\")  # start path
            defaultPrinterPath = folder_path_choose
            self.updateSelectPrinter()
        except:
            pass

    def onSourceBtnClick(self):
        try:
            folder_path_choose = QtWidgets.QFileDialog.getExistingDirectory(self.btn_choose_folder,
                                                                            "Open folder",
                                                                            "./")  # start path
            print(folder_path_choose)
            logger.info(f"Choosing folder_path is the {folder_path_choose}")
            if folder_path_choose == "":
                # self.windowAlert(title="系統提醒", message="取消選擇")
                return

            # update text and folder list
            self.source_path = folder_path_choose
            self.label_source_path.setText(self.source_path)
            self.updateFolderList()

        except Exception as e:
            self.windowAlert(title="系統提醒", message=str(e))

    def updateFolderList(self):
        global folders
        try:
            arr = listdir(self.source_path)
            tmpFolderArr = []
            for f in arr:
                if isdir(join(self.source_path, f)):
                    tmpFolderArr.append(f)
            folders = tmpFolderArr
            self.listWidget_folder.clear()
            for folder in folders:
                item = QtWidgets.QListWidgetItem(folder)
                item.setCheckState(QtCore.Qt.Checked)
                self.listWidget_folder.addItem(item)
            self.onFolderItemChanged()
        except:
            pass

    def updateDwgList(self):
        global dwgs
        try:
            tmpFileArr = set()
            for folder in folderCheck:
                arr = listdir(join(self.source_path, folder))
                for f in arr:
                    if isfile(join(self.source_path, folder, f)) and ".DWG" in f:
                        tmpFileArr.add(f'%_{f.split("_")[1]}')

            dwgs = list(tmpFileArr)
            self.listWidget_dwg.clear()
            for dwg in dwgs:
                item = QtWidgets.QListWidgetItem(dwg)
                item.setCheckState(QtCore.Qt.Checked)
                self.listWidget_dwg.addItem(item)
            self.onDwgItemChanged()
        except:
            pass

    def updateSelectPrinter(self):
        global printers
        global defaultPrinterPath
        arr = listdir(defaultPrinterPath)
        tmpPrinterArr = []
        for f in arr:
            if isfile(join(defaultPrinterPath, f)) and ".pc3" in f:
                tmpPrinterArr.append(f)
        printers = tmpPrinterArr
        print(tmpPrinterArr)
        logger.info(tmpPrinterArr)
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

    def onFolderItemChanged(self):
        global folderCheck
        global dwgs
        folderCheck.clear()
        for index in range(self.listWidget_folder.count()):
            if self.listWidget_folder.item(index).checkState() == 2:  # 2==checked
                folderCheck.append(self.listWidget_folder.item(index).text())

        self.updateDwgList()

    def onDwgItemChanged(self):
        global dwgCheck
        dwgCheck.clear()
        for index in range(self.listWidget_dwg.count()):
            if self.listWidget_dwg.item(index).checkState() == 2:  # 2==checked
                dwgCheck.append(self.listWidget_dwg.item(index).text())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    try:
        dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(dialog)
        dialog.show()
    except Exception as e:
        print(e)
        logger.error(f"Unexpected {e=}, {type(e)=}")
    sys.exit(app.exec_())
