# -*- coding: utf-8 -*-
from openpyxl import *
from datetime import datetime

class Parts:

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

