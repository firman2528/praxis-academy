from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(host='localhost', database='testDB', user='root', password='')
cursor = cnx.cursor()

tommorow = datetime.now().date() + timedelta(days=1)
sesuk = datetime.now().date() - timedelta(days=16)

add_employee = ("INSERT INTO employees"
                "(first_name, last_name, hire_date, gender, birth_date) "
               "VALUES (%s, %s, %s, %s, %s)")
add_salary = ("INSERT INTO salaries "
              "(emp_no, salary, from_date, to_date) "
              "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")
            
data_employee = ('Firman', 'Yuspriyadi', sesuk, 'M', date(1983,4,7))


cursor.execute(add_employee, data_employee)

emp_no = cursor.lastrowid

data_salary = {
    'emp_no' : emp_no,
    'salary' : 5000, 
    'from_date' : tommorow,
    'to_date' : date(9999,1,1)
}
cursor.execute(add_salary, data_salary)

cnx.commit()
cursor.close()
cnx.close()