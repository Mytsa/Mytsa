# -*- coding: utf-8 -*-
#import openpyxl
from openpyxl import *
from datetime import datetime

applicator = int(input('input SAP number of applicator: '))
date = datetime.strftime(datetime.now(), "%Y/%m/%d")
page = int(input('input page number of card: '))
cycles = int(input('input cycles: '))
old_cycles = int(input('input cycles previous card: '))
c = input('has a counter (y/no): ')

if c is 'y':
    counter = int(input('input counter data: '))
    correction = counter - (cycles + old_cycles)
    total_cycles = counter
    # print('correction is: {} '.format(correction))
else:
    total_cycles = cycles + old_cycles

# output block
print("total cycles is {}".format(total_cycles))
print("sum of cycles in this cart is {}".format(old_cycles + cycles))
# print('date is {}'.format(date))
print('next page is: ', page+1)
if c == 'y':
    print('correction is: ', correction)

wb = load_workbook(filename='counter_ver.1.xlsx', read_only=True)
ws = wb['2017']

mark = "**"  # word to search
for row in ws:
    for cell in row:
        if cell.value == mark:
            x = cell.row  # find last mark row
            break

wrfile = load_workbook('counter_ver.1.xlsx')

a = str('A') + str(x)
b = str('B') + str(x)
c = str('C') + str(x)
d = str('D') + str(x)
e = str('E') + str(x)
a1 = str('A') + str(x + 1)

sheet = wrfile.get_sheet_by_name('2017')
sheet[a] = applicator
sheet[b] = date
sheet[c] = page
sheet[d] = cycles
sheet[e] = total_cycles
sheet[a1] = '**'

wrfile.save('counter_ver.1.xlsx')



