#!/usr/bin/python
#-*- coding: utf-8 -*-
import book_information as bi
import xlrd

xl_workbook = xlrd.open_workbook("15-1.xlsx", encoding_override='latin-1')
sheet_names = xl_workbook.sheet_names()
print('Sheet Names', sheet_names)
xl_sheet = xl_workbook.sheet_by_name(sheet_names[0])
xl_sheet = xl_workbook.sheet_by_index(0)
num_rows = xl_sheet.nrows

print num_rows

#bi.create_tables_book_information()

a = 422
for i in range(1,num_rows):
    cell_obj = xl_sheet.cell(i,6)
    cell_obj_price = xl_sheet.cell(i,9)
    cell_obj = str(cell_obj)
    cell_obj = cell_obj.replace('text:u', '')
    cell_obj = cell_obj.replace('\'','')
    cell_obj_price = str(cell_obj_price)
    cell_obj_price = cell_obj_price.replace('number:','')
    cell_obj_price = cell_obj_price.replace('.0','')
    try:
	cell_obj_price = int(cell_obj_price)
    except:
	continue
    if cell_obj == ' ' or cell_obj_price == 0:
	continue
    else:
	if cell_obj.find("\\") == 0:
	    continue
	else:
#	print cell_obj_price
	    bi.insert_tables_book_information(a,cell_obj,cell_obj_price)
	    print "book_number = %d, book_name = %s, price = %d registered" % (a,cell_obj,cell_obj_price)
    a = a + 1
