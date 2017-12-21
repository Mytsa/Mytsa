# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # input area

        self.label_1 = QtWidgets.QLabel(MainWindow)
        self.label_1.setGeometry(QtCore.QRect(30, 55, 150, 16))
        self.label_1.setObjectName("s_part")
        self.s_part = QtWidgets.QTextEdit(self.centralwidget)
        self.s_part.setGeometry(QtCore.QRect(30, 70, 150, 25))
        self.s_part.setObjectName("s_part")


        # output area

        self.label_9 = QtWidgets.QLabel(MainWindow)
        self.label_9.setGeometry(QtCore.QRect(610, 150, 150, 16))
        self.label_9.setObjectName("pay")
        self.pay = QtWidgets.QTextBrowser(self.centralwidget)
        self.pay.setGeometry(QtCore.QRect(560, 170, 150, 41))
        self.pay.setObjectName("pay")


        # my info-block
        # self.label_12 = QtWidgets.QLabel(MainWindow)
        # self.label_12.setGeometry(QtCore.QRect(10, 10, 180, 20))
        # self.label_12.setObjectName("label_12")

        #  buttons

        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(30, 300, 300, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "repare"))
        self.label_1.setText(_translate("MainWindow", "search spare part"))

        self.label_9.setText(_translate("MainWindow", "виплата"))
        # self.label_12.setText(_translate("MainWindow", "Mytsa Viktor. Ukraine Lviv"))
        self.pushButton.setText(_translate("MainWindow", "напис на кнопці"))

