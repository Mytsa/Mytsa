# -*- coding: utf-8 -*-
# write and read excel files with check the existence of the file

from openpyxl import *

def open_file(name, sheet):
    wb = load_workbook('files\eq_files\{}.xlsx'.format(name))
    ws = wb[sheet]
    return ws
#<!--- if you need know about file at open moment

    # try:
    #     wb = load_workbook('files/{}.xlsx'.format(name))
    #     ws = wb[sheet]
    #     return ws
    # except FileNotFoundError:
    #     mes = ('file not find')
#-------------!>

def find_row(name, sheet, mark):
    try:
        # open_file(name, sheet):
        for row in open_file(name, sheet):
            for cell in row:
                if cell.value == mark:
                    ex = cell.row
                    # print(ex)
                    mes = 'file is find'
                    #print(mes)
                    return ex
    except FileNotFoundError:    # if you work with filter in def open_file - use this error "FileNotFoundError:"
        mes = 'file not find, please create file or check you data input'
        #print(mes)
        return mes

#<!-------- block for check open file action

# mark = 'Gamma 1 (8_1235)'
# name = 'log'
# sheet = 'main'
# find_row(name, sheet, mark)

#------------------!>

def find_row_fls(name, sheet, mark):
    wb = load_workbook('files\{}.xlsx'.format(name))
    ws = wb[sheet]
    for row in ws:
        for cell in row:
            if cell.value == mark:
                ex = cell.row
                return ex


def find_data_in_row(name, sheet, mark):
    ws = open_file(name, sheet)
    pos = find_row(name, sheet, mark)
    num = str(ws[pos].value)
    return num

def write_eq_file(name, mark, date, per_number, data):
    sheet = 's_p'
    ex = find_row(name, sheet, mark)
    w = load_workbook('files\eq_files\{}.xlsx'.format(name))

    a = str('A') + str(ex)
    b = str('B') + str(ex)
    c = str('C') + str(ex)
    a1 = str('A') + str(ex + 1)  # for mark symbols
    # write data to equipment file
    sheet = w.get_sheet_by_name('s_p')
    sheet[a] = date
    sheet[b] = per_number
    sheet[c] = data
    sheet[a1] = '**'    # mark last row for find in new write process

    w.save('files\eq_files\{}.xlsx'.format(name))

def write_sum_and_shift_files(eq_number, date, data):    # need sum of figures in table for creat summary table
    name = 'DownTime_shift.xlsx'
    sheet = 'main'
    mark = eq_number

    ex = find_row_fls(name, sheet, mark)
    w = load_workbook('files\{}.xlsx'.format(name))
    entry_figure = find_data_in_row(name, sheet, mark)

    f_data = int(data) + int(entry_figure)

    a = str('A') + str(ex)
    b = str('B') + str(ex)
    # write data to equipment file
    sheet = w.get_sheet_by_name('main')
    sheet[a] = date
    sheet[b] = f_data

    w.save('files\eq_files\{}.xlsx'.format(name))

def write_log_file(date, shift, eq_number, apl, minutes, data, notice):    # write data to Log file
    name = 'log'
    sheet = 'main'
    mark = '**'

    ex = find_row_fls(name, sheet, mark)
    w = load_workbook('files\{}.xlsx'.format(name))

    a = str('A') + str(ex)
    b = str('B') + str(ex)
    c = str('C') + str(ex)
    d = str('C') + str(ex)
    e = str('E') + str(ex)
    f = str('F') + str(ex)
    g = str('G') + str(ex)
    a1 = str('A') + str(ex + 1)  # for mark symbols

    # write data to equipment file
    sheet = w.get_sheet_by_name(sheet)
    sheet[a] = date
    sheet[b] = shift
    sheet[c] = eq_number
    sheet[d] = apl
    sheet[e] = minutes
    sheet[f] = data
    sheet[g] = notice
    sheet[a1] = '**'    # mark last row for find in new write process

    w.save('files\{}.xlsx'.format(name))
