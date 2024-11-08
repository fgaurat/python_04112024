import sqlite3
from Customer import Customer

class CustomerDAO:
    
    def __init__(self,db_file):
        self.__con = sqlite3.connect(db_file)

    def find_all(self):
        customers = []
        sql = "SELECT * FROM customers_tbl"
        cur = self.__con.cursor()
        res = cur.execute(sql)
        for data in res:
            c = Customer(*data)
            customers.append(c)
            yield c
        # return customers
    
    
    def __del__(self):
        self.__con.close() 