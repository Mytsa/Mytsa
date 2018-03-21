# -*- coding: utf-8 -*-
from openpyxl import *
from datetime import datetime

class Parts:
    # def __init__(self):
    #     self.w_date = datetime.strftime(datetime.now(), "%W")

    def f_mark_row(ws):
        mark = '**'
        for row in ws:
            for cell in row:
                if cell.value == mark:
                    ex = cell.row
                    # print(ex)
                    return ex

    def mark(w_date, per_number):
        wb = load_workbook('spare_parts/{}.xlsx'.format(per_number))
        ws = wb[w_date]
        ex = Parts.f_mark_row(ws)
        return ex

    def wrt_templ(per_number, w_date, px, num_part, name_part, pcs, sap_eq1, counter):
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
        sheet[c] = pcs
        sheet[d] = int(sap_eq1)
        sheet[e] = int(counter)
        sheet[a1] = '**'
        wrfile1.save(('spare_parts/{}.xlsx'.format(per_number)))

    def mark_log(a):
        wb = load_workbook('spare_parts/s_parts_log.xlsx')
        ws = wb[a]
        # find last mark row, for new data place
        ex = Parts.f_mark_row(ws)
        return ex

    def wrt_log(px, date, per_number, num_part, name_part, pcs, sap_eq1, counter):
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
        sheet[e] = pcs
        sheet[f] = sap_eq1
        sheet[g] = counter
        sheet[a1] = '**'
        wrfile2.save('spare_parts/s_parts_log.xlsx')

    def mark_c(mark):
        wb = load_workbook('spare_parts/cash.xlsx')
        ws = wb['1']
        # find last mark row, for new data place
        ex = Parts.f_mark_row(ws)
        return ex

    def inf_cash(index):
        wb = load_workbook('spare_parts/cash.xlsx')
        ws = wb['1']
        ex = Parts.f_mark_row(ws)
        pos = index + str(ex - 1)
        number = ws[pos].value
        return number

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

    def sap_part(mark):
        wb = load_workbook('spare_parts/spare_parts_catalog.xlsx')
        ws = wb['main']
        mark = str('*') + str(mark)
        for row in ws:
            for cell in row:
                if cell.value == mark:
                    ex = cell.row
                    pos = 'A' + str(ex)
                    position = ws[pos].value
                    return position

