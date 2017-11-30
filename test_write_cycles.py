#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mystav
#
# Created:     27.11.2017
# Copyright:   (c) mystav 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
import xlrd  # read excel file
import xlwt  # write excel file
import xlsxwriter    # write excel file new libory
from datetime import datetime

applicator = int(input('input SAP number of applicator: '))
date = datetime.strftime(datetime.now(), "%Y/%m/%d ")

page = int(input('input page number of card: '))
cycles = int(input('input cycles: '))
c = input('has a counter (y/no): ')

if c is 'y':
    counter = int(input('input counter data: '))
    correction = counter - cycles
    total_cycles = counter
    print('correction is: {} '.format(correction))
else:
    total_cycles = int(input('input total cycles: '))

wb = xlwt.Workbook()    # initialization new file to write
ws = wb.add_sheet(datetime.strftime(datetime.now(), "%Y"))    # initialization new file with sheet


# open file
rb = xlrd.open_workbook('apl_counter.xls', formatting_info=True)
# choice active sheet
sheet = rb.sheet_by_index(0)
i = 0
while sheet.row_values(i)[0] != '**':  # find last row before mark --> **
    x = i + 1
    i += 1
    # print(x)


# ---- work with new libory for write data in cell ---->

# Create an new Excel file and add a worksheet.
#workbook = xlsxwriter.Workbook('merge1.xlsx')
#worksheet = workbook.add_worksheet()

# Increase the cell size of the merged cells to highlight the formatting.
#worksheet.set_column('B:D', 12)
#worksheet.set_row(3, 30)

workbook = xlsxwriter.Workbook('apl_counter.xls')
worksheet = workbook.worksheet((datetime.now(), "%Y"))

worksheet.set_cell('A1', val)

worksheet.write_rich_string('A1', val)

workbook.close()

#    ---- end ---->


# clean all file and write new data - need decision
#def add(x, j, val):
#    ws.write(x, j, val)

#add(x, 0, applicator)
#add(x, 1, date)
#add(x, 2, page)
#add(x, 3, cycles)
#add(x, 4, total_cycles)
#ws.write(x + 1, 0, "**")  # mark last row with symbol --> **

#wb.save('apl_counter.xls')

