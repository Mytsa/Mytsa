# -*- coding: utf-8 -*-
# write and read excel files with check the existence of the file

from openpyxl import *
from f_w_r import find_row_fls

def shift_id(per_number):    # return name of shift by person number
    wb = load_workbook('files\personfile.xlsx')
    ws = wb['main']
    mark = str('*') + str(per_number)
    sheet = 'main'
    name = 'personfile'

    ex = find_row_fls(name, sheet, mark)
    pos = str('D') + str(ex)

    sft = (ws[pos].value)
    # print(sft)
    return sft


def check_apl(sap_eq):    # check equipment is applicator
    sap_eq1 = '*8000' + str(sap_eq)
    w = load_workbook('files\list_apl.xlsx')
    ws = w['main']
    mark = sap_eq1
    for row in ws:
        for cell in row:
            if cell.value == mark:
                ex_list = cell.row

    pos = 'C' + str(ex_list)
    type_eq = ws[pos].value
    # print(type_eq)
    return type_eq
#
#
# def apl_check(apl):    # not working now
#     if apl != '':
#         b = len(apl)
#         if apl.isdigit() is (False or b != 4):
#             mes = 'write correct applicator number'
#         else:
#             apl = '8000' + str(apl)
#     else:
#         apl = ''

# def four_num(num):    # check input number by digitals and for len in list by 4 numbers
#     b = len(num)
#     if b == 4:
#
#         try:
#             num = int(num)
#         except ValueError:
#             a = 'enter numbers'
#             return a
#
#     else:
#         # a = 'enter 4 number'
#         return False














