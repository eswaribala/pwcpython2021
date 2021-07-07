import pymysql

class DBTest:
    def __init__(self):
        self.conn=pymysql.connect(host="localhost",user="root",
                   passwd="vignesh",
                   db="pwcdb")

    def addProduct(self, data):

        cursor = self.conn.cursor();
        print("Cursor ready...");
        try:
            cursor.execute("""insert into product values 
        ('%d','%s','%s','%d')""" % (data[0], data[1], data[2],data[3]));
            # cursor.execute(query);
            self.conn.commit()
        except pymysql.Error as e:
            print("Exception occurred", e)
            self.conn.rollback()
        finally:
            cursor.close();
            self.conn.close();

dbTest=DBTest()
data=[2423,'Mouse','2020-1-2',1500]
dbTest.addProduct(data)