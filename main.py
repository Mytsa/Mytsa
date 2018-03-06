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
        self.ui.pushButton2.clicked.connect(self.s_part1)  # find spare part1
        self.ui.pushButton3.clicked.connect(self.s_part2)  # find spare part2
        self.ui.pushButton4.clicked.connect(self.s_part3)  # find spare part3
        self.ui.pushButton5.clicked.connect(self.s_part4)  # find spare part4
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
        self.ui.type_eq.setText(type_eq)   # output data of type equipment

# calculation logic
        sap_eq1 = '8000' + str(sap_eq)

        d = str('{}'.format(index[0])) + str(index[1])    # need decision
        g = str('{}'.format(index1[0])) + str(index1[1])  # need decision
        f = Log.filtr(type_eq)   # mark in message template on index by name
        Templ.wrt_templ(d, g, f, self.date, self.time, per_number, sap_eq1, counter)    # write data to template file (printing file)

# write data to equipment log file
        ex = Log.mark(sap_eq1)  # find index in file
        df = Log.lf(defect)  # loop in file log_f, class Excel, method lf()

        wb = load_workbook('eq_log/eq_file/{}.xlsx'.format(sap_eq1))  # file to write
        Log.data_log_eq(ex, wb, self.date, per_number, df, counter)    # sent data to work

        number_counter = Log.search_num_eq(sap_eq1, ex)
        num = number_counter

        self.ui.counter_info.setText(num)    # info block about last counter data in log file
# <! ------- spare parts write -----!>

        num_part1 = self.ui.sp1.toPlainText()
        num_part1 = '40000' + str(num_part1)
        name_part1 = Parts.name_part(num_part1)

        px_mark1 = Parts.mark(self.w_date, per_number)
        a = 'main'
        px_mark_log1 = Parts.mark_log(a)

        num_part2 = self.ui.sp3.toPlainText()  # ned decision about empty field
        if num_part2 == '':
            pass
        else:
            num_part2 = '40000' + str(num_part2)
            name_part2 = Parts.name_part(num_part2)

        num_part3 = self.ui.sp5.toPlainText()  # ned decision about empty field
        if num_part3 == '':
            pass
        else:
            num_part3 = '40000' + str(num_part3)
            name_part3 = Parts.name_part(num_part3)

        num_part4 = self.ui.sp7.toPlainText()  # ned decision about empty field
        if num_part4 == '':
            pass
        else:
            num_part4 = '40000' + str(num_part4)
            name_part4 = Parts.name_part(num_part4)


        if int(num) >= int(counter):
            # print('check counter with number in log file')
            self.ui.message.setText("input data of counter is not correct" + '\n' + "equipment log file is NOT saved")
        else:
            # check of input correct counter data, after successfully check write data to log or take a message
            forecast = Log.cntr(sap_eq1, ex, counter)   # show forecast of counter for the next repair
            type_eq_m = Log.te(type_eq)
            exl = Log.markl(type_eq_m)   # find last/mark row
            Log.eu_log(exl, type_eq_m, self.date, sap_eq1, per_number, df, counter)

            Parts.wrt_templ(per_number, self.w_date, px_mark1, num_part1, name_part1, sap_eq1, counter)
            Parts.wrt_log(px_mark_log1, self.date, per_number, num_part1, name_part1, sap_eq1, counter)

            if num_part2 == '':
                pass
            else:
                px_mark2 = Parts.mark(self.w_date, per_number)
                a = 'main'
                px_mark_log2 = Parts.mark_log(a)

                Parts.wrt_templ(per_number, self.w_date, px_mark2, num_part2, name_part2, sap_eq1, counter)
                Parts.wrt_log(px_mark_log2, self.date, per_number, num_part2, name_part2, sap_eq1, counter)

            if num_part3 == '':
                pass
            else:
                px_mark3 = Parts.mark(self.w_date, per_number)
                a = 'main'
                px_mark_log3 = Parts.mark_log(a)

                Parts.wrt_templ(per_number, self.w_date, px_mark3, num_part3, name_part3, sap_eq1, counter)
                Parts.wrt_log(px_mark_log3, self.date, per_number, num_part3, name_part3, sap_eq1, counter)

            if num_part4 == '':
                pass
            else:
                px_mark4 = Parts.mark(self.w_date, per_number)
                a = 'main'
                px_mark_log4 = Parts.mark_log(a)

                Parts.wrt_templ(per_number, self.w_date, px_mark4, num_part4, name_part4, sap_eq1, counter)
                Parts.wrt_log(px_mark_log4, self.date, per_number, num_part4, name_part4, sap_eq1, counter)

            wb.save('eq_log/eq_file/{}.xlsx'.format(sap_eq1))  # save equipment log file

            self.ui.message.setText('equipment log file is saved' + '\n' + 'to the next repair is: ' + forecast)


# print the template
    def print_mes(self):
        os.startfile('f2-02-04-5.xlsx', "print")  # write correct address, file name


# add spare part to cash file
    def s_part1(self):
        num_part1 = self.ui.sp1.toPlainText()  # input spare part
        num_part1 = '40000' + str(num_part1)
        if int(num_part1) > 400000001:
            name = Parts.name_part(num_part1)
            position = Parts.position_part(num_part1)
            self.ui.sp2.setText(name + '\n' + 'position is: ' + position)
        else:
            self.ui.sp2.setText('\n' + 'spare part is NOT find')

    def s_part2(self):
        num_part2 = self.ui.sp3.toPlainText()  # input spare part
        num_part2 = int(num_part2)
        if int(num_part2) > 1:
            num_part2 = '40000' + str(num_part2)
            name = Parts.name_part(num_part2)
            if name == '':  # ned decision about empty field
                self.ui.sp4.setText('\n' + 'spare part is NOT find')
            else:
                position = Parts.position_part(num_part2)
                self.ui.sp4.setText(name + '\n' + 'position is: ' + position)
        else:
            self.ui.sp4.setText('\n' + 'spare part is NOT find')
            num_part2 = ''  # ned decision about empty field
            self.ui.sp3.toPlainText(num_part2)

    def s_part3(self):
        num_part3 = self.ui.sp5.toPlainText()  # input spare part
        num_part3 = int(num_part3)
        if int(num_part3) > 1:
            num_part3 = '40000' + str(num_part3)
            name = Parts.name_part(num_part3)
            if name == '':  # ned decision about empty field
                self.ui.sp6.setText('\n' + 'spare part is NOT find')
            else:
                position = Parts.position_part(num_part3)
                self.ui.sp6.setText(name + '\n' + 'position is: ' + position)
        else:
            self.ui.sp6.setText('\n' + 'spare part is NOT find')
            num_part3 = ''  # ned decision about empty field
            self.ui.sp5.toPlainText(num_part3)

    def s_part4(self):
        num_part4 = self.ui.sp7.toPlainText()  # input spare part
        num_part4 = int(num_part4)
        if int(num_part4) > 1:
            num_part4 = '40000' + str(num_part4)
            name = Parts.name_part(num_part4)
            if name == '':  # ned decision about empty field
                self.ui.sp8.setText('\n' + 'spare part is NOT find')
            else:
                position = Parts.position_part(num_part4)
                self.ui.sp8.setText(name + '\n' + 'position is: ' + position)
        else:
            self.ui.sp8.setText('\n' + 'spare part is NOT find')
            num_part4 = ''  # ned decision about empty field
            self.ui.sp7.toPlainText(num_part4)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
sys.exit(app.exec_())
