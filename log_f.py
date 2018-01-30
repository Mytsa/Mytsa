# -*- coding: utf-8 -*-
from openpyxl import *
from datetime import datetime
# import main


class Excel(object):
    def __init__(self, defect):

        # self.date = datetime.strftime(datetime.now(), "%d/%m/%Y")
        # self.defect = main.MyWin.action(defect)
        self.defect = defect
        # self.sap_eq1 = sap_eq1
        # self.wb = load_workbook('eq_log/{}.xlsx'.format(self.sap_eq1))
        # self.ws = self.wb['main']
        # self.sheet = self.wb.get_sheet_by_name('main')
        # self.per_number = per_number
        # self.counter = counter




    def lf(defect):

# <------------------ this loops is for the present and must be work with data log in future !!!
        if defect == '1':
            df = 'Пошкодження поверхні контакту'
        elif defect == '2':
            df = 'Гострини на розрізі контакту'
        elif defect == '3':
            df = 'Не симетричне / не відповідне закриття ядра'
        elif defect == '4':
            df = 'Пошкодження контакту або його деформація'
        elif defect == '5':
            df = 'Асиметрія контакту'
        elif defect == '6':
            df = 'Зазубрини в місті відрізу контакту'
        elif defect == '7':
            df = 'Пошкодження проводу або ущільнення'
        elif defect == '8':
            df = 'Рекваліфікація / EMPB'
        elif defect == '9':
            df = 'Не вірна довжина проводу'
        elif defect == '10':
            df = 'Не відповідне зварне з’єднання'
        elif defect == '11':
            df = 'Не відповідна сила стягування кабельбіндера'
        elif defect == '12':
            df = 'Не відповідне термоусадження'
        elif defect == '13':
            df = 'Не відповідне скручення проводів'
        elif defect == '14':
            df = 'Не відповідна обмотка з’єднання  '
        elif defect == '15':
            df = 'Тріснута запчастина'
        elif defect == '16':
            df = 'Обладнання не вмикається / не продукує виріб'
        elif defect == '17':
            df = 'інше'
        else:
            df = 'не вірно визначений дефект'

        print(df)
        return df
# ------------------>
#     def wrt(self):
#
#     # write data to eq_log
#
#         # find last mark row, for new data place
#         mark = '**'
#         for row in self.ws:
#             for cell in row:
#                 if cell.value == mark:
#                     ex = cell.row
#                     break
#
#         # index coordinate to equipment file
#         a = str('A') + str(ex)
#         b = str('B') + str(ex)
#         c = str('C') + str(ex)
#         d = str('D') + str(ex)
#         a1 = str('A') + str(ex + 1)  # for mark symbols
#
#         # write data to equipment file
#
#         self.sheet[a] = self.date
#         self.sheet[b] = self.per_number
#         self.sheet[c] = lf(self)
#         self.sheet[d] = self.counter
#         self.sheet[a1] = '**'
#
#         self.wb.save('eq_log/{}.xlsx'.format(self.sap_eq1))
