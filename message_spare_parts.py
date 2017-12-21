# -*- coding: utf-8 -*-
import sys
# window1 is our interface file
from gui import *
from openpyxl import *
from datetime import datetime

class MyWin(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.action)  # calculation


    def action(self):
        # output clean area
        # self.ui.avans.setText("")  # avans
        # self.ui.pay.setText("")  # pay
        # self.ui.month_pay.setText("")  # month_pay
        # self.ui.total_work_hours.setText("")  # total_work_hours

        # input data
        s_part = self.ui.s_part.toPlainText()     # search spare part in catalog

        # calculation logica


        # read/write data intro/to file

        # date = datetime.strftime(datetime.now(), "%Y/%m/%d")  # local variables for excel

        wb = load_workbook('catalog.xlsx')
        ws = wb.active

        # searching date in A column and print all row
        date = input("Prompt: ")
        for row in ws.iter_rows('A{}:A{}'.format(ws.min_row, ws.max_row)):
            for cell in row:
                if ws.cell(row=row, column=0).value == date:
                    print(ws.cell.value)


