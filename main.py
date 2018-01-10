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
        self.date = datetime.strftime(datetime.now(), "%d/%m/%Y")
        self.time = datetime.strftime(datetime.now(), "%H:%M")

        self.ui.pushButton.clicked.connect(self.action)  # calculation
        self.ui.pushButton1.clicked.connect(self.print_mes)  # write data to file


    def action(self):
        # input data
        per_number = self.ui.per_number.toPlainText()     # input personal number
        defect = self.ui.defect.toPlainText()     # input defect
        sap_eq = self.ui.sap_eq.toPlainText()  # input sap number of equipment
        # type_eq = self.ui.type_eq.toPlainText()  # input type equipment
        fault = self.ui.fault.toPlainText()  # input type fault
        counter = self.ui.counter.toPlainText()  # input counter

        # output data
        # self.ui.type_eq.setText(counter)
        # calculation logica


        # read/write data intro/to file
        wrfile = load_workbook('f2-02-04-5.xlsx')

        # index coordinate
        a = str('C') + str(7)
        b = str('F') + str(7)
        c = str('K') + str(7)
        d = str('D') + str(19)
        e = str('F') + str(22)
        f = str('D') + str(29)
        g = str('D') + str(34)
        h = str('D') + str(52)  # counter

        # write data
        sheet = wrfile.get_sheet_by_name('1')

        sheet[a] = self.date
        sheet[b] = self.time
        sheet[c] = int(per_number)
        sheet[d] = defect    # need decision
        sheet[e] = int(sap_eq)
        sheet[f] = type_eq
        sheet[g] = fault
        sheet[h] = int(counter)

        wrfile.save('f2-02-04-5.xlsx')


    def print_mes(self):
        os.startfile('f2-02-04-5.xlsx', "print")  # write correct address, file name


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
sys.exit(app.exec_())
