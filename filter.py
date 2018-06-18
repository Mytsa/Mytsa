# -*- coding: utf-8 -*-
# write and read excel files with check the existence of the file

from openpyxl import *
from f_w_r import *

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












