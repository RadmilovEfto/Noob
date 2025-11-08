

import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="radmil0v",
    database="python17")

if connection.open :
    print("Connected")
else :
    print("not")


