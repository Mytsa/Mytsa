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
        self.m_date = datetime.strftime(datetime.now(), "%m")
        self.ui.pushButton.clicked.connect(self.action)  # calculation
        self.ui.pushButton1.clicked.connect(self.print_mes)  # write data to file
        self.ui.pushButton2.clicked.connect(self.find_spare_part)  # find spare part1
        # self.ui.pushButton3.clicked.connect(self.find_eq)  # find info about equipment

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
        if num_part1 == '':
            w_pcs1 = ''
            pass
        else:
            num_part1 = '40000' + str(num_part1)
            name_part1 = Parts.name_part(num_part1)
            pcs1 = self.ui.pcs1.toPlainText()

            if pcs1 == '':
                w_pcs1 = 'write correct pieces for spare parts №1' + '\n'
                num = counter
                #m_counter = ""
            else:
                w_pcs1 = ''
                #m_counter = "input data of counter is not correct"

        num_part2 = self.ui.sp3.toPlainText()  # ned decision about empty field
        if num_part2 == '':
            w_pcs2 = ''
            pass
        else:
            num_part2 = '40000' + str(num_part2)
            name_part2 = Parts.name_part(num_part2)
            pcs2 = self.ui.pcs2.toPlainText()

            if pcs2 == '':
                w_pcs2 = 'write correct pieces for spare parts №2' + '\n'
                num = counter
                #m_counter = ""
            else:
                w_pcs2 = ''
                #m_counter = "input data of counter is not correct"

        num_part3 = self.ui.sp5.toPlainText()  # ned decision about empty field
        if num_part3 == '':
            w_pcs3 = ''
            pass
        else:
            num_part3 = '40000' + str(num_part3)
            name_part3 = Parts.name_part(num_part3)
            pcs3 = self.ui.pcs3.toPlainText()

            if pcs3 == '':
                w_pcs3 = 'write correct pieces for spare parts №3'  + '\n'
                num = counter
                #m_counter = ""
            else:
                w_pcs3 = ''
                #m_counter = "input data of counter is not correct"

        num_part4 = self.ui.sp7.toPlainText()  # ned decision about empty field
        if num_part4 == '':
            w_pcs4 = ''
            pass
        else:
            num_part4 = '40000' + str(num_part4)
            name_part4 = Parts.name_part(num_part4)
            pcs4 = self.ui.pcs4.toPlainText()

            if pcs4 == '':
                w_pcs4 = 'write correct pieces for spare parts №4'
                num = counter
                # m_counter = ""
            else:
                w_pcs4 = ''
                

        if int(num) >= int(counter):
            # print('check counter with number in log file')
            #print('1')
            m_counter = "input data of counter is not correct" + '\n' 
            self.ui.message.setText("equipment log file is NOT saved" + '\n' + m_counter + w_pcs1 + w_pcs2 + w_pcs3 + w_pcs4)
        else:
            #print('2')
            # check of input correct counter data, after successfully check write data to log or take a message
            #forecast = Log.cntr(sap_eq1, ex, counter)   # show forecast of counter for the next repair
            l_counter = Log.l_cntr(sap_eq1, ex)    # last wrote counter
            type_eq_m = Log.te(type_eq)
            exl = Log.markl(type_eq_m)   # find last/mark row
            Log.eu_log(exl, type_eq_m, self.date, sap_eq1, per_number, df, counter)

            if num_part1 == '':
                pass
            else:
                px_mark1 = Parts.mark(self.w_date, per_number)
                a = 'main'
                px_mark_log1 = Parts.mark_log(a)                     

                Parts.wrt_templ(per_number, self.w_date, px_mark1, num_part1, name_part1, pcs1, sap_eq1, counter)
                Parts.wrt_log(px_mark_log1, self.date, per_number, num_part1, name_part1, pcs1, sap_eq1, counter)

                #if name_part1 == ('crimper wire' or 'crimper insulation'):
                    # write data to file with control of repair of applicator
                    #name_part1 = 1
# BIG PROBLEM WITH SENT DATA BY SINGLE
                    #name_part2 = 0 # how write sigly
                    #Parts.apl_sp(self.m_date, sap_eq1, self.date, name_part1, name_part2, df, counter, per_number)

                #elif name_part1 == ('anvil wire' or 'anvil insulation' or 'anvil'):
                    # write data to file with control of repair of applicator
                #else:
                    #pass

            if num_part2 == '':
                pass
            else:
                px_mark2 = Parts.mark(self.w_date, per_number)
                a = 'main'
                px_mark_log2 = Parts.mark_log(a)

                Parts.wrt_templ(per_number, self.w_date, px_mark2, num_part2, name_part2, pcs2, sap_eq1, counter)
                Parts.wrt_log(px_mark_log2, self.date, per_number, num_part2, name_part2, pcs2, sap_eq1, counter)

            if num_part3 == '':
                pass
            else:
                px_mark3 = Parts.mark(self.w_date, per_number)
                a = 'main'
                px_mark_log3 = Parts.mark_log(a)

                Parts.wrt_templ(per_number, self.w_date, px_mark3, num_part3, name_part3, pcs3, sap_eq1, counter)
                Parts.wrt_log(px_mark_log3, self.date, per_number, num_part3, name_part3, pcs3, sap_eq1, counter)

            if num_part4 == '':
                pass
            else:
                px_mark4 = Parts.mark(self.w_date, per_number)
                a = 'main'
                px_mark_log4 = Parts.mark_log(a)

                Parts.wrt_templ(per_number, self.w_date, px_mark4, num_part4, name_part4, pcs4, sap_eq1, counter)
                Parts.wrt_log(px_mark_log4, self.date, per_number, num_part4, name_part4, pcs4, sap_eq1, counter)

            wb.save('eq_log/eq_file/{}.xlsx'.format(sap_eq1))  # save equipment log file

            dif_counter = str(int(counter) - int(l_counter))

            self.ui.message.setText('logs files were saved' + '\n' + 'the difference between the repairs is: ' + dif_counter )


# print the template
    def print_mes(self):
        os.startfile('f2-02-04-5.xlsx', "print")  # write correct address, file name


#     def find_eq(self):
#         num_part1 = self.ui.sp1.toPlainText()  # input spare part
#         num_part1 = '40000' + str(num_part1)
#         if int(num_part1) > 400000001:
#             name = Parts.name_part(num_part1)
#             position = Parts.position_part(num_part1)
#             self.ui.sp2.setText(name + '\n' + 'position is: ' + position)
#         else:
#             self.ui.sp2.setText('\n' + 'spare part is NOT find')

    def find_spare_part(self):
        find_spare_part = self.ui.fp.toPlainText()  # input spare part
        find_spare_part = int(find_spare_part)

#<!-------- need write all symbols like in catalog file
        # sap_number = Parts.sap_part(find_spare_part)
        # name = Parts.name_part(find_spare_part)
        # position = Parts.position_part(find_spare_part)
        # self.ui.sp4.setText(name + '\n' + 'position is: ' + position + '\n' + sap_number)
# ---------------!>

        if int(find_spare_part) > 1:
            find_spare_part = '40000' + str(find_spare_part)
            name = Parts.name_part(find_spare_part)
            if name == '':  # ned decision about empty field
                self.ui.sp4.setText('\n' + 'spare part is NOT find')
            else:
                position = Parts.position_part(find_spare_part)
                self.ui.sp4.setText(name + '\n' + 'position is: ' + position)
        else:
            self.ui.sp4.setText('\n' + 'spare part is NOT find')
            find_spare_part = ''  # ned decision about empty field
            self.ui.fp.toPlainText(find_spare_part)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
sys.exit(app.exec_())
