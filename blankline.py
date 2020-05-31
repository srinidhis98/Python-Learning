import openpyxl
flag=False
wb = openpyxl.load_workbook('new_dataa2.xlsx')
sheet = wb['Sheet1']
for row in sheet.iter_rows():
    for cell in row:
        if cell.value == 'D':
            sheet.insert_rows(cell.row, amount=1)
            flag=True
            break
    if flag:break
    else:
        continue
wb.save("test.xlsx")