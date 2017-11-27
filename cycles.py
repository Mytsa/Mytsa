# -*- coding: utf-8 -*-
import xlrd  # read excel file
import xlwt  # write excel file
import xlsxwriter
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

# wb = xlwt.Workbook()    # initialization new file to write
# ws = wb.add_sheet(datetime.strftime(datetime.now(), "%Y"))    # initialization new file with sheet
#
#
# # open file
# rb = xlrd.open_workbook('apl_counter.xls', formatting_info=True)
# # choice active sheet
# sheet = rb.sheet_by_index(0)
# i = 0
# while sheet.row_values(i)[0] != '**':  # find last row before mark --> **
#     x = i + 1
#     i += 1
#     # print(x)

# ---- new shanche ---->


# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('apl_counter.xls')
worksheet = workbook.add_worksheet('2018')

# Some data we want to write to the worksheet.
# expenses = (
#     ['Rent', 1000],
#     ['Gas',   100],
#     ['Food',  300],
#     ['Gym',    50],
# )

# Start from the first cell. Rows and columns are zero indexed.
# row = 0
# col = 0

# Iterate over the data and write it out row by row.

worksheet.write(25, 0, applicator)
worksheet.write(25, 1, date)
worksheet.write(25, 2, page)
worksheet.write(25, 3, cycles)
worksheet.write(25, 4, total_cycles)
worksheet.write(26, 0, '**')


# Write a total using a formula.
# worksheet.write(row, 0, 'Total')
# worksheet.write(row, 1, '=SUM(B1:B4)')

workbook.close()


#  ---- end ---->

# clean all file and write new data - need decision

# def add(x, j, val):
#     ws.write(x, j, val)
#
# add(x, 0, applicator)
# add(x, 1, date)
# add(x, 2, page)
# add(x, 3, cycles)
# add(x, 4, total_cycles)
# ws.write(x + 1, 0, "**")  # mark last row with symbol --> **
#
# wb.save('apl_counter.xls')
