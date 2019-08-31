from __future__ import print_function

from decimal import Decimal 
from datetime import datetime, date, timedelta

import mysql.connector

cnx = mysql.connector.connect(host='localhost', database='testDB', user='root', password='')
# cursor = cnx.cursor()
tommorow = datetime.now().date() + timedelta(days=1)


curA = cnx.cursor(buffered=True)
curB = cnx.cursor(buffered=True)

query = (
    "SELECT s.emp_no, salary, from_date, to_date FROM employees as e"
    " LEFT JOIN salaries AS s USING (emp_no)"
    " WHERE to_date = DATE('9999-01-01')"
    " AND e.hire_date BETWEEN DATE(%s) AND DATE(%s)")

#UPDATE AND INSERT
update_old_salary = (
    "UPDATE salaries SET to_date = %s"
    " WHERE emp_no = %s AND from_date = %s"
)

update_old_salary = (
    "UPDATE salaries SET to_date = %s"
    " WHERE emp_no %s AND from_date = %s"
)

insert_new_salary=(
    "INSERT INTO salaries (emp_no, from_date, to_date, salary)"
    " VALUES (%s, %s, %s, %s)")

curA.execute(query, (date(2000,1,1), date(2000,12,31)))

# ITERATE THROUGH THE RESULT OF curA

for (emp_no, salary, from_date, to_date) in curA :
    new_salary = int(round(salary * Decimal('1.15')))
    curB.execute(update_old_salary, (tommorow, emp_no, from_date))
    curB.execute(insert_new_salary, (emp_no, tommorow, date(9999,1,1), new_salary))
    cnx.commit()
cnx.close()
