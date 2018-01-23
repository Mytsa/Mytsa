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
        self.dic_defect = {'1': ['B', 11], '2': ['B', 12], '3': ['B', 13], '4': ['B', 14], '5': ['B', 15], '6': ['B', 16], '7': ['B', 17], '8': ['B', 18], '17': ['B', 19], '9': ['H', 11], '10': ['H', 12], '11': ['H', 13], '12': ['H', 14], '13': ['H', 15], '14': ['H', 16], '15': ['H', 17], '16': ['H', 18]}
        self.dic_fault = {'1': ['B', 33], '3': ['B', 34], '2': ['H', 33]}

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
        sap_eq1 = '8000' + str(sap_eq)
        wb = load_workbook('eq_log/{}.xlsx'.format(sap_eq1))
        ws = wb['main']

        pos = str('G2')
        print(ws[pos].value)
        type_eq = str(ws[pos].value)

        # output data
        self.ui.type_eq.setText(type_eq)


        # read/write data intro/to file
        wrfile = load_workbook('f2-02-04-5.xlsx')
        sheet = wrfile.get_sheet_by_name('1')

        for i in range(11, 35):
            sheet[str('B') + str(i)] = ''  # clean check mark
            sheet[str('H') + str(i)] = ''  # clean check mark


        if type_eq == 'Аплікатор':
            #type_eq_pos = 'Аплікатор'
            f = str('B25')
        elif type_eq == 'Komax Alpha 355 / 355 S':
            #type_eq_pos = 'Komax Alpha 355 / 355 S'
            f = str('B26')
        elif type_eq == 'Komax Gamma 333 PC':
            #type_eq_pos = 'Komax Gamma 333 PC'
            f = str('B27')
        elif type_eq == 'Schunk / Stapla ультразвукова зварка':
           # type_eq_pos = 'Schunk / Stapla ультразвукова зварка'
            f = str('B28')
        elif type_eq == 'Кабельбіндеровий пістолет':
            #type_eq_pos = 'Кабельбіндеровий пістолет'
            f = str('H25')
        elif type_eq == 'Raychem / Raychem TE':
            #type_eq_pos = 'Raychem / Raychem TE'
            f = str('H26')
        elif type_eq == 'Komax Twist BT 188 t / BT 188':
            #type_eq_pos = 'Komax Twist BT 188 t / BT 188'
            f = str('H27')
        elif type_eq == 'Kabateck / Ondal':
            #type_eq_pos = 'Kabateck / Ondal'
            f = str('H28')
        else:
            #type_eq_pos = type_eq
            f = str('B29')

        # index coordinate
        a = str('C7')
        b = str('F7')
        c = str('K7')
        d = str('{}'.format(index[0])) + str(index[1])
        e = str('F22')
        g = str('{}'.format(index1[0])) + str(index1[1])    # need decision
        h = str('D52')    # counter

        # write data

        sheet[a] = self.date
        sheet[b] = self.time
        sheet[c] = int(per_number)
        sheet[d] = 'X'
        sheet[e] = int(sap_eq)
        sheet[f] = 'X'
        sheet[g] = 'X'
        sheet[h] = int(counter)

        wrfile.save('f2-02-04-5.xlsx')

# write data to eq_log
        wb = load_workbook('eq_log/{}.xlsx'.format(sap_eq1))
        ws = wb['main']

        mark = '**'
        for row in ws:
            for cell in row:
                if cell.value == mark:
                    ex = cell.row  # find last mark row, for data place
                    break

        # index coordinate
        a = str('A') + str(ex)
        b = str('B') + str(ex)
        d = str('D') + str(ex)

        a1 = str('A') + str(ex + 1)  # for mark symbols

        # write data
        sheet[a] = self.date
        sheet[b] = per_number
        sheet[d] = 'write data'

        sheet[a1] = '**'
        wb.save('eq_log/{}.xlsx'.format(sap_eq1))

    def print_mes(self):
        os.startfile('f2-02-04-5.xlsx', "print")  # write correct address, file name



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
sys.exit(app.exec_())
