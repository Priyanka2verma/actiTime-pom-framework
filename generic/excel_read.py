from xlrd import *

def read_data():
    wb = open_workbook("C:\\Users\\Hp\\PycharmProjects\\ActiTimeFramework_E20\\excel_files\\data.xlsx")
    sh = wb.sheet_by_name("Sheet1")
    data = sh.row_values(1)
    return data

