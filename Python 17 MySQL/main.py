

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

cursor = connection.cursor()

cursor.execute("INSERT INTO users (usarname, password, ages) VALUES ('Toma', 'aaass',35) ")
connection.commit()
