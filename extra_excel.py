# sheet1 = wb['flow handoff']
# sheet2 = wb["mpstat"]
# print(sheet2.max_row)
# cell1 = sheet1.cell(2,1)
# cell2 = sheet2.cell(3,1)
# print(cell1.value)
# print(cell2.value)
# if(cell1.value == cell2.value):
#     print("both value matched")

# sheet = wb["handoff"]
# # cell = sheet.cell(2900,1)
# # print(cell.value)
# # if(cell.value == None):
# #     print('empty')
# #     sheet.delete_rows(2900,1)
# #
# # wb.save("data_from_gw.xlsx")
#
#
# for row in range(2, sheet.max_row+1):
#     cell = sheet.cell(row,1)
#     if(cell.value == None):
#         sheet.delete_rows(row,1)
#     else:
#         pass
#
# wb.save('data1.xlsx')

# def delete_rows(workbook, sheet_name):
#     sheet = workbook[sheet_name]
#     print(sheet_name)
#     print(sheet.max_row)
#     blank_rows = 0
#     for row in range(2, sheet.max_row + 1):
#         #print(row)
#         cell1 = sheet.cell(row,1)
#         cell2 = sheet.cell(row,2)
#         if (cell1.value == None or cell2.value == None):
#             blank_rows += 1
#             sheet.delete_rows(row,1)
#     print(f'Blank rows count: {blank_rows}')
#     stat_msg = "Deleted empty rows"
#
#     return stat_msg


# cell1 = sheet1.cell(2, 1)
# cell2 = sheet2.cell(2, 1)
# if cell1.value == cell2.value:
#     new_cell = sheet2.cell(2, 2)
#     append_cell = sheet1.cell(2, 5)
#     append_cell.value = new_cell.value





# print(cell_list[0])
        # print(cell_list[1])

        # for r1, r2 in itertools.zip_longest(range(2, 4), range(2, 4)):
        #     # print(r1)
        #     # print(r2)
        #     cell1 = sheet1.cell(r1, 1)
        #     cell2 = sheet2.cell(r2, 1)
        #     if cell1.value == cell2.value:
        #         new_cell = sheet2.cell(r2, 2)
        #         append_cell = sheet1.cell(r1, 5)
        #         append_cell.value = new_cell.value