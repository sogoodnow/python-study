import xlrd

wkb = xlrd.open_workbook('test.xlsx')
sheet_names= wkb.sheet_names()
sql = ""
for sheet_name in sheet_names:
    # print(sheet_name)
    sheet = wkb.sheet_by_name(sheet_name)
    # print(sheet.col_values(0))
    keys = sheet.col_values(0)
    vals = ["item['"+x+"']" for x in keys]
    # print(vals)
    sql = "("+",".join(keys)+")"+"values("+"'%s',"*(len(keys)-1)+"'%s'"+")%("+",".join(vals)+")"
print(sql)