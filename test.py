from openpyxl import *

wb = load_workbook(filename='eq1.xlsx', read_only=True)
a = 'eq1'
ws = wb[a]
aa = str(input('input code: '))

mark = aa  # word to search last raw in sheet
for row in ws:
    for cell in row:
        if cell.value == mark:
            x = cell.row  # find last mark row, for data input place
            print(x)
            break
