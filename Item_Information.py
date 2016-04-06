import MySQLdb

def Create_Item_Information_Table():
	Database = MySQLdb.connect("localhost", "root", "20121436", "dbproject")
	cursor = Database.cursor()
	cursor.execute("CREATE TABLE Item_Information(Item_ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL, User_ID INT, Reserved_Price INT, State VARCHAR(10), Book_Number INT)")
	cursor.execute("ALTER TABLE Item_Information AUTO_INCREMENT = 1")
	Database.close()


def Insert_Item_Information_Table(User_ID, Reserved_Price , State, Book_Number):
	query1 = "SELECT book_number FROM Book_List WHERE " #check 
	Database = MySQLdb.connect("localhost", "root", "20121436", "dbproject")
	cursor = Database.cursor()
	Arg = "(%d, %d, %d, '%s', %d);" %(0, User_ID, Reserved_Price, State, Book_Number)		
	cursor.execute("INSERT INTO Item_Information values"+Arg)
	Database.commit()
	Database.close()                                           #duplicate Item ID check







#Create_Item_Information_Table()
Insert_Item_Information_Table(201221436, 15000, 'A', 1003)
