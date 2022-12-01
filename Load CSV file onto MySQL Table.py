#Python script to import csv file from local file system to mysql table
import MySQLdb
import csv

try:
    print("Start csv file load on to MySQL table")
    file = "C:\\temp\\abc.csv"
    #mysql connection
    connection = MySQLdb.connect(host='',user='', passwd='', db='',ssl='True')
    cursor = connection.cursor()
    csv_data = csv.reader(open(file))
    next(csv_data)
    for row in csv_data:
        cursor.execute('INSERT INTO table_name(id ,name) VALUES(%s, %s)',row)

    connection.commit()
    cursor.close()
    print("Successfully loaded csv file on to MySQL table")
except Exception as ex:
    print('Exception while load csv file on to MySQL table')
    print(ex)
finally:
        connection.close()
        print("MySQL connection is closed")