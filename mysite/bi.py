#-*- coding: utf-8 -*-
import sqlite3, xlrd, decimal
conn = sqlite3.connect('dev.db')
c = conn.cursor()
workbook = xlrd.open_workbook('15.2.xlsx')
worksheet = workbook.sheet_by_index(0)
num_rows = worksheet.nrows
j = 216
for i in range(1,num_rows):
    row_val = worksheet.row_values(i)
    book_name = row_val[4]
    author = row_val[7]
    department = row_val[3]
#    print row_val[9]
    if(type(row_val[9]) is float):
	price = int(row_val[9])
    else:
	continue
    e = 1
    if not author:
	continue
    query = "INSERT INTO mypage_book_list(book_id, department, book_name, author, price, edition) VALUES (%d, '%s', '%s', '%s', %d, %d)" % (j, department, book_name, author, price, 1)
    c.execute(query)
    j = j + 1
    print j
conn.commit()
conn.close()

