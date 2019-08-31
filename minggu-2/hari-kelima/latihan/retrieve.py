from __future__ import print_function
import datetime
import mysql.connector

def main() :

    cnx = mysql.connector.connect(host='localhost', database='testDB', user='root', password='')
    cursor = cnx.cursor()

    query = ("SELECT first_name, last_name, hire_date FROM employees "
            "WHERE emp_no = 1")

    hire_start = 1
    hire_end = datetime.date(2019, 1, 9)

    cursor.execute(query)

    for (first_name, last_name, hire_date) in cursor:
        print("{}, {} was hired on {:%d %b %Y}".format(last_name, first_name, hire_date))



    cursor.close()
    cnx.close()

if __name__ == "__main__" :
    main()