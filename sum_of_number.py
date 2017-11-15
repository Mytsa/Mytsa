# sum of number
import xlrd  # read excel file

class SumNumber():

    ws = xlrd.open_workbook('zakazu-20170721.xls', formatting_info=True)    # open order list
    sheet_ws = ws.sheet_by_index(0)    # choice active sheet

    def sum(self, sheet_ws, x):
        num1 = 0
        for i in range(0, x):    # x is last line with SAP number in file zakazku
            num = sheet_ws.row_values(i)[3]
            num1 = num1 + num
            i += i
            return num1
