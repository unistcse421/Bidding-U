#!/usr/bin/python
import MySQLdb as mdb

def creat_candidate_list():
	db = mdb.connect("localhost", "root", "wndud625", "db")
	cursor = db.cursor()
	cursor.execute("CREATE TABLE Candidate_List(user_id INT PRIMARY KEY NOT NULL, item_id INT NOT NULL, suggest_price INT NOT NULL, suggest_time VARCHAR(10) NOT NULL)")
	db.close()


#def insert_candidate_list(user_id, item_id):
#	query1 = "INSERT INTO Candidate_List VALUES"

#	db = mdb.connect("localhost", "root", "wndud625", "db")
#	cursor = db.cursor()
	
#	args = "(%d, %d, %d, '%s');" %(user_id, item_id, suggest_price, suggest_time)
#	cursor.execute(query1, args)
#	db.close()


creat_candidate_list()
#insert_candidate_list(1,1)
