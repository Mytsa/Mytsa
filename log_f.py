# -*- coding: utf-8 -*-
from openpyxl import *

class Log:

    def lf(defect):
# <------------------ this loops is for the present and must be work with data log in future ! -----> MAYBE!!!
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

        # print(df)
        return df
# ------------------>

    def mark(sap_eq1):
        wb = load_workbook('eq_log/{}.xlsx'.format(sap_eq1))
        ws = wb['main']
        # find last mark row, for new data place
        mark = '**'
        for row in ws:
            for cell in row:
                if cell.value == mark:
                    ex = cell.row
                    # print(ex)
                    return ex

    def num_check(num, counter):
        if num < counter:
            a = 'ok'
            return a
        else:
            b = 'counter not correct'
            return b

