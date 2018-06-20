# -*- coding: utf-8 -*-
import sys
import os
from openpyxl import *
from datetime import datetime
from gui import *    # gui is interface file
from f_w_r import *    # def for files are write and read
from filter import *    # filter to personal number - need decision!!!



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
        eq_num = self.ui.eq_number.toPlainText()  # input equipment number
        eq_number = '8000' + str(eq_num)    # add const in beginner of figures 8000....
        per_number = self.ui.per_number.toPlainText()  # input personal number
        minutes = self.ui.minutes.toPlainText()  # input minutes
        notice = self.ui.notice.toPlainText()  # input notice
        apl = self.ui.apl.toPlainText()  # input № of applicator


        b = len(eq_num)
        if eq_num.isdigit() is (False or b != 4):
            self.ui.message.setText('write correct equipment number')

        else:
            b = len(per_number)
            if per_number.isdigit() is (False or b != 4):
                self.ui.message.setText('write correct personal number')

            else:
# <! -------------- problem with 3 figures is write to log file
                b = len(apl)
                if apl != '':
                    apl = '8000' + str(apl)
                elif b != 4:
                    self.ui.message.setText('write correct applicator number')

                else:
                    pass
# --------------------------!>
                type_fix = '11'    # add choice of reason DownTime


                shift = shift_id(per_number)    # return name of shift by person number fo write data in Log file

                write_log_file(self.date, shift, eq_number, apl, minutes, type_fix, notice)  # write data to Log file - 1 sec

                write_eq_file(eq_number, self.date, per_number, type_fix)    # write data to equipment file   - 2 sec

                write_sum_and_shift_files(eq_number, type_fix, minutes)    # 1 sec

                write_sum_by_weeks(eq_number, self.w_date, type_fix, minutes)    # 6 sec

                #    sum of run is fucking 7 seconds
                mes = 'done'


                self.ui.message.setText(mes)  # output message/status of run


    def CreateTable(self):    # open table for shift
        os.startfile('files\DownTime_shift.xlsx', "open")  # write correct address, file name

    def HistoryEquipment(self):    # open equipment file for history run
        eq_number = self.ui.eq_number.toPlainText()  # input equipment number
        name = '8000' + str(eq_number)
        os.startfile('files\eq_files\{}.xlsx'.format(name), "open")  # write correct address, file name


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
