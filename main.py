# -*- coding: utf-8 -*-
import sys
from openpyxl import *
from datetime import datetime
from gui import *    # gui is interface file
from log_f import Log    # file work with log
from templ_f import Templ    # file work with template
from s_parts import Parts    # file work with template


class MyWin(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.date = datetime.strftime(datetime.now(), "%d/%m/%Y")
        self.time = datetime.strftime(datetime.now(), "%H:%M")
        self.w_date = datetime.strftime(datetime.now(), "%W")
        self.ui.pushButton.clicked.connect(self.action)  # calculation
        self.ui.pushButton1.clicked.connect(self.print_mes)  # write data to file
        self.dic_defect = {'1': ['B', 11], '2': ['B', 12], '3': ['B', 13], '4': ['B', 14], '5': ['B', 15], '6': ['B', 16], '7': ['B', 17], '8': ['B', 18], '17': ['B', 19], '9': ['H', 11], '10': ['H', 12], '11': ['H', 13], '12': ['H', 14], '13': ['H', 15], '14': ['H', 16], '15': ['H', 17], '16': ['H', 18]}
        self.dic_fault = {'1': ['B', 33], '3': ['B', 34], '2': ['H', 33]}


    def action(self):
    # input data
        per_number = self.ui.per_number.toPlainText()     # input personal number
        sap_eq = self.ui.sap_eq.toPlainText()  # input sap number of equipment
        defect = self.ui.defect.toPlainText()  # input defect
        index = self.dic_defect[defect]
        fault = self.ui.fault.toPlainText()  # input type fault
        index1 = self.dic_fault[fault]
        counter = self.ui.counter.toPlainText()  # input counter

        type_eq = Log.type(sap_eq)  # find log file and info about type of equipment
    # output data
        self.ui.type_eq.setText(type_eq)

# calculation logic
        sap_eq1 = '8000' + str(sap_eq)

        d = str('{}'.format(index[0])) + str(index[1])    # need decision
        g = str('{}'.format(index1[0])) + str(index1[1])  # need decision
        f = Log.filtr(type_eq)   # mark in message template on index by name
        Templ.wrt_templ(d, g, f, self.date, self.time, per_number, sap_eq1, counter)    # write data to template file

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

        num_part1 = self.ui.sp1.toPlainText()    # input spare part
        num_part1 = int(num_part1)
        name_part1 = 'anvil test'  # need decision about catalog list with spare parts

        if num_part1 > 1:
            px1 = Parts.mark(per_number)
            # Parts.wrt_templ(per_number, px, num_part1, name_part, sap_eq1, counter)
            a = 'main'
            px11 = Parts.mark_log(a)
            # Parts.wrt_log(px1, self.date, per_number, num_part1, name_part, sap_eq1, counter)
            m_part1 = ''

            if int(num) >= int(counter):
                self.ui.message.setText("input data of counter is not correct" + '\n' + "equipment log file is NOT saved" + '\n' + m_part1)
            else:
                pass
        else:
            m_part1 = 'write correct SAP number of spare part1'
            num = counter


        num_part2 = self.ui.sp2.toPlainText()  # input spare part
        num_part2 = int(num_part2)
        name_part2 = 'anvil test2'  # need decision about catalog list with spare parts
        empty = 0

        if num_part2 == empty:
            m_part2 = ''
            self.ui.message.setText("input data of counter is not correct" + '\n' + "equipment log file is NOT saved" + '\n' + m_part2)
        elif num_part2 > 1:
            px2 = px1 + 1
            px22 = px11 + 1
            m_part2 = ''

            if int(num) >= int(counter):
                self.ui.message.setText("input data of counter is not correct" + '\n' + "equipment log file is NOT saved" + '\n' + m_part2)
            else:
                pass
        else:
            m_part2 = 'write correct SAP number of spare part2'
            num = counter

        # check of input correct counter data, after successfully check write data to log or take a message
        if int(num) < int(counter):
            # show forecast of counter for the next repair
            forecast = Log.cntr(sap_eq1, ex, counter)
            type_eq_m = Log.te(type_eq)
            exl = Log.markl(type_eq_m)   # find last/mark row
            Log.eu_log(exl, type_eq_m, self.date, sap_eq1, per_number, df, counter)

            wb.save('eq_log/eq_file/{}.xlsx'.format(sap_eq1))

            Parts.wrt_templ(per_number, px1, num_part1, name_part1, sap_eq1, counter)
            Parts.wrt_log(px11, self.date, per_number, num_part1, name_part1, sap_eq1, counter)

            Parts.wrt_templ(per_number, px2, num_part2, name_part2, sap_eq1, counter)
            Parts.wrt_log(px22, self.date, per_number, num_part2, name_part2, sap_eq1, counter)

            self.ui.message.setText('equipment log file is saved' + '\n' + 'to the next repair is: ' + forecast + '\n' + m_part1 + '\n' + m_part2)
        else:
            self.ui.message.setText("input data of counter is not correct" + '\n' + "equipment log file is NOT saved" + '\n' + m_part1 + '\n' + m_part2)


# print the template
    def print_mes(self):
        os.startfile('f2-02-04-5.xlsx', "print")  # write correct address, file name


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
sys.exit(app.exec_())
