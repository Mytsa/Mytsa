# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # input area

        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(30, 55, 150, 16))
        self.label_3.setObjectName("salary")
        self.salary = QtWidgets.QTextEdit(self.centralwidget)
        self.salary.setGeometry(QtCore.QRect(30, 70, 150, 25))
        self.salary.setObjectName("salary")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(30, 105, 150, 16))
        self.label.setObjectName("hours")
        self.hours = QtWidgets.QTextEdit(self.centralwidget)
        self.hours.setGeometry(QtCore.QRect(30, 120, 150, 25))
        self.hours.setObjectName("hours")
        self.label_11 = QtWidgets.QLabel(MainWindow)
        self.label_11.setGeometry(QtCore.QRect(200, 105, 150, 16))
        self.label_11.setObjectName("w_hours")
        self.w_hours = QtWidgets.QTextEdit(self.centralwidget)
        self.w_hours.setGeometry(QtCore.QRect(200, 120, 150, 25))
        self.w_hours.setObjectName("w_hours")
        self.label_1 = QtWidgets.QLabel(MainWindow)
        self.label_1.setGeometry(QtCore.QRect(30, 155, 150, 16))
        self.label_1.setObjectName("bonus_present")
        self.bonus_present = QtWidgets.QTextEdit(self.centralwidget)
        self.bonus_present.setGeometry(QtCore.QRect(30, 170, 150, 25))
        self.bonus_present.setObjectName("bonus_present")
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(200, 55, 150, 16))
        self.label_2.setObjectName("proc")
        self.proc = QtWidgets.QTextEdit(self.centralwidget)
        self.proc.setGeometry(QtCore.QRect(200, 70, 150, 25))
        self.proc.setObjectName("proc")
        self.label_6 = QtWidgets.QLabel(MainWindow)
        self.label_6.setGeometry(QtCore.QRect(200, 155, 150, 16))
        self.label_6.setObjectName("bonus")
        self.bonus = QtWidgets.QTextEdit(self.centralwidget)
        self.bonus.setGeometry(QtCore.QRect(200, 170, 150, 25))
        self.bonus.setObjectName("bonus")

        self.label_4 = QtWidgets.QLabel(MainWindow)
        self.label_4.setGeometry(QtCore.QRect(30, 205, 150, 16))
        self.label_4.setObjectName("overtime")
        self.overtime = QtWidgets.QTextEdit(self.centralwidget)
        self.overtime.setGeometry(QtCore.QRect(30, 220, 150, 25))
        self.overtime.setObjectName("overtime")
        self.label_7 = QtWidgets.QLabel(MainWindow)
        self.label_7.setGeometry(QtCore.QRect(200, 205, 150, 16))
        self.label_7.setObjectName("bonus_overtime")
        self.bonus_overtime = QtWidgets.QTextEdit(self.centralwidget)
        self.bonus_overtime.setGeometry(QtCore.QRect(200, 220, 150, 25))
        self.bonus_overtime.setObjectName("bonus_overtime")

        # output area

        self.label_9 = QtWidgets.QLabel(MainWindow)
        self.label_9.setGeometry(QtCore.QRect(610, 150, 150, 16))
        self.label_9.setObjectName("pay")
        self.pay = QtWidgets.QTextBrowser(self.centralwidget)
        self.pay.setGeometry(QtCore.QRect(560, 170, 150, 41))
        self.pay.setObjectName("pay")

        self.label_5 = QtWidgets.QLabel(MainWindow)
        self.label_5.setGeometry(QtCore.QRect(610, 250, 150, 16))
        self.label_5.setObjectName("month_pay")
        self.month_pay = QtWidgets.QTextBrowser(self.centralwidget)
        self.month_pay.setGeometry(QtCore.QRect(560, 270, 150, 41))
        self.month_pay.setObjectName("month_pay")

        self.label_10 = QtWidgets.QLabel(MainWindow)
        self.label_10.setGeometry(QtCore.QRect(610, 50, 150, 16))
        self.label_10.setObjectName("avans")
        self.avans = QtWidgets.QTextBrowser(self.centralwidget)
        self.avans.setGeometry(QtCore.QRect(560, 70, 150, 41))
        self.avans.setObjectName("avans")

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
        MainWindow.setWindowTitle(_translate("MainWindow", "salary calculation"))
        self.label.setText(_translate("MainWindow", "робочих годин в місяці"))
        self.label_1.setText(_translate("MainWindow", "премія за присутність"))
        self.label_2.setText(_translate("MainWindow", "% до ставки"))
        self.label_3.setText(_translate("MainWindow", "ставка"))
        self.label_4.setText(_translate("MainWindow", "понаднормові години"))
        self.label_5.setText(_translate("MainWindow", "з/п за місяць"))
        self.label_6.setText(_translate("MainWindow", "додаткова премія"))
        self.label_7.setText(_translate("MainWindow", "премія за понад нормові години"))

        self.label_9.setText(_translate("MainWindow", "виплата"))
        self.label_10.setText(_translate("MainWindow", "виплата авансу"))
        self.label_11.setText(_translate("MainWindow", "відпрацьовано місячних годин"))
        # self.label_12.setText(_translate("MainWindow", "Mytsa Viktor. Ukraine Lviv"))
        self.pushButton.setText(_translate("MainWindow", "рахуй !"))

