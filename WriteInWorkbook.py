import xlsxwriter
import datetime

workbook = xlsxwriter.Workbook('myxls.xlsx')
starting = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
worksheet = workbook.add_worksheet()
worksheet.write('A1',starting)
