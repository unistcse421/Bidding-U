#!/usr/bin/python

import MySQLdb

db = MySQLdb.connect("localhost", "root", "wndud625", "TESTDB")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

Data = cursor.fetchone()

print "Database version : %s " % data

db.close()

