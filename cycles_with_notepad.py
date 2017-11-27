from datetime import datetime
import xlwt  # write excel file

applicator = int(input('input SAP number of applicator: '))
date = datetime.strftime(datetime.now(), "%Y/%m/%d ")
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
print('date is {}'.format(date))
print('next page is: ', page+1)
if c == 'y':
    print('correction is: ', correction)


# <---- to excel file for print
wb = xlwt.Workbook()    # initialization new file to write
ws = wb.add_sheet(str(applicator))    # initialization new file with sheet

def add(x, j, val):
    ws.write(x, j, val)

add(15, 1, date)
add(15, 2, page)
add(15, 4, total_cycles)
if c == 'y':
    add(15, 5, correction)
else:
    print('')

wb.save('apl_print.xls')

# ----> end record excel file for print

# data to write
res = str(applicator) + str('	') + str(date) + str('	') + str(page) + str('	') + str(cycles) + str('	') + str(total_cycles)

# write data
def wrt(res):
    k = open('cycles.txt', 'a')    # name of record file
    k.write(str(res) + '\n')
    k.close()

wrt(res)
