# -*- coding: utf-8 -*-

import sys
from openpyxl import *
from datetime import datetime
# window1 is our interface file
from window1 import *
# from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = UiDialog()
        self.ui.setupUi(self)

        # push button and function is go
        self.ui.pushButton_2.clicked.connect(self.action)    # action of calculation
        self.ui.pushButton.clicked.connect(self.print_card)    # print data - work


    def action(self):
        self.ui.textEdit_5.setText("")    # total_cycles
        self.ui.textEdit_6.setText("10")    # correction
        self.ui.textEdit_8.setText("")    # next page

        applicator = self.ui.textEdit.toPlainText()
        # applicator = int(input('input SAP number of applicator: '))

        page = self.ui.textEdit_2.toPlainText()
        #page = int(input('input page number of card: '))
        # page1 = page + 1

        cycles = self.ui.textEdit_3.toPlainText()
        #cycles = int(input('input cycles: '))

        old_cycles = self.ui.textEdit_4.toPlainText()
        #old_cycles = int(input('input cycles previous card: '))


        self.ui.textEdit_8.setText(page)



        # checkbox action
        # c = 1
        # if c is 'y':
        #     #counter = int(input('input counter data: '))
        #     counter = self.ui.textEdit_7.toPlainText()
        #     correction = counter - (cycles + old_cycles)
        #     self.ui.textEdit_6.setText(correction)
        #     total_cycles = counter
        #     # print('correction is: {} '.format(correction))
        # else:
        total_cycles = cycles + old_cycles
        self.ui.textEdit_5.setText(total_cycles, applicator)


        #
        # # write data to file
        # wb = load_workbook(filename='counter_ver.1.xlsx', read_only=True)
        # ws = wb['2017']
        #
        # mark = "**"  # word to search
        # for row in ws:
        #     for cell in row:
        #         if cell.value == mark:
        #             x = cell.row  # find last mark row
        #             print(x)
        #             break
        #
        # wrfile = load_workbook('counter_ver.1.xlsx')
        #
        # date = datetime.strftime(datetime.now(), "%Y/%m/%d")
        #
        # a = str('A') + str(x)
        # b = str('B') + str(x)
        # c = str('C') + str(x)
        # d = str('D') + str(x)
        # e = str('E') + str(x)
        # a1 = str('A') + str(x + 1)
        #
        # sheet = wrfile.get_sheet_by_name('2017')
        # sheet[a] = applicator
        # sheet[b] = date
        # sheet[c] = page
        # sheet[d] = cycles
        # sheet[e] = total_cycles
        # sheet[a1] = '**'
        #
        # wrfile.save('counter_ver.1.xlsx')
        #


    def print_card(self):
        os.startfile("I:/python/code/cycles_apl/counter_ver.1.xlsx", "print")    # write correct address, file name


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
