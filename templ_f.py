# -*- coding: utf-8 -*-
from openpyxl import *
from datetime import datetime

class Templ:
    # def __init__(self):
    #     self.date = datetime.strftime(datetime.now(), "%d/%m/%Y")
    #     self.time = datetime.strftime(datetime.now(), "%H:%M")


    def wrt_templ(d, g, f, date, time, per_number, sap_eq1, counter):
        wrfile = load_workbook('f2-02-04-5.xlsx')
        sheet = wrfile.get_sheet_by_name('1')

        for i in range(11, 35):
            sheet[str('B') + str(i)] = ''  # clean check mark
            sheet[str('H') + str(i)] = ''  # clean check mark
        # index coordinate for template file
        a = str('C7')
        b = str('F7')
        c = str('K7')
        e = str('F22')
        h = str('D52')  # counter
        # write data to template file
        sheet[a] = date
        sheet[b] = time
        sheet[c] = int(per_number)
        sheet[d] = 'X'
        sheet[e] = int(sap_eq1)
        sheet[f] = 'X'
        sheet[g] = 'X'
        sheet[h] = int(counter)
        wrfile.save('f2-02-04-5.xlsx')
