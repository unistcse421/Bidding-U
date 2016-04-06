#!/usr/bin/python
import MySQLdb as mdb

def create_auction_list():
	db = mdb.connect("localhost", "root", "wndud625", "db")
	cursor = db.cursor()
	cursor.execute("CREATE TABLE Auction_List(auction_id INT PRIMARY KEY AUTO_INCREMENT, item_id INT, due_date VARCHAR(10) NOT NULL, current_price INT NOT NULL)")
	cursor.execute("ALTER TABLE Auction_List AUTO_INCREMENT = 1")
	cursor.close()
	db.close()


def insert_auction_list(item_id):
	query1 = "SELECT Reserved_Price FROM Item_Information WHERE item_id=Item_ID"
	query2 = "INSERT INTO Auction_List VALUES"

	db = mdb.connect("localhost", "root", "wndud625", "db")
	cursor = db.cursor()

	cursor.execute(query1)
	c = cursor.fetchone()
	while c is not None:
		cprice = c[0]
		c = cursor.fetchone()

	due_date = 20150607
	args = "(%d, %d, '%s', %d);" % (0, item_id, due_date, cprice)


	cursor.execute(query2 + args)
	db.commit()
	cursor.close()
	db.close()

create_auction_list()
insert_auction_list(1)

