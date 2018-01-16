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
        self.dic_defect = {'1': ['B', 11], '2': ['B', 12], '3': ['B', 13], '4': ['B', 14], '5': ['B', 15], '6': ['B', 16], '7': ['B', 17], '8': ['B', 18], '9': ['B', 19], '10': ['H', 11], '11': ['H', 12], '12': ['H', 13], '13': ['H', 14], '14': ['H', 15], '15': ['H', 16], '16': ['H', 17], '17': ['H', 18]}
        self.dic_fault = {'1': ['B', 33], '2': ['B', 34], '3': ['H', 33]}

    def action(self):
        # input data
        per_number = self.ui.per_number.toPlainText()     # input personal number
        defect = self.ui.defect.toPlainText()     # input defect
        index = self.dic_defect[defect]
        sap_eq = self.ui.sap_eq.toPlainText()  # input sap number of equipment
        fault = self.ui.fault.toPlainText()  # input type fault
        index1 = self.dic_fault[fault]
        counter = self.ui.counter.toPlainText()  # input counter

        # calculation logica
        wb = load_workbook(filename='eq.xlsx', read_only=True)
        ws = wb['eq']

        mark = sap_eq  # word to search last raw in sheet
        for row in ws:
            for cell in row:
                if cell.value == mark:
                    x = cell.row  # find last mark row, for data input place
                    break
        print(x.value)

        # type_eq =
        # output data
        # self.ui.type_eq.setText(type_eq)


        # read/write data intro/to file
        wrfile = load_workbook('f2-02-04-5.xlsx')
        sheet = wrfile.get_sheet_by_name('1')

        for i in range(11, 35):
            sheet[str('B') + str(i)] = ''  # clean check mark
            sheet[str('H') + str(i)] = ''  # clean check mark


        # index coordinate
        a = str('C7')
        b = str('F7')
        c = str('K7')
        d = str('{}'.format(index[0])) + str(index[1])
        e = str('F22')
        # f = str('D29')
        g = str('{}'.format(index1[0])) + str(index1[1])    # need decision
        h = str('D52')    # counter

        # write data

        sheet[a] = self.date
        sheet[b] = self.time
        sheet[c] = int(per_number)
        sheet[d] = 'X'
        sheet[e] = int(sap_eq)
        # sheet[f] = type_eq
        sheet[g] = 'X'
        sheet[h] = int(counter)

        wrfile.save('f2-02-04-5.xlsx')


    def print_mes(self):
        os.startfile('f2-02-04-5.xlsx', "print")  # write correct address, file name



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
sys.exit(app.exec_())
