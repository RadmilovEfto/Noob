import pymysql


class Db :
    def __init__(self):
        self.connection = pymysql.connect(
            host = "localhost",
            user = "root",
            password = 'radmil0v',
            database =  "oop_2"

        )