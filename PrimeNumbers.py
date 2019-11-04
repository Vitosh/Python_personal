import xlsxwriter
import math

def Main():
    wbk_name = 'vitoshacademy.xlsx'
    wbk = xlsxwriter.Workbook(wbk_name)
    wks = wbk.add_worksheet()
    wks.set_column(0,9,3.22)
    cell_format_default = wbk.add_format({'bold': False, 'font_color': 'black', 'bg_color':'white','align':'center'})
    cell_format_prime = wbk.add_format({'bold': True, 'font_color': 'white', 'bg_color': 'green','align': 'center'})

    for number in range(1, 151):
        if (number % 10 == 0):
            column = 9
            row = number // 10 - 1 
        else:
            row = number // 10
            column = number % 10 - 1        
        
        if is_prime(number):
            wks.write(row,column, number, cell_format_prime)
        else:
            wks.write(row,column, number, cell_format_default)
    wbk.close()

def is_prime(number):
    if number == 1 or number == 2 or number == 3:
        return True
    
    if number < 1:
        return False

    for  i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True
    
if __name__== "__main__":
    Main()
