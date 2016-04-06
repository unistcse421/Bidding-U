#!/usr/bin/python


def create_tables_book_information():
    import MySQLdb
    db = MySQLdb.connect("localhost", "root", "dbproject", "dbproject")
    cursor = db.cursor()
    try:
        cursor.execute("CREATE TABLE Book_List(book_number int(5), book_name varchar(50), price int(7), PRIMARY KEY(book_number, book_name));")
    except:
	print "There already exists the table"
    db.close()

def insert_tables_book_information(book_number, book_name, price):
    import MySQLdb
    db = MySQLdb.connect("localhost", "root", "dbproject", "dbproject")
    cursor = db.cursor()
    instruction = "(%d, '%s', %d);" % (book_number, book_name, price)    
    try:
	cursor.execute("""INSERT INTO Book_List VALUES""" + instruction)
	db.commit()
    except:
	print "There exists same Book_number or Book_name"
        db.rollback()
    db.close()

