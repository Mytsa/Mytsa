# -*- coding: utf-8 -*-
# write and read excel files with check the existence of the file

from openpyxl import *


def open_file(name, sheet):
    wb = load_workbook('files/{}.xlsx'.format(name))
    ws = wb[sheet]
    return ws
#<!--- if you need kniw about file at open moment

    # try:
    #     wb = load_workbook('files/{}.xlsx'.format(name))
    #     ws = wb[sheet]
    #     return ws
    # except FileNotFoundError:
    #     print('file not find')
#-------------!>

def find_row(name, sheet, mark):
    try:
        # open_file(name, sheet):
        for row in open_file(name, sheet):
            for cell in row:
                if cell.value == mark:
                    ex = cell.row
                    print(ex)
                    return ex
    except FileNotFoundError:    # if you work with filter in def open_file - use this error "FileNotFoundError:"
        message = 'file not find, please create file or check you data input'
        print(message)

#<!-------- block for check open file action

# mark = 'Gamma 1 (8_1235)'
# name = 'log1'
# sheet = 'main'
# find_row(name, sheet, mark)

#------------------!>

