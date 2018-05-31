# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(343, 831)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("bg:rgb(214, 214, 0);\n" "font: 10pt \"Times New Roman\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 160, 321, 121))
        # self.groupBox.setMaximumSize(QtCore.QSize(321, 16777215))
        self.groupBox.setObjectName("groupBox")

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        # self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 290, 321, 81))
        self.groupBox_2.setObjectName("groupBox_2")

        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 380, 321, 81))
        self.groupBox_3.setObjectName("groupBox_3")

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(20, 180, 82, 17))
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 200, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")

        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 220, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")

        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(20, 260, 82, 17))
        self.radioButton_4.setObjectName("radioButton_4")

        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(20, 240, 82, 17))
        self.radioButton_5.setObjectName("radioButton_5")

        self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_6.setGeometry(QtCore.QRect(180, 180, 82, 17))
        self.radioButton_6.setObjectName("radioButton_6")

        self.radioButton_7 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_7.setGeometry(QtCore.QRect(180, 200, 82, 17))
        self.radioButton_7.setObjectName("radioButton_7")

        self.radioButton_8 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_8.setGeometry(QtCore.QRect(180, 220, 82, 17))
        self.radioButton_8.setObjectName("radioButton_8")

        self.radioButton_9 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_9.setGeometry(QtCore.QRect(180, 240, 82, 17))
        self.radioButton_9.setObjectName("radioButton_9")

        self.radioButton_10 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_10.setGeometry(QtCore.QRect(180, 260, 82, 17))
        self.radioButton_10.setObjectName("radioButton_10")

        self.radioButton_11 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_11.setGeometry(QtCore.QRect(20, 310, 82, 17))
        self.radioButton_11.setObjectName("radioButton_11")

        self.radioButton_12 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_12.setGeometry(QtCore.QRect(20, 350, 82, 17))
        self.radioButton_12.setObjectName("radioButton_12")

        self.radioButton_13 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_13.setGeometry(QtCore.QRect(20, 330, 82, 17))
        self.radioButton_13.setObjectName("radioButton_13")

        self.radioButton_14 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_14.setGeometry(QtCore.QRect(180, 310, 82, 17))
        self.radioButton_14.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.radioButton_14.setObjectName("radioButton_14")

        self.radioButton_15 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_15.setGeometry(QtCore.QRect(180, 330, 82, 17))
        self.radioButton_15.setObjectName("radioButton_15")

        self.radioButton_16 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_16.setGeometry(QtCore.QRect(180, 350, 82, 17))
        self.radioButton_16.setObjectName("radioButton_16")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 100, 161, 51))
        self.textEdit.setStyleSheet("font: 75 24pt \"Times New Roman\";")
        self.textEdit.setObjectName("textEdit")

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 20, 71, 31))
        self.textEdit_2.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.textEdit_2.setObjectName("textEdit_2")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 71, 20))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 121, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 80, 47, 13))
        self.label_3.setObjectName("label_3")

# <!---- progres Bar
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 650, 301, 23))
        self.progressBar.setStyleSheet("font: bold 10pt \"Times New Roman\";")
        self.progressBar.setProperty("value", 9)    # need sent data instead 9
        self.progressBar.setObjectName("progressBar")
# progres Bar ----!>

        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(20, 530, 301, 71))
        self.textEdit_3.setObjectName("textEdit_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 510, 171, 16))
        self.label_4.setObjectName("label_4")

        self.radioButton_19 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_19.setGeometry(QtCore.QRect(20, 440, 82, 17))
        self.radioButton_19.setObjectName("radioButton_18")

        self.radioButton_18 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_18.setGeometry(QtCore.QRect(20, 420, 82, 17))
        self.radioButton_18.setObjectName("radioButton_19")

        self.radioButton_17 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_17.setGeometry(QtCore.QRect(20, 400, 82, 17))
        self.radioButton_17.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.radioButton_17.setObjectName("radioButton_17")

        self.radioButton_22 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_22.setGeometry(QtCore.QRect(180, 440, 82, 16))
        self.radioButton_22.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.radioButton_22.setObjectName("radioButton_22")

        self.radioButton_20 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_20.setGeometry(QtCore.QRect(180, 400, 82, 17))
        self.radioButton_20.setObjectName("radioButton_20")

        self.radioButton_21 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_21.setGeometry(QtCore.QRect(180, 420, 82, 17))
        self.radioButton_21.setObjectName("radioButton_21")

        self.radioButton_23 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_23.setGeometry(QtCore.QRect(20, 470, 82, 17))
        self.radioButton_23.setObjectName("radioButton_23")

        self.radioButton_24 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_24.setGeometry(QtCore.QRect(20, 490, 82, 17))
        self.radioButton_24.setObjectName("radioButton_24")

        self.radioButton_25 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_25.setGeometry(QtCore.QRect(180, 470, 82, 17))
        self.radioButton_25.setObjectName("radioButton_25")

        self.radioButton_26 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_26.setGeometry(QtCore.QRect(180, 490, 82, 17))
        self.radioButton_26.setObjectName("radioButton_26")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(190, 0, 71, 20))
        self.label_5.setObjectName("label_5")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 610, 111, 31))
        self.pushButton.setStyleSheet("font: 75 bold 18pt \"Times New Roman\";bg:rgb(214, 214, 0);")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 610, 131, 31))
        self.pushButton_2.setStyleSheet("font: 75 bold 10pt \"Times New Roman\"")
        self.pushButton_2.setObjectName("pushButton_2")

        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(130, 20, 191, 51))
        self.textEdit_4.setStyleSheet("font: 8pt \"Calibri\";")
        self.textEdit_4.setObjectName("textEdit_4")

        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(230, 100, 91, 51))
        self.textEdit_5.setStyleSheet("font: 75 24pt \"Times New Roman\";")
        self.textEdit_5.setObjectName("textEdit_5")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 680, 151, 31))
        self.pushButton_3.setStyleSheet("font: 75 9pt \"Times New Roman\"")
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(180, 680, 151, 31))
        self.pushButton_4.setStyleSheet("font: 75 9pt \"Times New Roman\"")
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 720, 321, 31))
        self.pushButton_5.setStyleSheet("font: 75 bold 14pt \"Times New Roman\"")
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 760, 151, 31))
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(180, 760, 151, 31))
        self.pushButton_7.setObjectName("pushButton_7")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        MainWindow.insertToolBarBreak(self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.textEdit_2, self.textEdit_4)
        MainWindow.setTabOrder(self.textEdit_4, self.textEdit)
        MainWindow.setTabOrder(self.textEdit, self.textEdit_5)
        MainWindow.setTabOrder(self.textEdit_5, self.radioButton)
        MainWindow.setTabOrder(self.radioButton, self.radioButton_2)
        MainWindow.setTabOrder(self.radioButton_2, self.radioButton_3)
        MainWindow.setTabOrder(self.radioButton_3, self.radioButton_5)
        MainWindow.setTabOrder(self.radioButton_5, self.radioButton_4)
        MainWindow.setTabOrder(self.radioButton_4, self.radioButton_6)
        MainWindow.setTabOrder(self.radioButton_6, self.radioButton_7)
        MainWindow.setTabOrder(self.radioButton_7, self.radioButton_8)
        MainWindow.setTabOrder(self.radioButton_8, self.radioButton_9)
        MainWindow.setTabOrder(self.radioButton_9, self.radioButton_10)
        MainWindow.setTabOrder(self.radioButton_10, self.radioButton_11)
        MainWindow.setTabOrder(self.radioButton_11, self.radioButton_13)
        MainWindow.setTabOrder(self.radioButton_13, self.radioButton_12)
        MainWindow.setTabOrder(self.radioButton_12, self.radioButton_14)
        MainWindow.setTabOrder(self.radioButton_14, self.radioButton_15)
        MainWindow.setTabOrder(self.radioButton_15, self.radioButton_16)
        MainWindow.setTabOrder(self.radioButton_16, self.radioButton_17)
        MainWindow.setTabOrder(self.radioButton_17, self.radioButton_19)
        MainWindow.setTabOrder(self.radioButton_19, self.radioButton_18)
        MainWindow.setTabOrder(self.radioButton_18, self.radioButton_22)
        MainWindow.setTabOrder(self.radioButton_22, self.radioButton_20)
        MainWindow.setTabOrder(self.radioButton_20, self.radioButton_21)
        MainWindow.setTabOrder(self.radioButton_21, self.radioButton_23)
        MainWindow.setTabOrder(self.radioButton_23, self.radioButton_24)
        MainWindow.setTabOrder(self.radioButton_24, self.radioButton_25)
        MainWindow.setTabOrder(self.radioButton_25, self.radioButton_26)
        MainWindow.setTabOrder(self.radioButton_26, self.textEdit_3)
        MainWindow.setTabOrder(self.textEdit_3, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.pushButton_4)
        MainWindow.setTabOrder(self.pushButton_4, self.pushButton_5)
        MainWindow.setTabOrder(self.pushButton_5, self.pushButton_6)
        MainWindow.setTabOrder(self.pushButton_6, self.pushButton_7)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DownTime -Lviv"))
        self.radioButton.setText(_translate("MainWindow", "1 value"))
        self.radioButton_2.setText(_translate("MainWindow", "2 value"))
        self.radioButton_3.setText(_translate("MainWindow", "3 value"))
        self.radioButton_4.setText(_translate("MainWindow", "5 value"))
        self.radioButton_5.setText(_translate("MainWindow", "4 value"))
        self.radioButton_6.setText(_translate("MainWindow", "6 value"))
        self.radioButton_7.setText(_translate("MainWindow", "7 value"))
        self.radioButton_8.setText(_translate("MainWindow", "8 value"))
        self.radioButton_9.setText(_translate("MainWindow", "9 value"))
        self.radioButton_10.setText(_translate("MainWindow", "10 value"))
        self.radioButton_11.setText(_translate("MainWindow", "11 value"))
        self.radioButton_12.setText(_translate("MainWindow", "13 value"))
        self.radioButton_13.setText(_translate("MainWindow", "12 value"))
        self.radioButton_14.setText(_translate("MainWindow", "14 value"))
        self.radioButton_15.setText(_translate("MainWindow", "15 value"))
        self.radioButton_16.setText(_translate("MainWindow", "16 value"))
        self.textEdit.setWhatsThis(_translate("MainWindow", "equipment number"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:24pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.label.setText(_translate("MainWindow", "you number"))
        self.label_2.setText(_translate("MainWindow", "equipment number"))
        self.label_3.setText(_translate("MainWindow", "minutes"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "notice"))
        self.groupBox.setTitle(_translate("MainWindow", "Komax"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Applicator"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Welding"))
        self.radioButton_19.setText(_translate("MainWindow", "19 value"))
        self.radioButton_18.setText(_translate("MainWindow", "18 value"))
        self.radioButton_17.setText(_translate("MainWindow", "17 value"))
        self.radioButton_22.setText(_translate("MainWindow", "22 value"))
        self.radioButton_20.setText(_translate("MainWindow", "20 value"))
        self.radioButton_21.setText(_translate("MainWindow", "21 value"))
        self.radioButton_23.setText(_translate("MainWindow", "23 value"))
        self.radioButton_24.setText(_translate("MainWindow", "24 value"))
        self.radioButton_25.setText(_translate("MainWindow", "25 value"))
        self.radioButton_26.setText(_translate("MainWindow", "26 value"))
        self.label_5.setText(_translate("MainWindow", "status of run"))
        self.pushButton.setText(_translate("MainWindow", "ADD"))
        self.pushButton_2.setText(_translate("MainWindow", "create table per shift"))
        self.textEdit_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Calibri\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.textEdit_5.setWhatsThis(_translate("MainWindow", "equipment number"))
        self.textEdit_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:24pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "show of last 2shifts"))
        self.pushButton_4.setText(_translate("MainWindow", "show of last 10shifts/week"))
        self.pushButton_5.setText(_translate("MainWindow", "show DownTime of last month"))
        self.pushButton_6.setText(_translate("MainWindow", "show equipment history"))
        self.pushButton_7.setText(_translate("MainWindow", "1111111"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

