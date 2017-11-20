# -*- coding: utf-8 -*-
import xlrd  # read excel file
import xlwt  # write excel file
from datetime import datetime

applicator = int(input('input SAP number of applicator: '))
date = datetime.strftime(datetime.now(), "%Y/%m/%d ")

page = int(input('input page number of card: '))
cycles = int(input('input cycles: '))
c = input('has a counter (y/no): ')

if c is 'y':
    counter = int(input('input counter data: '))
else:
    total_cycles = int(input('input total cycles: '))
    counter = total_cycles
correction = counter - total_cycles

wb = xlwt.Workbook()    # initialization new file to write
ws = wb.add_sheet(datetime.strftime(datetime.now(), "%Y"))    # initialization new file with sheet


# open file
rb = xlrd.open_workbook('apl_counter.xls', formatting_info=True)
# choice active sheet
sheet = rb.sheet_by_index(0)
i = 0
while sheet.row_values(i)[0] != '**':
    x = i + 1
    i += 1
    # print(x)




def add(x, j, val):
    ws.write(x, j, val)

add(x, 0, applicator)
add(x, 1, date)
add(x, 2, page)
add(x, 3, cycles)
add(x, 4, total_cycles)
ws.write(x + 1, 0, "**")

wb.save('apl_counter.xls')
