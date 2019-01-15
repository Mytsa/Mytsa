﻿# -*- coding: utf-8 -*-
import sys
import os
from openpyxl import *
from datetime import datetime
from gui import *    # gui is interface file
from f_w_r import *    # def for files are write and read
from filter import *    # filter to personal number, applicator list

from PyQt5 import QtCore, QtGui, QtWidgets


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.date = datetime.strftime(datetime.now(), "%d/%m/%Y")
        self.time = datetime.strftime(datetime.now(), "%H:%M")
        self.w_date = datetime.strftime(datetime.now(), "%W")
        self.m_date = datetime.strftime(datetime.now(), "%m")

        # Здесь прописываем событие нажатия на кнопку
        self.ui.pushButton.clicked.connect(self.Add)
        self.ui.pushButton_2.clicked.connect(self.CreateTable)
        self.ui.pushButton_3.clicked.connect(self.HistoryEquipment)
        self.ui.pushButton_4.clicked.connect(self.ManualCorrection)
        self.ui.pushButton_5.clicked.connect(self.Clean_data_shift)
        self.ui.pushButton_6.clicked.connect(self.Contact_info)

        self.ui.radioButton_1.clicked.connect(self.Radio1)
        self.ui.radioButton_2.clicked.connect(self.Radio2)
        self.ui.radioButton_3.clicked.connect(self.Radio3)
        self.ui.radioButton_4.clicked.connect(self.Radio4)
        self.ui.radioButton_5.clicked.connect(self.Radio5)
        self.ui.radioButton_6.clicked.connect(self.Radio6)
        self.ui.radioButton_7.clicked.connect(self.Radio7)
        self.ui.radioButton_8.clicked.connect(self.Radio8)
        self.ui.radioButton_9.clicked.connect(self.Radio9)
        self.ui.radioButton_10.clicked.connect(self.Radio10)
        self.ui.radioButton_11.clicked.connect(self.Radio11)
        self.ui.radioButton_12.clicked.connect(self.Radio12)
        self.ui.radioButton_13.clicked.connect(self.Radio13)

        self.ui.radioButton_15.clicked.connect(self.Radio15)

        self.ui.radioButton_19.clicked.connect(self.Radio19)
        self.ui.radioButton_18.clicked.connect(self.Radio18)
        self.ui.radioButton_17.clicked.connect(self.Radio17)
        self.ui.radioButton_22.clicked.connect(self.Radio22)
        self.ui.radioButton_20.clicked.connect(self.Radio20)
        self.ui.radioButton_21.clicked.connect(self.Radio21)
        self.ui.radioButton_25.clicked.connect(self.Radio25)
        self.ui.radioButton_24.clicked.connect(self.Radio24)
        self.ui.radioButton_23.clicked.connect(self.Radio23)
        # self.ui.radioButton_26.clicked.connect(self.Radio26)


    def Add(self):

        eq_num = self.ui.eq_number.toPlainText()  # input equipment number
        eq_number = '8000' + str(eq_num)    # add const in beginner of figures 8000....
        per_number = self.ui.per_number.toPlainText()  # input personal number
        minutes = self.ui.minutes.toPlainText()  # input minutes
        notice = self.ui.notice.toPlainText()  # input notice
        apl = self.ui.apl.toPlainText()  # input № of applicator

        shift = shift_id(per_number)
        if shift:
            type_fix = data_from_write_type()    # sent data of type fix
            if type_fix:
                apl_check = check_apl(apl)
                apl_type_fix_massiv = ('механічне налаштування', 'заміна запчастин', 'налаштування симетричності розрізу')
                if minutes.isdigit():
                    apl_checked = True
                    if type_fix in apl_type_fix_massiv:
                        if apl_check:
                            write_apl_data(apl, self.date, per_number, type_fix, notice)
                        if type_fix in apl_type_fix_massiv and not apl_check:
                            apl_checked = False
                    else:
                        apl = ''
                    shift_write = write_sum_and_shift_files(eq_number, type_fix, minutes)  # 1 sec
                    if shift_write and apl_checked:
                        write_log_file(self.date, shift, eq_number, apl, minutes, type_fix, notice)  # write data to Log file - 1 sec
                        write_data = write_eq_file(eq_number, self.date, per_number, type_fix, notice)
                        type_clear = ''
                        write_type(type_clear)

                        if write_data:
                            self.ui.message.setText(str('done') + '\n' + str(type_fix))  # output message/status of run
                    else:
                        self.ui.message.setText('check equipment file or equipment number and applicator number')
                else:
                    self.ui.message.setText('write correct time')
            else:
                self.ui.message.setText('choice type of Down Time')
        else:
            self.ui.message.setText('write correct personal number')


    def Radio1(self):
        mess = 'проблеми з матеріалом'
        write_type(mess)

    def Radio2(self):
        mess = 'механічна поломка'
        write_type(mess)

    def Radio3(self):
        mess = 'електрична поломка'
        write_type(mess)

    def Radio4(self):
        mess = 'СPU 2000'
        write_type(mess)

    def Radio5(self):
        mess = 'scaner'
        write_type(mess)

    def Radio6(self):
        mess = 'інший тип простою'
        write_type(mess)

    def Radio7(self):
        mess = 'налаштування принтера'
        write_type(mess)

    def Radio8(self):
        mess = 'налаштування втулочного модуля'
        write_type(mess)

    def Radio25(self):
        mess = 'очікування зварка'
        write_type(mess)

    def Radio10(self):
        mess = 'ТО обладнання'
        write_type(mess)

    def Radio11(self):
        mess = 'механічне налаштування'
        write_type(mess)

    def Radio12(self):
        mess = 'налаштування симетричності розрізу'
        write_type(mess)

    def Radio13(self):
        mess = 'заміна запчастин'
        write_type(mess)

    def Radio15(self):
        mess = 'ТО аплікатора'
        write_type(mess)

    def Radio17(self):
        mess = 'Збій програми'
        write_type(mess)

    def Radio18(self):
        mess = 'новий проект/нові параметри'
        write_type(mess)

    def Radio19(self):
        mess = 'заміна електродів'
        write_type(mess)

    def Radio20(self):
        mess = 'чистка обладнання'
        write_type(mess)

    def Radio21(self):
        mess = 'ремонт електродів / зазор'
        write_type(mess)

    def Radio22(self):
        mess = 'проблеми з матеріалом на зварці'
        write_type(mess)

    def Radio23(self):
        mess = 'ТО зварки'
        write_type(mess)

    def Radio24(self):
        mess = 'очікування тех.відділу'
        write_type(mess)

    def Radio9(self):
        mess = 'ПЗ'
        write_type(mess)

    # def Radio26(self):
    #     mess = 'заміна електродів'
    #     write_type(mess)

    def CreateTable(self):    # open table for shift
        os.startfile('files\DownTime_shift.xlsx', "open")  # write correct address, file name
        write_sum_by_weeks(self.w_date)  # 6 sec
        self.ui.message.setText('table is create')  # output message/status of run

    def HistoryEquipment(self):    # open equipment file for history run
        eq_number = self.ui.eq_number.toPlainText()  # input equipment number
        name = '8000' + str(eq_number)
        if eq_number.isdigit() or len(eq_number) != 4 or False:
            self.ui.message.setText('write correct equipment number')
        os.startfile('files\eq_files\{}.xlsx'.format(name), "open")  # write correct address, file name

    def ManualCorrection(self):    # open table correction
        os.startfile('files\log.xlsx', "open")  # write correct address, file name

    def Clean_data_shift(self):
        sheet = 'main'
        clean_sum_by_weeks(sheet)
        self.ui.message.setText('clean shift table')

    def Contact_info(self):
        self.ui.message.setText(str('use only with permission') + '\n' + str('contact info') + '\n' + str('e-mail: Viktor.Mytsa@gmail.com'))


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
