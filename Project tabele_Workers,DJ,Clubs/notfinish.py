import pymysql

def connect():
    return pymysql.connector.connect(
        host="localhost",
        user="root",
    )
