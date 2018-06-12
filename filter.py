# -*- coding: utf-8 -*-
# write and read excel files with check the existence of the file

from openpyxl import *
from f_w_r import *

def shift_id(per_number):    # return name of shift by person number
    name = personfile   # file with data about person in shift
    sheet = 'main'
    mark = per_number
    sft = find_data_in_row(name, sheet, mark)
    return sft


# def type_eq(type_eq):
#     if type_eq == 'Аплікатор':
#         type_eq_m = 'applicator'
#     elif type_eq == 'Komax Alpha 355 / 355 S':
#         type_eq_m = 'komax'
#     elif type_eq == 'Komax Gamma 333 PC':
#         type_eq_m = 'komax'
#     elif type_eq == 'Schunk / Stapla ультразвукова зварка':
#         type_eq_m = 'schunk'
#     else:
#         type_eq_m = 'other'
#     return type_eq_m
#
#     sap_eq1 = '*8000' + str(sap_eq)
#     w = load_workbook('list_eq.xlsx')
#     ws = w['list_eq']
#     # find last mark row, for new data place
#     mark = sap_eq1
#     for row in ws:
#         for cell in row:
#             if cell.value == mark:
#                 ex_list = cell.row
#
#     pos = 'C' + str(ex_list)
#     type_eq = ws[pos].value
#     return type_eq
