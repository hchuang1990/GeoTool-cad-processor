# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.resize(632, 741)
        Dialog.setModal(False)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 471, 391))
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 58, 16))
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(250, 60, 121, 16))
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 58, 16))
        self.label_3.setText("")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 81, 16))
        self.listWidget_folder = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_folder.setGeometry(QtCore.QRect(250, 90, 201, 281))
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.listWidget_folder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.listWidget_folder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.listWidget_folder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.listWidget_folder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.listWidget_folder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.listWidget_folder.addItem(item)
        self.label_source = QtWidgets.QLabel(self.groupBox)
        self.label_source.setGeometry(QtCore.QRect(70, 30, 219, 15))
        self.listWidget_file = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_file.setGeometry(QtCore.QRect(20, 90, 211, 281))
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.listWidget_file.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.listWidget_file.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_file.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_file.addItem(item)
        self.btn_choose_folder = QtWidgets.QPushButton(self.groupBox)
        self.btn_choose_folder.setGeometry(QtCore.QRect(360, 28, 93, 25))
        self.btn_choose_folder.clicked.connect(self.onSourceBtnClick)
        self.btn_run = QtWidgets.QPushButton(Dialog)
        self.btn_run.setGeometry(QtCore.QRect(510, 29, 93, 25))
        self.btn_cancel = QtWidgets.QPushButton(Dialog)
        self.btn_cancel.setGeometry(QtCore.QRect(510, 60, 93, 25))
        self.btn_cancel.clicked.connect(self.btn_cancel_clicked)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 420, 471, 251))
        self.cb_explode = QtWidgets.QCheckBox(self.groupBox_2)
        self.cb_explode.setGeometry(QtCore.QRect(20, 37, 85, 18))
        self.btn_explode_logic = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_explode_logic.setGeometry(QtCore.QRect(140, 30, 311, 27))
        self.selectPaper = QtWidgets.QComboBox(self.groupBox_2)
        self.selectPaper.setGeometry(QtCore.QRect(140, 203, 311, 21))
        self.selectPaper.addItem("")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(40, 203, 91, 16))
        self.selectFormat = QtWidgets.QComboBox(self.groupBox_2)
        self.selectFormat.setGeometry(QtCore.QRect(140, 120, 311, 21))
        self.selectFormat.addItem("")
        self.selectFormat.addItem("")
        self.selectFormat.addItem("")
        self.selectFormat.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_4.setGeometry(QtCore.QRect(140, 163, 201, 21))
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(40, 163, 91, 16))
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 80, 85, 18))
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(41, 122, 91, 16))
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_7.setGeometry(QtCore.QRect(360, 161, 93, 25))
        self.label_log_path = QtWidgets.QLabel(Dialog)
        self.label_log_path.setGeometry(QtCore.QRect(150, 688, 219, 15))
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 690, 105, 15))
        self.btn_log_path = QtWidgets.QPushButton(Dialog)
        self.btn_log_path.setGeometry(QtCore.QRect(400, 682, 93, 28))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "CAD批次作業"))
        self.groupBox.setTitle(_translate("Dialog", "來源"))
        self.label.setText(_translate("Dialog", "路徑"))
        self.label_2.setText(_translate("Dialog", "檔案"))
        self.label_4.setText(_translate("Dialog", "資料夾"))
        __sortingEnabled = self.listWidget_folder.isSortingEnabled()
        self.listWidget_folder.setSortingEnabled(False)
        item = self.listWidget_folder.item(0)
        item.setText(_translate("Dialog", "58年地形套疊圖.dwg"))
        item = self.listWidget_folder.item(1)
        item.setText(_translate("Dialog", "77年正射影像套疊圖.dwg"))
        item = self.listWidget_folder.item(2)
        item.setText(_translate("Dialog", "77年地形套疊圖.dwg"))
        item = self.listWidget_folder.item(3)
        item.setText(_translate("Dialog", "83年正射影像套疊圖.dwg"))
        item = self.listWidget_folder.item(4)
        item.setText(_translate("Dialog", "83年地形套疊圖.dwg"))
        item = self.listWidget_folder.item(5)
        item.setText(_translate("Dialog", "相關位置圖(107年地形圖).dwg"))
        self.listWidget_folder.setSortingEnabled(__sortingEnabled)
        self.label_source.setText(_translate("Dialog", "E:chiao_studyprojectscad2shptestrun..."))
        __sortingEnabled = self.listWidget_file.isSortingEnabled()
        self.listWidget_file.setSortingEnabled(False)
        item = self.listWidget_file.item(0)
        item.setText(_translate("Dialog", "A020027"))
        item = self.listWidget_file.item(1)
        item.setText(_translate("Dialog", "A020028"))
        item = self.listWidget_file.item(2)
        item.setText(_translate("Dialog", "A020029"))
        item = self.listWidget_file.item(3)
        item.setText(_translate("Dialog", "A020030"))
        self.listWidget_file.setSortingEnabled(__sortingEnabled)
        self.btn_choose_folder.setText(_translate("Dialog", "選擇"))
        self.btn_run.setText(_translate("Dialog", "執行"))
        self.btn_cancel.setText(_translate("Dialog", "取消"))
        self.groupBox_2.setTitle(_translate("Dialog", "動作"))
        self.cb_explode.setText(_translate("Dialog", "炸裂"))
        self.btn_explode_logic.setText(_translate("Dialog", "設定邏輯"))
        self.selectPaper.setItemText(0, _translate("Dialog", "ISO_full_bleed_A2_(594.00_x_420.00_MM)"))
        self.label_11.setText(_translate("Dialog", "紙張大小"))
        self.selectFormat.setItemText(0, _translate("Dialog", "dxf"))
        self.selectFormat.setItemText(1, _translate("Dialog", "pdf"))
        self.selectFormat.setItemText(2, _translate("Dialog", "tiff"))
        self.selectFormat.setItemText(3, _translate("Dialog", "jpg"))
        self.comboBox_4.setItemText(0, _translate("Dialog", "DWG To PDF"))
        self.comboBox_4.setItemText(1, _translate("Dialog", "DWG To TIFF6"))
        self.comboBox_4.setItemText(2, _translate("Dialog", "PublishToWeb JPG"))
        self.label_10.setText(_translate("Dialog", "印表機"))
        self.checkBox_2.setText(_translate("Dialog", "另存新檔"))
        self.label_12.setText(_translate("Dialog", "格式"))
        self.pushButton_7.setText(_translate("Dialog", "連結"))
        self.label_log_path.setText(_translate("Dialog", "E:chiao_studyprojectscad2shptestrun..."))
        self.label_7.setText(_translate("Dialog", "記錄檔保存位置"))
        self.btn_log_path.setText(_translate("Dialog", "變更"))

    def btn_cancel_clicked(self):
        self.exit()

    def exit(self):
        sys.exit(app.exec_())

    def onSourceBtnClick(self):
        dir_choose = QFileDialog.getExistingDirectory(self, "選取資料夾", self.cwd)
        # if filename:
        #     print(filename)
        #     print(filetype)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
