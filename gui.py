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
        self.label_1.setGeometry(QtCore.QRect(5, 5, 80, 16))
        self.label_1.setObjectName("per_number")
        self.per_number = QtWidgets.QTextEdit(self.centralwidget)
        self.per_number.setGeometry(QtCore.QRect(5, 25, 80, 25))
        self.per_number.setObjectName("per_number")

        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(305, 5, 150, 16))
        self.label_2.setObjectName("counter")
        self.counter = QtWidgets.QTextEdit(self.centralwidget)
        self.counter.setGeometry(QtCore.QRect(300, 25, 150, 25))
        self.counter.setObjectName("counter")

        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(118, 5, 150, 16))
        self.label_3.setObjectName("sap number of equipment")
        self.sap_eq = QtWidgets.QTextEdit(self.centralwidget)
        self.sap_eq.setGeometry(QtCore.QRect(140, 25, 80, 25))
        self.sap_eq.setObjectName("sap number of equipment")

        self.label_4 = QtWidgets.QLabel(MainWindow)
        self.label_4.setGeometry(QtCore.QRect(10, 55, 40, 16))
        self.label_4.setObjectName("defect")
        self.defect = QtWidgets.QTextEdit(self.centralwidget)
        self.defect.setGeometry(QtCore.QRect(5, 75, 40, 25))
        self.defect.setObjectName("defect")

        self.label_5 = QtWidgets.QLabel(MainWindow)
        self.label_5.setGeometry(QtCore.QRect(10, 205, 150, 16))
        self.label_5.setObjectName("fault")
        self.fault = QtWidgets.QTextEdit(self.centralwidget)
        self.fault.setGeometry(QtCore.QRect(5, 225, 150, 25))
        self.fault.setObjectName("fault")

        # self.label_6 = QtWidgets.QLabel(MainWindow)
        # self.label_6.setGeometry(QtCore.QRect(10, 255, 150, 16))
        # self.label_6.setObjectName("")
        # self. = QtWidgets.QTextEdit(self.centralwidget)
        # self..setGeometry(QtCore.QRect(5, 275, 150, 25))
        # self..setObjectName("")


        # self.label_7 = QtWidgets.QLabel(MainWindow)
        # self.label_7.setGeometry(QtCore.QRect(305, 70, 150, 16))
        # self.label_7.setObjectName("spare_parts")
        # self.sp1 = QtWidgets.QTextEdit(self.centralwidget)
        # self.sp1.setGeometry(QtCore.QRect(300, 90, 150, 25))
        # self.sp1.setObjectName("spare_parts")
        #
        # self.label_8 = QtWidgets.QLabel(MainWindow)
        # self.label_8.setGeometry(QtCore.QRect(305, 120, 150, 16))
        # self.label_8.setObjectName("spare_parts1")
        # self.sp2 = QtWidgets.QTextEdit(self.centralwidget)
        # self.sp2.setGeometry(QtCore.QRect(300, 140, 150, 25))
        # self.sp2.setObjectName("spare_parts1")
        #
        # self.label_9 = QtWidgets.QLabel(MainWindow)
        # self.label_9.setGeometry(QtCore.QRect(305, 170, 150, 16))
        # self.label_9.setObjectName("spare_parts2")
        # self.sp3 = QtWidgets.QTextEdit(self.centralwidget)
        # self.sp3.setGeometry(QtCore.QRect(300, 190, 150, 25))
        # self.sp3.setObjectName("spare_parts2")
        #
        # self.label_10 = QtWidgets.QLabel(MainWindow)
        # self.label_10.setGeometry(QtCore.QRect(305, 220, 150, 16))
        # self.label_10.setObjectName("spare_parts3")
        # self.sp4 = QtWidgets.QTextEdit(self.centralwidget)
        # self.sp4.setGeometry(QtCore.QRect(300, 240, 150, 25))
        # self.sp4.setObjectName("spare_parts3")

        # output area

        self.label_11 = QtWidgets.QLabel(MainWindow)
        self.label_11.setGeometry(QtCore.QRect(10, 255, 150, 16))
        self.label_11.setObjectName("type_eq")
        self.type_eq = QtWidgets.QTextBrowser(self.centralwidget)
        self.type_eq.setGeometry(QtCore.QRect(5, 275, 150, 25))
        self.type_eq.setObjectName("type_eq")

        # self.label_12 = QtWidgets.QLabel(MainWindow)
        # self.label_12.setGeometry(QtCore.QRect(610, 200, 150, 16))
        # self.label_12.setObjectName("")
        # self. = QtWidgets.QTextBrowser(self.centralwidget)
        # self..setGeometry(QtCore.QRect(560, 220, 150, 41))
        # self..setObjectName("")

        # defect block
        self.label_14 = QtWidgets.QLabel(MainWindow)
        self.label_14.setGeometry(QtCore.QRect(5, 100, 250, 20))
        self.label_14.setObjectName("Пошкодження поверхні контакту")

        self.label_15 = QtWidgets.QLabel(MainWindow)
        self.label_15.setGeometry(QtCore.QRect(5, 120, 250, 20))
        self.label_15.setObjectName("Гострини на розрізі контакту")

        self.label_16 = QtWidgets.QLabel(MainWindow)
        self.label_16.setGeometry(QtCore.QRect(5, 140, 250, 20))
        self.label_16.setObjectName("Не симетричне / не відповідне закриття ядра")

        self.label_17 = QtWidgets.QLabel(MainWindow)
        self.label_17.setGeometry(QtCore.QRect(5, 160, 250, 20))
        self.label_17.setObjectName("Пошкодження контакту або його деформація")

        self.label_18 = QtWidgets.QLabel(MainWindow)
        self.label_18.setGeometry(QtCore.QRect(5, 180, 250, 20))
        self.label_18.setObjectName("Асиметрія контакту")


        # my info-block
        self.label_13 = QtWidgets.QLabel(MainWindow)
        self.label_13.setGeometry(QtCore.QRect(620, 305, 180, 20))
        self.label_13.setObjectName("label_12")

        #  buttons

        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(30, 305, 200, 41))
        self.pushButton.setObjectName("pushButton")

        self.pushButton1 = QtWidgets.QPushButton(MainWindow)
        self.pushButton1.setGeometry(QtCore.QRect(300, 305, 200, 41))
        self.pushButton1.setObjectName("pushButton1")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "repare report"))
        self.label_1.setText(_translate("MainWindow", "personal number"))
        self.label_2.setText(_translate("MainWindow", "counter"))
        self.label_3.setText(_translate("MainWindow", "sap № of equipment 8000: "))
        self.label_4.setText(_translate("MainWindow", "defect"))
        self.label_5.setText(_translate("MainWindow", "fault"))
        # self.label_6.setText(_translate("MainWindow", ""))
        # self.label_7.setText(_translate("MainWindow", "SAP № of spare parts 1"))
        # self.label_8.setText(_translate("MainWindow", "SAP № of spare parts 2"))
        # self.label_9.setText(_translate("MainWindow", "SAP № of spare parts 3"))
        # self.label_10.setText(_translate("MainWindow", "SAP № of spare parts 4"))

        self.label_11.setText(_translate("MainWindow", "type of equipment"))
        # self.label_12.setText(_translate("MainWindow", ""))
        self.label_13.setText(_translate("MainWindow", "Mytsa Viktor. Ukraine Lviv"))


        self.label_14.setText(_translate("MainWindow", "1: Пошкодження поверхні контакту"))
        self.label_15.setText(_translate("MainWindow", "2: Гострини на розрізі контакту"))
        self.label_16.setText(_translate("MainWindow", "3: Не симетричне / не відповідне закриття ядра"))
        self.label_17.setText(_translate("MainWindow", "4: Пошкодження контакту або його деформація"))
        self.label_18.setText(_translate("MainWindow", "5: Асиметрія контакту"))


        self.pushButton.setText(_translate("MainWindow", "write data to file"))
        self.pushButton1.setText(_translate("MainWindow", "print 1 card of message"))

