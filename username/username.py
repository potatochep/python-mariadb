# connect with test database
import pymysql

conn = pymysql.connect(
        user="root",
        password="rla538363",
        host="localhost",
        port=3306,
        database="test"
    )

cur = conn.cursor()       

sql = "SELECT * FROM USER_TB" 
cur.execute(sql)

resultset = cur.fetchall()
print(resultset)