# -*- coding: utf-8 -*-
import sys
# window1 is our interface file
from window2 import *
from openpyxl import *
from datetime import datetime

class MyWin(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.action)    # print data - work
        self.ui.pushButton_2.clicked.connect(self.print_card)    # print data - work

    def action(self):
        self.ui.total_cycles.setText("")    # total_cycles
        self.ui.next_page.setText("")    # next page
        self.ui.correction.setText("")    # correction

        applicator = self.ui.applicator.toPlainText()
        cycles = self.ui.cycles.toPlainText()
        old_cycles = self.ui.old_cycles.toPlainText()
        page = self.ui.page.toPlainText()

        counter = self.ui.counter.toPlainText()
        total_cycles = str(int(cycles) + int(old_cycles))

        if counter != total_cycles:
            correction = str((int(counter) - (int(cycles) + int(old_cycles))))
            self.ui.total_cycles.setText(counter)
            self.ui.correction.setText(correction)
        else:
            self.ui.total_cycles.setText(total_cycles)

        page1 = str(int(page) + 1)
        self.ui.next_page.setText(page1)


        #write data to file
        wb = load_workbook(filename='counter_ver.1.xlsx', read_only=True)
        ws = wb['2017']

        mark = "**"  # word to search
        for row in ws:
            for cell in row:
                if cell.value == mark:
                    x = cell.row  # find last mark row
                    #print(x)
                    break

        wrfile = load_workbook('counter_ver.1.xlsx')

        date = datetime.strftime(datetime.now(), "%Y/%m/%d")

        a = str('A') + str(x)
        b = str('B') + str(x)
        c = str('C') + str(x)
        d = str('D') + str(x)
        e = str('E') + str(x)
        a1 = str('A') + str(x + 1)

        sheet = wrfile.get_sheet_by_name('2017')
        sheet[a] = int(applicator)
        sheet[b] = date
        sheet[c] = int(page)
        sheet[d] = int(cycles)
        sheet[e] = int(total_cycles)
        sheet[a1] = '**'

        wrfile.save('counter_ver.1.xlsx')


        # write data to file
        wb = load_workbook(filename='Template_apl_cycles.xlsx', read_only=True)
        wrfile = load_workbook('Template_apl_cycles.xlsx')

        b = str('B') + str(80)
        c = str('C') + str(75)

        sheet = wrfile.get_sheet_by_name('print')
        sheet[b] = "correction is: {}".format(correction)
        sheet[c] = int(total_cycles)

        wrfile.save('Template_apl_cycles.xlsx')

    def print_card(self):
        os.startfile("I:/python/code/cycles_apl/Template_apl_cycles.xlsx", "print")    # write correct address, file name

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
