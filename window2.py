# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(980, 406)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # input area

        self.label_8 = QtWidgets.QLabel(MainWindow)
        self.label_8.setGeometry(QtCore.QRect(30, 10, 251, 21))
        self.label_8.setObjectName("label_8")

        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(30, 120, 101, 16))
        self.label.setObjectName("label")
        self.cycles = QtWidgets.QTextEdit(self.centralwidget)
        self.cycles.setGeometry(QtCore.QRect(30, 140, 281, 41))
        self.cycles.setObjectName("cycles")
        self.label_1 = QtWidgets.QLabel(MainWindow)
        self.label_1.setGeometry(QtCore.QRect(30, 190, 101, 16))
        self.label_1.setObjectName("label_1")
        self.old_cycles = QtWidgets.QTextEdit(self.centralwidget)
        self.old_cycles.setGeometry(QtCore.QRect(30, 210, 281, 41))
        self.old_cycles.setObjectName("old_cycles")
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(340, 50, 101, 16))
        self.label_2.setObjectName("label_2")
        self.page = QtWidgets.QTextEdit(self.centralwidget)
        self.page.setGeometry(QtCore.QRect(340, 70, 61, 41))
        self.page.setObjectName("page")
        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(30, 50, 101, 16))
        self.label_3.setObjectName("label_3")
        self.applicator = QtWidgets.QTextEdit(self.centralwidget)
        self.applicator.setGeometry(QtCore.QRect(30, 70, 281, 41))
        self.applicator.setObjectName("applicator")
        self.label_6 = QtWidgets.QLabel(MainWindow)
        self.label_6.setGeometry(QtCore.QRect(30, 260, 101, 16))
        self.label_6.setObjectName("label_6")
        self.counter = QtWidgets.QTextEdit(self.centralwidget)
        self.counter.setGeometry(QtCore.QRect(30, 280, 281, 41))
        self.counter.setObjectName("counter")

        # output area

        self.label_9 = QtWidgets.QLabel(MainWindow)
        self.label_9.setGeometry(QtCore.QRect(610, 10, 251, 21))
        self.label_9.setObjectName("label_9")

        self.label_4 = QtWidgets.QLabel(MainWindow)
        self.label_4.setGeometry(QtCore.QRect(610, 50, 101, 16))
        self.label_4.setObjectName("label_4")
        self.total_cycles = QtWidgets.QTextBrowser(self.centralwidget)
        self.total_cycles.setGeometry(QtCore.QRect(610, 70, 261, 41))
        self.total_cycles.setObjectName("total_cycles")
        self.label_5 = QtWidgets.QLabel(MainWindow)
        self.label_5.setGeometry(QtCore.QRect(610, 190, 101, 16))
        self.label_5.setObjectName("label_5")
        self.next_page = QtWidgets.QTextBrowser(self.centralwidget)
        self.next_page.setGeometry(QtCore.QRect(610, 210, 61, 31))
        self.next_page.setObjectName("next_page")
        self.label_7 = QtWidgets.QLabel(MainWindow)
        self.label_7.setGeometry(QtCore.QRect(610, 120, 101, 16))
        self.label_7.setObjectName("label_7")
        self.correction = QtWidgets.QTextBrowser(self.centralwidget)
        self.correction.setGeometry(QtCore.QRect(610, 140, 261, 41))
        self.correction.setObjectName("correction")


        #  buttons

        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(30, 340, 281, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(780, 210, 100, 31))
        self.pushButton_2.setObjectName("pushButton")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MYTSA_CYCLES"))
        self.label.setText(_translate("MainWindow", "cycles"))
        self.label_1.setText(_translate("MainWindow", "old cycles"))
        self.label_2.setText(_translate("MainWindow", "page"))
        self.label_3.setText(_translate("MainWindow", "applicator"))
        self.label_4.setText(_translate("MainWindow", "total cycles"))
        self.label_5.setText(_translate("MainWindow", "next page"))
        self.label_6.setText(_translate("MainWindow", "counter"))
        self.label_7.setText(_translate("MainWindow", "correction"))
        self.label_8.setText(_translate("MainWindow", "INPUT DATA FROM APPLICATOR"))
        self.label_9.setText(_translate("MainWindow", "CHECK THIS DATA IN NEW CARD"))
        self.pushButton.setText(_translate("MainWindow", "CALCULATION"))
        self.pushButton_2.setText(_translate("MainWindow", "PRINT NEW CARD"))
