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
        self.label_1.setObjectName("per_number")
        self.per_number = QtWidgets.QTextEdit(self.centralwidget)
        self.per_number.setGeometry(QtCore.QRect(30, 70, 150, 25))
        self.per_number.setObjectName("per_number")

        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 150, 16))
        self.label_2.setObjectName("counter")
        self.per_number = QtWidgets.QTextEdit(self.centralwidget)
        self.per_number.setGeometry(QtCore.QRect(30, 120, 150, 25))
        self.per_number.setObjectName("counter")


        # output area

        self.label_10 = QtWidgets.QLabel(MainWindow)
        self.label_10.setGeometry(QtCore.QRect(610, 150, 150, 16))
        self.label_10.setObjectName("counter")
        self.counter = QtWidgets.QTextBrowser(self.centralwidget)
        self.counter.setGeometry(QtCore.QRect(560, 170, 150, 41))
        self.counter.setObjectName("counter")

        self.label_11 = QtWidgets.QLabel(MainWindow)
        self.label_11.setGeometry(QtCore.QRect(610, 200, 150, 16))
        self.label_11.setObjectName("")
        self. = QtWidgets.QTextBrowser(self.centralwidget)
        self..setGeometry(QtCore.QRect(560, 220, 150, 41))
        self..setObjectName("")


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
        self.label_1.setText(_translate("MainWindow", "personal number"))
        self.label_2.setText(_translate("MainWindow", "counter"))

        self.label_10.setText(_translate("MainWindow", "counter"))
        self.label_11.setText(_translate("MainWindow", ""))
        # self.label_12.setText(_translate("MainWindow", "Mytsa Viktor. Ukraine Lviv"))
        self.pushButton.setText(_translate("MainWindow", "напис на кнопці"))

