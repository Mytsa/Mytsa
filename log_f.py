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
        wb = load_workbook('eq_log/eq_file/{}.xlsx'.format(sap_eq1))
        ws = wb['main']
        # find last mark row, for new data place
        mark = '**'
        for row in ws:
            for cell in row:
                if cell.value == mark:
                    ex = cell.row
                    # print(ex)
                    return ex

    def te(type_eq):
        if type_eq == 'Аплікатор':
            type_eq_m = 'applicator'
        elif type_eq == 'Komax Alpha 355 / 355 S':
            type_eq_m = 'komax'
        elif type_eq == 'Komax Gamma 333 PC':
            type_eq_m = 'komax'
        elif type_eq == 'Schunk / Stapla ультразвукова зварка':
            type_eq_m = 'schunk'
        else:
            type_eq_m = 'other'
        return type_eq_m


    def markl(type_eq_m):
        w = load_workbook('eq_log/general equipment log.xlsx')
        sheet = str(type_eq_m)
        ws = w[sheet]
        # find last mark row, for new data place
        mark = '**'
        for row in ws:
            for cell in row:
                if cell.value == mark:
                    ex_log = cell.row
                    # print(ex_log)
                    return ex_log

    def filtr(type_eq):
        if type_eq == 'Аплікатор':
            f = str('B25')
        elif type_eq == 'Komax Alpha 355 / 355 S':
            f = str('B26')
        elif type_eq == 'Komax Gamma 333 PC':
            f = str('B27')
        elif type_eq == 'Schunk / Stapla ультразвукова зварка':
            f = str('B28')
        elif type_eq == 'Кабельбіндеровий пістолет':
            f = str('H25')
        elif type_eq == 'Raychem / Raychem TE':
            f = str('H26')
        elif type_eq == 'Komax Twist BT 188 t / BT 188':
            f = str('H27')
        elif type_eq == 'Kabateck / Ondal':
            f = str('H28')
        else:
            f = str('B29')
        return f

    def type(sap_eq):
        sap_eq1 = '8000' + str(sap_eq)
        wb = load_workbook('eq_log/eq_file/{}.xlsx'.format(sap_eq1))  # search file by number
        ws = wb['main']
        pos = str('G2')  # take type of equipment
        type_eq = str(ws[pos].value)

        return type_eq

