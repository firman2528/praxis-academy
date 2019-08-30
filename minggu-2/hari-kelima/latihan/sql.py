import mysql.connector
from mysql.connector import errorcode
from mysql.connector import (connection)


try :
    cnx = mysql.connector.connect(user='root', database='customers')
except connection.connector.Error as err :
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR :
        print("Something is wrong with you username")
    elif err.errno == errorcode.ER_BAD_DB_ERROR :
        print("Database doesnt exist")
    else :
        print(err)
else :
    cnx.close