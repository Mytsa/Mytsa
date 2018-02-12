# -*- coding: utf-8 -*-
import sys
from openpyxl import *
from datetime import datetime
from gui import *    # gui is interface file
from log_f import Log    # file work with log


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
        sap_eq = self.ui.sap_eq.toPlainText()  # input sap number of equipment

        # find log file
        type_eq = Log.type(sap_eq)

        # output data
        self.ui.type_eq.setText(type_eq)

        # write data intro/to template file
        wrfile = load_workbook('f2-02-04-5.xlsx')
        sheet = wrfile.get_sheet_by_name('1')
        for i in range(11, 35):
            sheet[str('B') + str(i)] = ''  # clean check mark
            sheet[str('H') + str(i)] = ''  # clean check mark


        # mark in message template on index by name
        f = Log.filtr(type_eq)

        defect = self.ui.defect.toPlainText()  # input defect
        index = self.dic_defect[defect]

        fault = self.ui.fault.toPlainText()  # input type fault
        index1 = self.dic_fault[fault]
        counter = self.ui.counter.toPlainText()  # input counter

# calculation logic
        sap_eq1 = '8000' + str(sap_eq)
        # index coordinate for template file
        a = str('C7')
        b = str('F7')
        c = str('K7')
        d = str('{}'.format(index[0])) + str(index[1])
        e = str('F22')
        g = str('{}'.format(index1[0])) + str(index1[1])    # need decision
        h = str('D52')    # counter

        # write data to template file
        sheet[a] = self.date
        sheet[b] = self.time
        sheet[c] = int(per_number)
        sheet[d] = 'X'
        sheet[e] = int(sap_eq1)
        sheet[f] = 'X'
        sheet[g] = 'X'
        sheet[h] = int(counter)

        wrfile.save('f2-02-04-5.xlsx')

    # write data to equipment log file

        wb = load_workbook('eq_log/eq_file/{}.xlsx'.format(sap_eq1))  # find file by number
        ws = wb['main']

        ex = Log.mark(sap_eq1)    # find index in file

        # index coordinate to equipment file
        a = str('A') + str(ex)
        b = str('B') + str(ex)
        c = str('C') + str(ex)
        d = str('D') + str(ex)
        a1 = str('A') + str(ex + 1)  # for mark symbols

        # write data to equipment file
        df = Log.lf(defect)    # loop in file log_f, class Excel, method lf()

        sheet = wb.get_sheet_by_name('main')
        sheet[a] = self.date
        sheet[b] = per_number
        sheet[c] = df
        sheet[d] = counter
        sheet[a1] = '**'

        pos = str('D') + str(ex - 1)  # take type of equipment
        num = str(ws[pos].value)
        self.ui.counter_info.setText(num)    # info block about last counter data in log file

    # show forecast of counter for the next repair
        pos_f = str('D') + str(ex)
        num_r = int(ws[pos_f].value)
        pos_aver = str('H2')
        num_aver = int(ws[pos_aver].value)

        forecast = num_aver - num_r
        forecast = str(forecast)

        # check of input correct counter data, after successfully check write data to log or take a message
        if int(num) < int(counter):

            type_eq_m = Log.te(type_eq)
            exl = Log.markl(type_eq_m)
            w = load_workbook('eq_log/general equipment log.xlsx')

            a = str('A') + str(exl)
            b = str('B') + str(exl)
            c = str('C') + str(exl)
            d = str('D') + str(exl)
            e = str('E') + str(exl)
            a1 = str('A') + str(exl + 1)  # for mark symbols
            # write data to equipment file
            sheet = w.get_sheet_by_name(type_eq_m)
            sheet[a] = self.date
            sheet[b] = sap_eq1
            sheet[c] = per_number
            sheet[d] = df
            sheet[e] = counter
            sheet[a1] = '**'

            w.save('eq_log/general equipment log.xlsx')

            wb.save('eq_log/eq_file/{}.xlsx'.format(sap_eq1))
            self.ui.message.setText('equipment log file is saved' + '\n' + 'forecast of next repair is: ' + forecast)
        else:
            self.ui.message.setText("input data of counter is not correct" + '\n' + "equipment log file is NOT saved")





# print the template
    def print_mes(self):
        os.startfile('f2-02-04-5.xlsx', "print")  # write correct address, file name


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
sys.exit(app.exec_())
