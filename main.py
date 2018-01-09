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
        self.file_name = 'f2-02-04-5'
        self.date = datetime.strftime(datetime.now(), "%d/%m/%Y")
        self.time = datetime.strftime(datetime.now(), "%H:%M")



        self.ui.pushButton.clicked.connect(self.action)  # calculation
        self.ui.pushButton1.clicked.connect(self.print_mes)  # print card


    def action(self):
        # output clean area
        self.ui.counter.setText("")  # counter

        # input data
        per_number = self.ui.per_number.toPlainText()     # input personal number


        # defect need drop-list

        defect = self.ui.radioButton.setText('yes')  # input defect from radio-bottom
        # print(defect)



        sap_eq = self.ui.sap_eq.toPlainText()  # input sap number of equipment


        # type equipment need drop-list

        type_eq = self.ui.type_eq.toPlainText()  # input type equipment



        fault = self.ui.fault.toPlainText()  # input type fault
        counter = self.ui.counter.toPlainText()  # input counter


        # calculation logica


        # output data
        self.ui.counter.setText(counter)


        # read/write data intro/to file

        wrfile = load_workbook('{}.xlsx'.format(self.file_name))

        # index coordinate
        a = str('C') + str(4)
        b = str('F') + str(7)
        c = str('K') + str(7)
        d = str('A') + str(1)
        e = str('E') + str(22)
        f = str(y1) + str(y)
        g = str(z1) + str(z)
        h = str('D') + str(51)  # counter

        # write data
        sheet = wrfile.get_sheet_by_name('')

        sheet[a] = self.date
        sheet[b] = self.time
        sheet[c] = per_number
        sheet[d] = defect    # need decision
        sheet[e] = sap_eq
        sheet[f] = type_eq
        sheet[g] = fault
        sheet[h] = counter

        wrfile.save('{}.xlsx'.format(self.file_name))



    def print_mes(self):
        os.startfile('{}.xlsx'.format(self.file_name), "print")  # write correct address, file name

    def cc(self):
        print('working')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
sys.exit(app.exec_())
