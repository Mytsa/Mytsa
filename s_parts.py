# -*- coding: utf-8 -*-
from openpyxl import *
from datetime import datetime

class Parts:
    # def __init__(self):
    #     self.date = self.date = datetime.strftime(datetime.now(), "%d/%m/%Y")

    def mark(per_number):
        wb = load_workbook('spare_parts/p_spare.xlsx')
        ws = wb[per_number]
        # find last mark row, for new data place
        mark = '**'
        for row in ws:
            for cell in row:
                if cell.value == mark:
                    ex = cell.row
                    # print(ex)
                    return ex

    def wrt_templ(per_number, px, num_part, name_part, sap_eq1, counter):
        wrfile = load_workbook('spare_parts/p_spare.xlsx')
        sheet = wrfile.get_sheet_by_name(per_number)

        # index coordinate for template file
        a = str('B') + str(px)
        b = str('C') + str(px)
        c = str('D') + str(px)
        d = str('E') + str(px)
        e = str('F') + str(px)  # counter
        a1 = str('B') + str(1+px)
        # write data to template file
        sheet[a] = num_part
        sheet[b] = name_part
        sheet[c] = '1'
        sheet[d] = int(sap_eq1)
        sheet[e] = int(counter)
        sheet[a1] = '**'
        wrfile.save('spare_parts/p_spare.xlsx')

    def mark_log(a):
        wb = load_workbook('spare_parts/s_parts_log.xlsx')
        ws = wb[a]
        # find last mark row, for new data place
        mark = '**'
        for row in ws:
            for cell in row:
                if cell.value == mark:
                    ex = cell.row
                    #print(ex)
                    return ex

    def wrt_log(px, date, per_number, num_part, name_part, sap_eq1, counter):
        wrfile = load_workbook('spare_parts/s_parts_log.xlsx')
        sheet = wrfile.get_sheet_by_name('main')

        # index coordinate for template file
        a = str('A') + str(px)
        b = str('B') + str(px)
        c = str('C') + str(px)
        d = str('D') + str(px)
        e = str('E') + str(px)
        f = str('F') + str(px)
        g = str('G') + str(px)
        a1 = str('A') + str(1+px)
        # write data to template file
        sheet[a] = date
        sheet[b] = per_number
        sheet[c] = num_part
        sheet[d] = name_part
        sheet[e] = '1'
        sheet[f] = sap_eq1
        sheet[g] = counter
        sheet[a1] = '**'
        wrfile.save('spare_parts/s_parts_log.xlsx')
