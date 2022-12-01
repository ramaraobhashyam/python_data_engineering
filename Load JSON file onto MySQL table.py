#Python script to truncate target table and load json file from local file system to mysql table
import mysql.connector as mysql
import MySQLdb
import json

file = "C:\\temp\\abc.json"
print(file)
with open(file,'r') as f:
    json_data= json.load(f) 
db = MySQLdb.connect(host='',user='', passwd='', db='',ssl='True')
 
cursor = db.cursor()
 
cursor.execute("TRUNCATE TABLE table_name;")
db.commit()
 
transaction_sql = (
    "insert into table_name"
    "(date_timestamp, date_id, tid, type, amount, price)"
    "values (%(date)s, from_unixtime(%(date)s), %(tid)s, %(type)s, %(amount)s, %(price)s)")
 
for transaction in json_data:
   cursor.execute(transaction_sql, transaction)
 
db.commit()
 
cursor.close()
db.close()