import sqlite3
import csv
def main():
    con = sqlite3.connect("customers_db.db")
    cur = con.cursor()
    
    
    sql  = """INSERT INTO customers_tbl(first_name,last_name,email,gender,ip_address,iban)
    VALUES (?,?,?,?,?,?)"""
    
    with open('MOCK_DATA.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            del row['id']
            all_data = list(row.values())
            cur.execute(sql,all_data)
            # print(row.values())
    
    con.commit()
    con.close()

if __name__=='__main__':
    main()
