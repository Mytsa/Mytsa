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
        MainWindow.resize(343, 825)
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

        self.radioButton_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_1.setGeometry(QtCore.QRect(20, 180, 150, 17))
        self.radioButton_1.setObjectName("radioButton")

        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 200, 150, 17))
        self.radioButton_2.setObjectName("radioButton_2")

        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 220, 150, 17))
        self.radioButton_3.setObjectName("radioButton_3")

        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(20, 260, 150, 17))
        self.radioButton_4.setObjectName("radioButton_4")

        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(20, 240, 150, 17))
        self.radioButton_5.setObjectName("radioButton_5")

        self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_6.setGeometry(QtCore.QRect(180, 180, 150, 17))
        self.radioButton_6.setObjectName("radioButton_6")

        self.radioButton_7 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_7.setGeometry(QtCore.QRect(180, 200, 150, 17))
        self.radioButton_7.setObjectName("radioButton_7")

        self.radioButton_8 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_8.setGeometry(QtCore.QRect(180, 220, 150, 17))
        self.radioButton_8.setObjectName("radioButton_8")

        self.radioButton_9 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_9.setGeometry(QtCore.QRect(180, 240, 150, 17))
        self.radioButton_9.setObjectName("radioButton_9")

        self.radioButton_10 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_10.setGeometry(QtCore.QRect(180, 260, 150, 17))
        self.radioButton_10.setObjectName("radioButton_10")

        self.radioButton_11 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_11.setGeometry(QtCore.QRect(20, 310, 150, 17))
        self.radioButton_11.setObjectName("radioButton_11")

        self.radioButton_12 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_12.setGeometry(QtCore.QRect(20, 350, 150, 17))
        self.radioButton_12.setObjectName("radioButton_12")

        self.radioButton_13 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_13.setGeometry(QtCore.QRect(20, 330, 150, 17))
        self.radioButton_13.setObjectName("radioButton_13")

        # self.radioButton_14 = QtWidgets.QRadioButton(self.centralwidget)
        # self.radioButton_14.setGeometry(QtCore.QRect(180, 300, 150, 17))
        # self.radioButton_14.setStyleSheet("font: 10pt \"Times New Roman\";")
        # self.radioButton_14.setObjectName("radioButton_14")

        self.radioButton_15 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_15.setGeometry(QtCore.QRect(180, 305, 150, 17))
        self.radioButton_15.setObjectName("radioButton_15")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(205, 325, 150, 15))
        self.label_6.setObjectName("label_6")

        self.apl = QtWidgets.QTextEdit(self.centralwidget)
        self.apl.setGeometry(QtCore.QRect(210, 340, 100, 30))
        self.apl.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.apl.setObjectName("apl")


        # self.radioButton_16 = QtWidgets.QRadioButton(self.centralwidget)
        # self.radioButton_16.setGeometry(QtCore.QRect(180, 350, 82, 17))
        # self.radioButton_16.setObjectName("radioButton_16")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 0, 150, 16))
        self.label_2.setObjectName("eq_number")

        self.eq_number = QtWidgets.QTextEdit(self.centralwidget)
        self.eq_number.setGeometry(QtCore.QRect(120, 20, 90, 51))
        self.eq_number.setStyleSheet("font: 75 24pt \"Times New Roman\";")
        self.eq_number.setObjectName("eq_number")

        self.per_number = QtWidgets.QTextEdit(self.centralwidget)
        self.per_number.setGeometry(QtCore.QRect(10, 20, 71, 31))
        self.per_number.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.per_number.setObjectName("per_number")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 200, 20))
        self.label.setObjectName("label")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 0, 200, 13))
        self.label_3.setObjectName("minutes")
        
        self.minutes = QtWidgets.QTextEdit(self.centralwidget)
        self.minutes.setGeometry(QtCore.QRect(240, 20, 91, 51))
        self.minutes.setStyleSheet("font: 75 24pt \"Times New Roman\";")
        self.minutes.setObjectName("minutes")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 600, 171, 16))
        self.label_5.setObjectName("message")

        self.message = QtWidgets.QTextEdit(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(20, 620, 301, 71))
        self.message.setStyleSheet("font: 9pt \"Calibri\";")
        self.message.setObjectName("message")

# # <!---- progres Bar
#         self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
#         self.progressBar.setGeometry(QtCore.QRect(20, 650, 301, 23))
#         self.progressBar.setStyleSheet("font: bold 10pt \"Times New Roman\";")
#         self.progressBar.setProperty("value", 9)    # need sent data instead 9
#         self.progressBar.setObjectName("progressBar")
# # progres Bar ----!>

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 75, 71, 20))
        self.label_4.setObjectName("notice")

        self.notice = QtWidgets.QTextEdit(self.centralwidget)
        self.notice.setGeometry(QtCore.QRect(10, 95, 320, 55))
        self.notice.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.notice.setObjectName("notice")


        self.radioButton_19 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_19.setGeometry(QtCore.QRect(20, 440, 150, 17))
        self.radioButton_19.setObjectName("radioButton_18")

        self.radioButton_18 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_18.setGeometry(QtCore.QRect(20, 420, 150, 17))
        self.radioButton_18.setObjectName("radioButton_19")

        self.radioButton_17 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_17.setGeometry(QtCore.QRect(20, 400, 150, 17))
        self.radioButton_17.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.radioButton_17.setObjectName("radioButton_17")

        self.radioButton_22 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_22.setGeometry(QtCore.QRect(180, 440, 150, 16))
        self.radioButton_22.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.radioButton_22.setObjectName("radioButton_22")

        self.radioButton_20 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_20.setGeometry(QtCore.QRect(180, 400, 150, 17))
        self.radioButton_20.setObjectName("radioButton_20")

        self.radioButton_21 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_21.setGeometry(QtCore.QRect(180, 420, 150, 17))
        self.radioButton_21.setObjectName("radioButton_21")

        self.radioButton_23 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_23.setGeometry(QtCore.QRect(20, 470, 150, 17))
        self.radioButton_23.setObjectName("radioButton_23")

        self.radioButton_24 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_24.setGeometry(QtCore.QRect(20, 490, 150, 17))
        self.radioButton_24.setObjectName("radioButton_24")

        self.radioButton_25 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_25.setGeometry(QtCore.QRect(180, 470, 150, 17))
        self.radioButton_25.setObjectName("radioButton_25")

        # self.radioButton_26 = QtWidgets.QRadioButton(self.centralwidget)
        # self.radioButton_26.setGeometry(QtCore.QRect(180, 490, 150, 17))
        # self.radioButton_26.setObjectName("radioButton_26")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 515, 300, 80))
        self.pushButton.setStyleSheet("font: 75 bold 18pt \"Times New Roman\";bg:rgb(214, 214, 0);")
        self.pushButton.setObjectName("ADD")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 700, 131, 31))
        self.pushButton_2.setStyleSheet("font: 75 bold 10pt \"Times New Roman\"")
        self.pushButton_2.setObjectName("table for shift")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 700, 151, 31))
        self.pushButton_3.setObjectName("history")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(5, 58, 110, 31))
        self.pushButton_4.setObjectName("manual correction")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(190, 740, 131, 31))
        self.pushButton_5.setObjectName("clean table")

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 740, 151, 31))
        self.pushButton_6.setObjectName("contact info")


        

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(100, 772, 180, 20))
        self.label_10.setObjectName("Mytsa Viktor")

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
        MainWindow.setTabOrder(self.per_number, self.message)
        MainWindow.setTabOrder(self.message, self.eq_number)
        MainWindow.setTabOrder(self.eq_number, self.minutes)
        MainWindow.setTabOrder(self.minutes, self.radioButton_1)
        MainWindow.setTabOrder(self.radioButton_1, self.radioButton_2)
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
        MainWindow.setTabOrder(self.radioButton_12, self.radioButton_15)
        MainWindow.setTabOrder(self.radioButton_15, self.apl)
        MainWindow.setTabOrder(self.apl, self.radioButton_17)
        MainWindow.setTabOrder(self.radioButton_17, self.radioButton_19)
        MainWindow.setTabOrder(self.radioButton_19, self.radioButton_18)
        MainWindow.setTabOrder(self.radioButton_18, self.radioButton_22)
        MainWindow.setTabOrder(self.radioButton_22, self.radioButton_20)
        MainWindow.setTabOrder(self.radioButton_20, self.radioButton_21)
        MainWindow.setTabOrder(self.radioButton_21, self.radioButton_23)
        MainWindow.setTabOrder(self.radioButton_23, self.radioButton_24)
        MainWindow.setTabOrder(self.radioButton_24, self.radioButton_25)
        MainWindow.setTabOrder(self.radioButton_25, self.notice)
        # MainWindow.setTabOrder(self.radioButton_26, self.notice)
        MainWindow.setTabOrder(self.notice, self.pushButton)
        MainWindow.setTabOrder(self.pushButton_2, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.pushButton_4)
        MainWindow.setTabOrder(self.pushButton_4, self.pushButton_5)
        MainWindow.setTabOrder(self.pushButton_5, self.pushButton_6)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DownTime -Lviv"))
        self.radioButton_1.setText(_translate("MainWindow", "проблеми з матеріалом"))
        self.radioButton_2.setText(_translate("MainWindow", "механічна поломка"))
        self.radioButton_3.setText(_translate("MainWindow", "електрична поломка"))
        self.radioButton_4.setText(_translate("MainWindow", "CPU 2000"))
        self.radioButton_5.setText(_translate("MainWindow", "збій роботи сервера"))
        self.radioButton_6.setText(_translate("MainWindow", "інший тип простою"))
        self.radioButton_7.setText(_translate("MainWindow", "налаш. принтера"))
        self.radioButton_8.setText(_translate("MainWindow", "втулочний модуль"))
        self.radioButton_9.setText(_translate("MainWindow", "ПЗ"))
        self.radioButton_10.setText(_translate("MainWindow", "Технічний Огляд"))
        self.radioButton_11.setText(_translate("MainWindow", "механічне налаштування"))
        self.radioButton_12.setText(_translate("MainWindow", "налаштування розрізу"))
        self.radioButton_13.setText(_translate("MainWindow", "заміна з/ч"))
        # self.radioButton_14.setText(_translate("MainWindow", "зміна кроку подачі"))
        self.radioButton_15.setText(_translate("MainWindow", "ТО аплікатора"))

        # self.radioButton_16.setText(_translate("MainWindow", "16 value"))
        self.eq_number.setWhatsThis(_translate("MainWindow", "equipment number 8000:"))
        self.eq_number.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:24pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.per_number.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.label.setText(_translate("MainWindow", "you number"))
        self.label_2.setText(_translate("MainWindow", "equipment number 8000:"))
        self.label_3.setText(_translate("MainWindow", "minutes"))
        self.notice.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "коментар"))
        self.groupBox.setTitle(_translate("MainWindow", "Komax"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Applicator"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Welding"))
        self.radioButton_19.setText(_translate("MainWindow", "заміна електродів"))
        self.radioButton_18.setText(_translate("MainWindow", "новий проект/параметри"))
        self.radioButton_17.setText(_translate("MainWindow", "Збій програми"))
        self.radioButton_22.setText(_translate("MainWindow", "проблеми з матеріалом на зварці"))
        self.radioButton_20.setText(_translate("MainWindow", "чистка обладнання"))
        self.radioButton_21.setText(_translate("MainWindow", "виставлення зазорів"))
        self.radioButton_25.setText(_translate("MainWindow", "очікування зварка"))
        self.radioButton_24.setText(_translate("MainWindow", "очікування Komax"))
        self.radioButton_23.setText(_translate("MainWindow", "ТО зварки"))
        # self.radioButton_26.setText(_translate("MainWindow", "заблоковано"))
        self.label_5.setText(_translate("MainWindow", "status of run"))
        self.label_6.setText(_translate("MainWindow", "№ of applicator 8000:"))
        self.pushButton.setText(_translate("MainWindow", "ADD"))
        self.pushButton_2.setText(_translate("MainWindow", "create table per shift"))
        self.pushButton_3.setText(_translate("MainWindow", "show equipment history"))
        self.pushButton_4.setText(_translate("MainWindow", "manual correction"))
        self.pushButton_5.setText(_translate("MainWindow", "clean shift table"))
        self.pushButton_6.setText(_translate("MainWindow", "permission info"))

        self.message.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Calibri\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.minutes.setWhatsThis(_translate("MainWindow", "minutes"))
        self.minutes.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:24pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))

        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

        self.label_10.setText(_translate("MainWindow", "Mytsa Viktor. Ukraine Lviv"))

