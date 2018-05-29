import xlsxwriter
import os
import xlrd    
import time 
from xlsxwriter.utility import xl_rowcol_to_cell

def findCell(sh, searchedValue):
    for row in range(sh.nrows):
        for col in range(sh.ncols):
            myCell = sh.cell(row, col)
            if myCell.value == searchedValue:
                return xl_rowcol_to_cell(row, col)
    return -1

myName = 'hello.xlsx'
wbk = xlsxwriter.Workbook(myName)
wks = wbk.add_worksheet()
i = -1

for x in range(1, 1000, 11):
    i+=1
    cella = xl_rowcol_to_cell(i, 0) #0,0 is A1!
    cellb = xl_rowcol_to_cell(i, 1)
    cellc = xl_rowcol_to_cell(i, 2)
    wks.write(cella,x)
    wks.write(cellb,x*3)
    wks.write(cellc,x*4.5)
myPath= os.getcwd()+"\\"+myName

searchedValue = 300
for sh in xlrd.open_workbook(myPath).sheets():  
    print(findCell(sh, searchedValue))
input('Press ENTER to exit')
