#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      mystav
#
# Created:     27.11.2017
# Copyright:   (c) mystav 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import xlsxwriter

workbook = xlsxwriter.Workbook('rec.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Hello')
worksheet.write_comment('A1', 'This is a comment')

workbook.close()