import os
import datetime
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
        with connection.cursor() as cursor:
            list_of_names = ['Jimmy', 'Jim']
            #prepare string with same number of placeholders in  alist
            format_strings = ','.join(['%s']*len(list_of_names))
            cursor.execute("DELETE FROM Friends WHERE name in ({});".format(format_strings), list_of_names)
            connection.commit()
finally:
    #close the connection
    connection.close()