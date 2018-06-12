# -*- coding: utf-8 -*-
import sys
import os
from openpyxl import *
import subprocess
from datetime import datetime
from gui import *    # gui is interface file
from f_w_r import *
from filter import *



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


    def Add(self):
        eq_number = self.ui.eq_number.toPlainText()  # input equipment number
        eq_number = '8000' + str(eq_number)    # add const in beginner of figures 8000....
        per_number = self.ui.per_number.toPlainText()  # input personal number

        minutes = self.ui.minutes.toPlainText()  # input minutes
        notice = self.ui.notice.toPlainText()  # input notice
        apl = self.ui.apl.toPlainText()  # input № of machine for applicator
        # print(eq_number + str(' eq_num') + per_number + str(' per num'), notice + str(' commet'), minutes + str(' minutes'))

        shift = shift_id(per_number)    # return name of shift by person number fo rwrite data in Log file
        write_log_file(date, shift, eq_number, apl, minutes, data, notice)    # write data to Log file


        name = eq_number
        sheet = 's_p'
        mark = '**'
        mes = str(find_row(name, sheet, mark))
        # print(mes)
        self.ui.message.setText(mes)  # output message/status of run
        # print(message)





    def CreateTable(self):    # open table for shift
        os.startfile('files\DownTime_shift.xlsx', "open")  # write correct address, file name

    def HistoryEquipment(self):    # open equipment file for history run
        eq_number = self.ui.eq_number.toPlainText()  # input equipment number
        name = '8000' + str(eq_number)
        if eq_number == '':
            self.ui.message.setText('write correct equipment number')
        else:
            os.startfile('files\eq_files\{}.xlsx'.format(name), "open")  # write correct address, file name


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
