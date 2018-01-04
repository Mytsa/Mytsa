# -*- coding: utf-8 -*-

from openpyxl import *
from datetime import datetime

class Message():
    def __init__(self):
        self.file_name = file_name
        self.date = datetime.strftime(datetime.now(), "%d/%m/%Y")
        self.time = datetime.strftime(datetime.now(), "%H:%M")
        self.per_number = per_number
        self.defect = defect
        self.sap_eq = sap_eq
        self.typ_eq = type_eq
        self.fault = fault
        self.counter = counter


    def write(self):
        # write data intro/to file

        wrfile = load_workbook('{}.xlsx'.format(self.file_name))

        # index coordinate
        a = str('A') + str(x)
        b = str('B') + str(x)
        c = str('C') + str(x)
        d = str('D') + str(x)
        e = str('E') + str(x)
        f = str('F') + str(x)
        g = str('G') + str(x)
        h = str('H') + str(x)

        # write data
        sheet = wrfile.get_sheet_by_name('')

        sheet[a] = (self.date)
        sheet[b] = (self.time)
        sheet[c] = (self.per_number)
        sheet[d] = (self.defect)
        sheet[e] = (self.sap_eq)
        sheet[f] = (self.typ_eq)
        sheet[g] = (self.fault)
        sheet[h] = (self.counter)

        wrfile.save('{}.xlsx'.format(self.file_name))


    def print_mes(self):
        os.startfile('{}.xlsx'.format(self.file_name), "print")  # write correct address, file name
