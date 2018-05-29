import xlwings as xw

bookName = r'C:\somePath\hello.xlsx'
sheetName = 'Sheet1'

wb = xw.Book(bookName)
sht = wb.sheets[sheetName]

myCell = wb.sheets[sheetName].api.UsedRange.Find('test')
print('---------------')
print (myCell.address)
input()
