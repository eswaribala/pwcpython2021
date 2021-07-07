import pymysql

class DBTest:
    def __init__(self):
        self.conn=pymysql.connect(host="localhost",user="root",
                   passwd="vignesh",
                   db="pwcdb")



dbTest=DBTest()
