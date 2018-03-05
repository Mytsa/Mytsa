# -*- coding: utf-8 -*-
from openpyxl import *
from datetime import datetime

class Parts:
    # def __init__(self):
    #     self.w_date = datetime.strftime(datetime.now(), "%W")

    def mark(w_date, per_number):
        wb = load_workbook('spare_parts/{}.xlsx'.format(per_number))
        # print(w_date)
        ws = wb[w_date]
        # find last mark row, for new data place
        mark = '**'
        for row in ws:
            for cell in row:
                if cell.value == mark:
                    ex = cell.row
                    # print(ex)
                    return ex

    def wrt_templ(per_number, w_date, px, num_part, name_part, sap_eq1, counter):
        wrfile1 = load_workbook('spare_parts/{}.xlsx'.format(per_number))
        sheet = wrfile1.get_sheet_by_name(w_date)

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
        wrfile1.save(('spare_parts/{}.xlsx'.format(per_number)))

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
        wrfile2 = load_workbook('spare_parts/s_parts_log.xlsx')
        sheet = wrfile2.get_sheet_by_name('main')
        px = int(px)    # only for position A1

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
        wrfile2.save('spare_parts/s_parts_log.xlsx')

    def mark_c(mark):
        wb = load_workbook('spare_parts/cash.xlsx')
        ws = wb['1']
        # find last mark row, for new data place
        for row in ws:
            for cell in row:
                if cell.value == mark:
                    ex = cell.row
                    return ex

    def cash_save(index, ex, num_part):
        wb = load_workbook('spare_parts/cash.xlsx')
        ws = wb['1']
        a = str(index) + str(ex)
        a1 = str(index) + str(1 + ex)
        ws[a] = num_part
        ws[a1] = '**'
        wb.save('spare_parts/cash.xlsx')

    def inf_cash(index):
        wb = load_workbook('spare_parts/cash.xlsx')
        ws = wb['1']
        mark = '**'
        for row in ws:
            for cell in row:
                if cell.value == mark:
                    ex = cell.row
                    pos = index + str(ex - 1)
                    number = ws[pos].value
                    return number

    def clean_cash(index):
        wb = load_workbook('spare_parts/cash.xlsx')
        ws = wb['1']
        for i in range(1, 6):
            ws[str(index) + str(i)] = ''  # clean check mark
        pos = str(index) + str('1')
        ws[pos] = '**'
        wb.save('spare_parts/cash.xlsx')

    def name_part(mark):
        wb = load_workbook('spare_parts/spare_parts_catalog.xlsx')
        ws = wb['main']
        mark = str('*') + str(mark)
        for row in ws:
            for cell in row:
                if cell.value == mark:
                    ex = cell.row
                    pos = 'C' + str(ex)
                    name = ws[pos].value
                    return name

    def position_part(mark):
        wb = load_workbook('spare_parts/spare_parts_catalog.xlsx')
        ws = wb['main']
        mark = str('*') + str(mark)
        for row in ws:
            for cell in row:
                if cell.value == mark:
                    ex = cell.row
                    pos = 'D' + str(ex)
                    position = ws[pos].value
                    return position


