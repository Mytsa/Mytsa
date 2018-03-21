# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
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
        self.counter.setGeometry(QtCore.QRect(285, 25, 100, 25))
        self.counter.setObjectName("counter")

        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(118, 5, 150, 16))
        self.label_3.setObjectName("sap number of equipment")
        self.sap_eq = QtWidgets.QTextEdit(self.centralwidget)
        self.sap_eq.setGeometry(QtCore.QRect(140, 25, 80, 25))
        self.sap_eq.setObjectName("sap number of equipment")

        self.label_4 = QtWidgets.QLabel(MainWindow)
        self.label_4.setGeometry(QtCore.QRect(10, 55, 150, 16))
        self.label_4.setObjectName("опис дефекту:")
        self.defect = QtWidgets.QTextEdit(self.centralwidget)
        self.defect.setGeometry(QtCore.QRect(5, 75, 40, 25))
        self.defect.setObjectName("опис дефекту:")

        self.label_5 = QtWidgets.QLabel(MainWindow)
        self.label_5.setGeometry(QtCore.QRect(10, 450, 150, 16))
        self.label_5.setObjectName("Ймовірні причини дефекту:")
        self.fault = QtWidgets.QTextEdit(self.centralwidget)
        self.fault.setGeometry(QtCore.QRect(5, 470, 40, 25))
        self.fault.setObjectName("Ймовірні причини дефекту:")


        self.label_7 = QtWidgets.QLabel(MainWindow)
        self.label_7.setGeometry(QtCore.QRect(394, 210, 100, 40))
        self.label_7.setObjectName("spare_parts")
        self.sp1 = QtWidgets.QTextEdit(self.centralwidget)
        self.sp1.setGeometry(QtCore.QRect(390, 245, 110, 25))
        self.sp1.setObjectName("spare_parts")

        self.label_35 = QtWidgets.QLabel(MainWindow)
        self.label_35.setGeometry(QtCore.QRect(525, 225, 80, 16))
        self.label_35.setObjectName("pcs1")
        self.pcs1 = QtWidgets.QTextEdit(self.centralwidget)
        self.pcs1.setGeometry(QtCore.QRect(520, 245, 50, 25))
        self.pcs1.setObjectName("pcs1")

        self.label_9 = QtWidgets.QLabel(MainWindow)
        self.label_9.setGeometry(QtCore.QRect(394, 270, 150, 40))
        self.label_9.setObjectName("spare_parts2")
        self.sp3 = QtWidgets.QTextEdit(self.centralwidget)
        self.sp3.setGeometry(QtCore.QRect(390, 305, 110, 25))
        self.sp3.setObjectName("spare_parts2")

        self.label_37 = QtWidgets.QLabel(MainWindow)
        self.label_37.setGeometry(QtCore.QRect(525, 285, 80, 16))
        self.label_37.setObjectName("pcs2")
        self.pcs2 = QtWidgets.QTextEdit(self.centralwidget)
        self.pcs2.setGeometry(QtCore.QRect(520, 305, 50, 25))
        self.pcs2.setObjectName("pcs2")

        self.label_34 = QtWidgets.QLabel(MainWindow)
        self.label_34.setGeometry(QtCore.QRect(394, 330, 150, 40))
        self.label_34.setObjectName("spare_parts3")
        self.sp5 = QtWidgets.QTextEdit(self.centralwidget)
        self.sp5.setGeometry(QtCore.QRect(390, 365, 110, 25))
        self.sp5.setObjectName("spare_parts3")

        self.label_38 = QtWidgets.QLabel(MainWindow)
        self.label_38.setGeometry(QtCore.QRect(525, 340, 80, 16))
        self.label_38.setObjectName("pcs3")
        self.pcs3 = QtWidgets.QTextEdit(self.centralwidget)
        self.pcs3.setGeometry(QtCore.QRect(520, 365, 50, 25))
        self.pcs3.setObjectName("pcs3")

        self.label_36 = QtWidgets.QLabel(MainWindow)
        self.label_36.setGeometry(QtCore.QRect(394, 390, 150, 40))
        self.label_36.setObjectName("spare_parts4")
        self.sp7 = QtWidgets.QTextEdit(self.centralwidget)
        self.sp7.setGeometry(QtCore.QRect(390, 425, 110, 25))
        self.sp7.setObjectName("spare_parts4")

        self.label_39 = QtWidgets.QLabel(MainWindow)
        self.label_39.setGeometry(QtCore.QRect(525, 400, 80, 16))
        self.label_39.setObjectName("pcs4")
        self.pcs4 = QtWidgets.QTextEdit(self.centralwidget)
        self.pcs4.setGeometry(QtCore.QRect(520, 425, 50, 25))
        self.pcs4.setObjectName("pcs4")


        self.label_10 = QtWidgets.QLabel(MainWindow)
        self.label_10.setGeometry(QtCore.QRect(275, 140, 150, 16))
        self.label_10.setObjectName("spare part number")
        self.fp = QtWidgets.QTextEdit(self.centralwidget)
        self.fp.setGeometry(QtCore.QRect(270, 160, 140, 25))
        self.fp.setObjectName("spare part number")


        # output area

        self.label_8 = QtWidgets.QLabel(MainWindow)
        self.label_8.setGeometry(QtCore.QRect(570, 140, 150, 16))
        self.label_8.setObjectName("spare_parts1")
        self.sp4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.sp4.setGeometry(QtCore.QRect(535, 160, 190, 50))
        self.sp4.setObjectName("spare_parts1")


        self.label_11 = QtWidgets.QLabel(MainWindow)
        self.label_11.setGeometry(QtCore.QRect(600, 5, 150, 16))
        self.label_11.setObjectName("type_eq")
        self.type_eq = QtWidgets.QTextBrowser(self.centralwidget)
        self.type_eq.setGeometry(QtCore.QRect(575, 25, 150, 40))
        self.type_eq.setObjectName("type_eq")


        self.label_6 = QtWidgets.QLabel(MainWindow)
        self.label_6.setGeometry(QtCore.QRect(585, 70, 150, 16))
        self.label_6.setObjectName("counter_info")
        self.counter_info = QtWidgets.QTextBrowser(self.centralwidget)
        self.counter_info.setGeometry(QtCore.QRect(575, 90, 150, 25))
        self.counter_info.setObjectName("counter_info")

        self.label_12 = QtWidgets.QLabel(MainWindow)
        self.label_12.setGeometry(QtCore.QRect(460, 455, 150, 16))
        self.label_12.setObjectName("статус обробки")
        self.message = QtWidgets.QTextBrowser(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(400, 470, 250, 85))
        self.message.setObjectName("статус обробки")


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
        
        self.label_19 = QtWidgets.QLabel(MainWindow)
        self.label_19.setGeometry(QtCore.QRect(5, 200, 250, 20))
        self.label_19.setObjectName("Зазубрини в місті відрізу контакту")
        
        self.label_20 = QtWidgets.QLabel(MainWindow)
        self.label_20.setGeometry(QtCore.QRect(5, 220, 250, 20))
        self.label_20.setObjectName("Пошкодження проводу або ущільнення")
      
        self.label_21 = QtWidgets.QLabel(MainWindow)
        self.label_21.setGeometry(QtCore.QRect(5, 240, 250, 20))
        self.label_21.setObjectName("Рекваліфікація / EMPB")
        
        self.label_22 = QtWidgets.QLabel(MainWindow)
        self.label_22.setGeometry(QtCore.QRect(5, 420, 250, 20))
        self.label_22.setObjectName("Інше:")
        
        self.label_23 = QtWidgets.QLabel(MainWindow)
        self.label_23.setGeometry(QtCore.QRect(5, 260, 250, 20))
        self.label_23.setObjectName("Не вірна довжина проводу")

        self.label_24 = QtWidgets.QLabel(MainWindow)
        self.label_24.setGeometry(QtCore.QRect(5, 280, 250, 20))
        self.label_24.setObjectName("Не відповідне зварне з’єднання")
        
        self.label_25 = QtWidgets.QLabel(MainWindow)
        self.label_25.setGeometry(QtCore.QRect(5, 300, 300, 20))
        self.label_25.setObjectName("Не відповідна сила стягування кабельбіндера")
        
        self.label_26 = QtWidgets.QLabel(MainWindow)
        self.label_26.setGeometry(QtCore.QRect(5, 320, 250, 20))
        self.label_26.setObjectName("Не відповідне термоусадження")
        
        self.label_27 = QtWidgets.QLabel(MainWindow)
        self.label_27.setGeometry(QtCore.QRect(5, 340, 250, 20))
        self.label_27.setObjectName("Не відповідне скручення проводів")

        self.label_28 = QtWidgets.QLabel(MainWindow)
        self.label_28.setGeometry(QtCore.QRect(5, 360, 250, 20))
        self.label_28.setObjectName("Не відповідна обмотка з’єднання")

        self.label_29 = QtWidgets.QLabel(MainWindow)
        self.label_29.setGeometry(QtCore.QRect(5, 380, 250, 20))
        self.label_29.setObjectName("Тріснута запчастина")

        self.label_30 = QtWidgets.QLabel(MainWindow)
        self.label_30.setGeometry(QtCore.QRect(5, 400, 300, 20))
        self.label_30.setObjectName("Обладнання не вмикається / не продукує виріб")

        self.label_31 = QtWidgets.QLabel(MainWindow)
        self.label_31.setGeometry(QtCore.QRect(5, 490, 300, 20))
        self.label_31.setObjectName("Людський фактор")

        self.label_32 = QtWidgets.QLabel(MainWindow)
        self.label_32.setGeometry(QtCore.QRect(5, 530, 300, 20))
        self.label_32.setObjectName("Інше:")
        
        self.label_33 = QtWidgets.QLabel(MainWindow)
        self.label_33.setGeometry(QtCore.QRect(5, 510, 300, 20))
        self.label_33.setObjectName("Нормальне зношення / механічне зношення")

        # my info-block
        self.label_13 = QtWidgets.QLabel(MainWindow)
        self.label_13.setGeometry(QtCore.QRect(620, 555, 180, 20))
        self.label_13.setObjectName("label_12")

        #  buttons

        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(30, 555, 200, 41))
        self.pushButton.setObjectName("pushButton")

        self.pushButton1 = QtWidgets.QPushButton(MainWindow)
        self.pushButton1.setGeometry(QtCore.QRect(300, 555, 200, 41))
        self.pushButton1.setObjectName("pushButton1")

        self.pushButton2 = QtWidgets.QPushButton(MainWindow)
        self.pushButton2.setGeometry(QtCore.QRect(425, 140, 100, 41))
        self.pushButton2.setObjectName("pushButton2")

        # self.pushButton3 = QtWidgets.QPushButton(MainWindow)
        # self.pushButton3.setGeometry(QtCore.QRect(430, 25, 110, 27))
        # self.pushButton3.setObjectName("pushButton3")

        # self.pushButton4 = QtWidgets.QPushButton(MainWindow)
        # self.pushButton4.setGeometry(QtCore.QRect(412, 320, 100, 25))
        # self.pushButton4.setObjectName("pushButton4")
        #
        # self.pushButton5 = QtWidgets.QPushButton(MainWindow)
        # self.pushButton5.setGeometry(QtCore.QRect(412, 390, 100, 25))
        # self.pushButton5.setObjectName("pushButton5")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "repare report"))
        self.label_1.setText(_translate("MainWindow", "personal number"))
        self.label_2.setText(_translate("MainWindow", "counter"))
        self.label_3.setText(_translate("MainWindow", "SAP № of equipment 8000:"))
        self.label_4.setText(_translate("MainWindow", "опис дефекту:"))
        self.label_5.setText(_translate("MainWindow", "Ймовірні причини дефекту:"))
        self.label_6.setText(_translate("MainWindow", "останній запис лічильника"))
        self.label_7.setText(_translate("MainWindow", "SAP № of \nspare part1  40000:"))
        self.label_8.setText(_translate("MainWindow", "info about spare parts"))
        self.label_9.setText(_translate("MainWindow", "SAP № of \nspare part2  40000:"))
        self.label_10.setText(_translate("MainWindow", "spare part number 40000:"))
        self.label_34.setText(_translate("MainWindow", "SAP № of \nspare part3  40000:"))
        self.label_35.setText(_translate("MainWindow", "pieces"))
        self.label_36.setText(_translate("MainWindow", "SAP № of \nspare part4  40000:"))
        self.label_37.setText(_translate("MainWindow", "pieces"))
        self.label_38.setText(_translate("MainWindow", "pieces"))
        self.label_39.setText(_translate("MainWindow", "pieces"))



        self.label_11.setText(_translate("MainWindow", "type of equipment"))
        self.label_12.setText(_translate("MainWindow", "<--- статус обробки --->"))
        self.label_13.setText(_translate("MainWindow", "Mytsa Viktor. Ukraine Lviv"))


        self.label_14.setText(_translate("MainWindow", "1: Пошкодження поверхні контакту"))
        self.label_15.setText(_translate("MainWindow", "2: Гострини на розрізі контакту"))
        self.label_16.setText(_translate("MainWindow", "3: Не симетричне / не відповідне закриття ядра"))
        self.label_17.setText(_translate("MainWindow", "4: Пошкодження контакту або його деформація"))
        self.label_18.setText(_translate("MainWindow", "5: Асиметрія контакту"))
        self.label_19.setText(_translate("MainWindow", "6: Зазубрини в місті відрізу контакту"))
        self.label_20.setText(_translate("MainWindow", "7: Пошкодження проводу або ущільнення"))
        self.label_21.setText(_translate("MainWindow", "8: Рекваліфікація / EMPB"))
        self.label_22.setText(_translate("MainWindow", "17: Інше:    ---> записати в карті"))
        self.label_23.setText(_translate("MainWindow", "9: Не вірна довжина проводу"))
        self.label_24.setText(_translate("MainWindow", "10: Не відповідне зварне з’єднання"))
        self.label_25.setText(_translate("MainWindow", "11: Не відповідна сила стягування кабельбіндера"))
        self.label_26.setText(_translate("MainWindow", "12: Не відповідне термоусадження"))
        self.label_27.setText(_translate("MainWindow", "13: Не відповідне скручення проводів"))        
        self.label_28.setText(_translate("MainWindow", "14: Не відповідна обмотка з’єднання"))
        self.label_29.setText(_translate("MainWindow", "15: Тріснута запчастина"))
        self.label_30.setText(_translate("MainWindow", "16: Обладнання не вмикається / не продукує виріб"))

        self.label_31.setText(_translate("MainWindow", "1: Людський фактор"))
        self.label_32.setText(_translate("MainWindow", "3: Інше:    ---> записати в карті"))
        self.label_33.setText(_translate("MainWindow", "2: Нормальне зношення / механічне зношення"))        


        self.pushButton.setText(_translate("MainWindow", "write data to file"))
        self.pushButton1.setText(_translate("MainWindow", "print 1 card of message"))
        self.pushButton2.setText(_translate("MainWindow", "find spare part"))
        #self.pushButton3.setText(_translate("MainWindow", "find equipment"))
        # self.pushButton4.setText(_translate("MainWindow", "find spare part3"))
        # self.pushButton5.setText(_translate("MainWindow", "find spare part4"))

