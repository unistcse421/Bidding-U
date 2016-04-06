import MySQLdb

def Create_User_Information_Table():
	Database = MySQLdb.connect("localhost", "root", "20121436", "dbproject")
	cursor = Database.cursor()
	cursor.execute("CREATE TABLE User_Information(User_ID INT PRIMARY KEY, Name VARCHAR(50), Phone_Number VARCHAR(20), Password VARCHAR(20), level INT)")
	Database.close()

def Insert_User_Information_Table(User_ID, Name, Phone_Number, Password):
	Database = MySQLdb.connect("localhost", "root", "20121436", "dbproject")
	cursor = Database.cursor()
	Arg = "(%d, '%s', '%s', '%s', %d);" %(User_ID, Name, Phone_Number, Password, 5)	
	
	cursor.execute("INSERT INTO User_Information values"+Arg)
	Database.commit()
	Database.close()                                           #duplicate ID check

	




#Create_User_Information_Table()
Insert_User_Information_Table(20121222, 'leekanggeun', '010-2303-0332', '1234')



