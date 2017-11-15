import xlrd  # read excel file
import xlwt  # write excel file

import comparison_line
import sum_of_number    # need number of last row with number for range


rb = xlrd.open_workbook('20171102.xls', formatting_info=True)   # order list from SAP - fresh
sheet_rb = rb.sheet_by_index(0)    # choice active sheet

ws = xlrd.open_workbook('zakazu-20170721.xls', formatting_info=True)    # open order list
sheet_ws = ws.sheet_by_index(0)    # choice active sheet

wb = xlwt.Workbook()    # initialization new file to write
ws = wb.add_sheet('sheet')  # initialization new file with sheet



ws.write(i, j, val) # (i, j)-index to write data, val is data to write




wb.save('new_order.xls')    # save new file
