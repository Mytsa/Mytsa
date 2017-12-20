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
        # self.ui.avans.setText("")  # avans
        # self.ui.pay.setText("")  # pay
        # self.ui.month_pay.setText("")  # month_pay
        # self.ui.total_work_hours.setText("")  # total_work_hours

        # input data
        s_part = self.ui.s_part.toPlainText()     # search spare part in catalog
        # dodat = self.ui.proc.toPlainText()
        # hour = self.ui.hours.toPlainText()
        # whour = self.ui.w_hours.toPlainText()
        # prysut = self.ui.bonus_present.toPlainText()
        # bonus = self.ui.bonus.toPlainText()
        # over = self.ui.overtime.toPlainText()
        # pover = self.ui.bonus_overtime.toPlainText()

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

        # mark = s_part  # word to search last raw in sheet
        # for row in ws:
        #     for cell in row:
        #         if cell.value == mark:
        #             x = cell.row  # find mark row, for data input place
        #             break

        # # write data to counter file
        # wrfile = load_workbook('counter_apl.xlsx')
        #             ws.title = "New Title"   # create sheet with name "new title
        #
        # # index coordinate
        # a = str('A') + str(x)
        # b = str('B') + str(x)
        # c = str('C') + str(x)
        # d = str('D') + str(x)
        # e = str('E') + str(x)
        # a1 = str('A') + str(x + 1)  # for mark symbols
        #
        # # write data
        # sheet = wrfile.get_sheet_by_name(y_date)
        # sheet[a] = int(applicator)
        # sheet[b] = date
        # sheet[c] = int(page)
        # sheet[d] = int(cycles)
        # sheet[e] = int(total_cycles)
        # sheet[a1] = '**'
        #
        # wrfile.save('counter_apl.xlsx')

