import os
import pymysql

# get username from cloud9 workspace

username = os.getenv('C9_USER')

# connect to database
connection = pymysql.connect(host='localhost',
                            user = username,
                            password = '',
                            db='Chinook')

#run a query                            
try:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    #close the connection
    connection.close()