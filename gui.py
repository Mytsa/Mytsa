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

        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 150, 16))
        self.label_3.setObjectName("sap number of equipment")
        self.sap_eq = QtWidgets.QTextEdit(self.centralwidget)
        self.sap_eq.setGeometry(QtCore.QRect(30, 170, 150, 25))
        self.sap_eq.setObjectName("sap number of equipment")

        self.label_4 = QtWidgets.QLabel(MainWindow)
        self.label_4.setGeometry(QtCore.QRect(30, 190, 150, 16))
        self.label_4.setObjectName("defect")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(70, 210, 82, 17))
        self.radioButton.setObjectName("radioButton")


        self.label_5 = QtWidgets.QLabel(MainWindow)
        self.label_5.setGeometry(QtCore.QRect(30, 250, 150, 16))
        self.label_5.setObjectName("fault")
        self.fault = QtWidgets.QTextEdit(self.centralwidget)
        self.fault.setGeometry(QtCore.QRect(30, 270, 150, 25))
        self.fault.setObjectName("fault")

        # output area

        self.label_10 = QtWidgets.QLabel(MainWindow)
        self.label_10.setGeometry(QtCore.QRect(610, 150, 150, 16))
        self.label_10.setObjectName("counter")
        self.counter = QtWidgets.QTextBrowser(self.centralwidget)
        self.counter.setGeometry(QtCore.QRect(560, 170, 150, 41))
        self.counter.setObjectName("counter")

        # self.label_11 = QtWidgets.QLabel(MainWindow)
        # self.label_11.setGeometry(QtCore.QRect(610, 200, 150, 16))
        # self.label_11.setObjectName("")
        # self. = QtWidgets.QTextBrowser(self.centralwidget)
        # self..setGeometry(QtCore.QRect(560, 220, 150, 41))
        # self..setObjectName("")


        # my info-block
        # self.label_12 = QtWidgets.QLabel(MainWindow)
        # self.label_12.setGeometry(QtCore.QRect(10, 10, 180, 20))
        # self.label_12.setObjectName("label_12")

        #  buttons

        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(30, 300, 200, 41))
        self.pushButton.setObjectName("pushButton")

        self.pushButton1 = QtWidgets.QPushButton(MainWindow)
        self.pushButton1.setGeometry(QtCore.QRect(300, 300, 200, 41))
        self.pushButton1.setObjectName("pushButton1")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "repare"))
        self.label_1.setText(_translate("MainWindow", "personal number"))
        self.label_2.setText(_translate("MainWindow", "counter"))
        self.label_3.setText(_translate("MainWindow", "sap number of equipment"))
        self.label_4.setText(_translate("MainWindow", "defect"))
        self.label_5.setText(_translate("MainWindow", "fault"))

        self.label_10.setText(_translate("MainWindow", "counter"))
        # self.label_11.setText(_translate("MainWindow", ""))
        # self.label_12.setText(_translate("MainWindow", "Mytsa Viktor. Ukraine Lviv"))
        self.pushButton.setText(_translate("MainWindow", "write data to file"))
        self.pushButton1.setText(_translate("MainWindow", "print 1 card of message"))

