#pip install XlsxWriter
import xlsxwriter
from xlsxwriter.utility import xl_rowcol_to_cell

wbk = xlsxwriter.Workbook('hello.xlsx')
wks = wbk.add_worksheet()
wks.write('A1', 'Hello world')

wks2 = wbk.add_worksheet()
i = -1

for x in range(1, 1000, 11):
	i+=1
	cella = xl_rowcol_to_cell(i, 0)	#0,0 is A1!
	cellb = xl_rowcol_to_cell(i, 1)
	cellc = xl_rowcol_to_cell(i, 2)
	print cella
	wks2.write(cella,x)
	wks2.write(cellb,x*3)
	wks2.write(cellc,x*4.5)
wbk.close()
