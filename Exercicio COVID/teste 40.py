import xlrd

loc = ("Dados_CEP_MRJ_covid_19.csv")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

print(sheet.cell_value(0, 0))
