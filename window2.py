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
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(10, 0, 141, 41))
        self.label.setObjectName("label")
        self.cycles = QtWidgets.QTextEdit(self.centralwidget)
        self.cycles.setGeometry(QtCore.QRect(10, 30, 141, 41))
        self.cycles.setObjectName("cycles")
        self.label_1 = QtWidgets.QLabel(MainWindow)
        self.label_1.setGeometry(QtCore.QRect(10, 60, 141, 41))
        self.label_1.setObjectName("label_1")
        self.old_cycles = QtWidgets.QTextEdit(self.centralwidget)
        self.old_cycles.setGeometry(QtCore.QRect(10, 90, 141, 41))
        self.old_cycles.setObjectName("old_cycles")
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 141, 41))
        self.label_2.setObjectName("label_2")
        self.page = QtWidgets.QTextEdit(self.centralwidget)
        self.page.setGeometry(QtCore.QRect(10, 150, 141, 41))
        self.page.setObjectName("page")
        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(10, 180, 141, 41))
        self.label_3.setObjectName("label_3")
        self.applicator = QtWidgets.QTextEdit(self.centralwidget)
        self.applicator.setGeometry(QtCore.QRect(10, 210, 141, 41))
        self.applicator.setObjectName("applicator")
        # self.label_6 = QtWidgets.QLabel(MainWindow)
        # self.label_6.setGeometry(QtCore.QRect(10, 240, 141, 41))
        # self.label_6.setObjectName("label_6")
        # self.counter = QtWidgets.QTextEdit(self.centralwidget)
        # self.counter.setGeometry(QtCore.QRect(10, 270, 141, 41))
        # self.counter.setObjectName("counter")


        self.label_4 = QtWidgets.QLabel(MainWindow)
        self.label_4.setGeometry(QtCore.QRect(380, 0, 150, 50))
        self.label_4.setObjectName("label_4")
        self.total_cycles = QtWidgets.QTextBrowser(self.centralwidget)
        self.total_cycles.setGeometry(QtCore.QRect(380, 40, 150, 50))
        self.total_cycles.setObjectName("total_cycles")
        self.label_5 = QtWidgets.QLabel(MainWindow)
        self.label_5.setGeometry(QtCore.QRect(380, 110, 150, 50))
        self.label_5.setObjectName("label_5")
        self.next_page = QtWidgets.QTextBrowser(self.centralwidget)
        self.next_page.setGeometry(QtCore.QRect(380, 150, 150, 50))
        self.next_page.setObjectName("next_page")
        # self.label_7 = QtWidgets.QLabel(MainWindow)
        # self.label_7.setGeometry(QtCore.QRect(380, 180, 150, 50))
        # self.label_7.setObjectName("label_7")
        # self.correction = QtWidgets.QTextBrowser(self.centralwidget)
        # self.correction.setGeometry(QtCore.QRect(380, 210, 150, 50))
        # self.correction.setObjectName("correction")


        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(70, 300, 100, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 300, 100, 30))
        self.pushButton_2.setObjectName("pushButton")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "cycles"))
        self.label_1.setText(_translate("MainWindow", "old cycles"))
        self.label_2.setText(_translate("MainWindow", "page"))
        self.label_3.setText(_translate("MainWindow", "applicator"))
        self.label_4.setText(_translate("MainWindow", "total cycles"))
        self.label_5.setText(_translate("MainWindow", "next page"))
#        self.label_6.setText(_translate("MainWindow", "counter"))
#        self.label_7.setText(_translate("MainWindow", "correction"))
        self.pushButton.setText(_translate("MainWindow", "calculation"))
        self.pushButton_2.setText(_translate("MainWindow", "print new card"))

