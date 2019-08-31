import mysql.connector
from mysql.connector import errorcode
# from mysql.connector import (connection)



try :
    cnx = mysql.connector.connect(user='root', password='', host='localhost',database ='testDB', use_pure=False)
    if cnx.is_connected() :
        db_info=cnx.get_server_info()
        print("connection to my sql version", db_info)
        cnx.close()
except mysql.connector.Error as err :
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR :
        print("Something is wrong with you username")
    elif err.errno == errorcode.ER_BAD_DB_ERROR :
        print("Database doesnt exist")
    else :
        print(err)
else :
    cnx.close