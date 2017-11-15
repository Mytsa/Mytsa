import xlrd  # read excel file
import xlwt  # write excel file

# open file
rb = xlrd.open_workbook('20171102.xls', formatting_info=True)

# choice active sheet
sheet = rb.sheet_by_index(0)

# initialization new file to write
wb = xlwt.Workbook()
# initialization new file with sheet
ws = wb.add_sheet('sheet')

# get info from cell and write to new file
for i in range(0, 74):  # end of range need decision
    for j in range(0, 3):
        val = sheet.row_values(i)[j]

        print(val)
        # write info to new file
        ws.write(i, j, val)
        j += 1
    i += 1

# save new file
wb.save('rec.xls')
