# from openpyxl import load_workbook
# wb2 = load_workbook('files/eq_files/80001841.xlsx')
# print(wb2.get_sheet_names('s_p'))

from openpyxl import *


def type(sap_eq):
    sap_eq1 = '*8000' + str(sap_eq)
    w = load_workbook('files\list_apl.xlsx')
    ws = w['main']
    # find last mark row, for new data place
    mark = sap_eq1
    for row in ws:
        for cell in row:
            if cell.value == mark:
                ex_list = cell.row

    pos = 'C' + str(ex_list)
    type_eq = ws[pos].value
    print(type_eq)
    return type_eq

type('0571')
# from f_w_r import *

# def shift_id(mark):    # return name of shift by person number
#     # mark = '3070'
#     wb = load_workbook('files\personfile.xlsx')
#     ws = wb['main']
#     for row in ws:
#         for cell in row:
#             if cell.value == mark:
#                 ex = cell.row
#                 pos = ex
#                 print(pos)
#
# a = '*3070'
# print(shift_id(a))
#
# per_number = '*3070'

# def shift_id(per_number):    # return name of shift by person number
#     name = 'personfile'   # file with data about person in shift
#     sheet = 'main'
#     mark = '*3070'
#     sft = find_data_in_row(name, sheet, mark)
#     print(sft)
#
#     return sft
# shift_id(per_number)


# wb = load_workbook('files\personfile.xlsx')
# ws = wb['main']
# mark = '*3070'
# sheet = 'main'
# name = 'personfile'
#
# ex = find_row_fls(name, sheet, mark)
# pos = str('D') + str(ex)
#
# print(ws[pos].value)
# eq_num = input('imnput number : ')
#
# a = eq_num.isdigit()
# print(a)
# num = str(num)
# if eq_num == int(eq_num):
#     print('write correct equipment number')
#
# else:
#     print('good')

#
# if type_fix == 'механічне налаштування':
#     # add to number applicator 8000...
#     if apl == '':
#         self.ui.message.setText('write correct applicator number')
#     else:
#         apl = '8000' + str(apl)
#         eq_number = apl
#         write_eq_file(eq_number, self.date, per_number, type_fix, notice)
# elif type_fix == 'заміна запчастин':
#     if apl == '':
#         self.ui.message.setText('write correct applicator number')
#     else:
#         apl = '8000' + str(apl)
#         eq_number = apl
#         write_eq_file(eq_number, self.date, per_number, type_fix, notice)
#
# elif type_fix == 'налаштування симетричності розрізу':
#     if apl == '':
#         self.ui.message.setText('write correct applicator number')
#     else:
#         apl = '8000' + str(apl)
#         eq_number = apl
#         write_eq_file(eq_number, self.date, per_number, type_fix, notice)