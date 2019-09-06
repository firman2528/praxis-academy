import mysql.connector as mariadb 
from flask import Flask, render_template
from datetime import datetime


app = Flask(__name__)


app.config['MYSQL_DATABASE_USER']='dt_admin'
app.config['MYSQL_DATABASE_PASSWORD']='dt2016'
app.config['MYSQL_DATABASE_DB']='penyewaan'
app.config['MYSQL_DATABASE_HOST']='localhost'



class Database:
    def __init__(self) :
        host="127.0.0.1"
        user="root"
        password = ""
        db="penyewaan"

        self.con=mariadb.connect(host=host, user=user, password=password, db=db)
        self.cursor = self.con.cursor()

        

    def list_customer(self) :
        self.cursor.execute("select * from customer")
        result = self.cursor.fetchall()
        print(result)
        return result 

@app.template_filter()
def datetimefilter(value, format='%Y%m%d %H:%M') :
    # CONVERT A DATETIME TO A DIFFERENT FORMAT
    return value.strftime(format)
    

@app.route("/")
def template_test() :
    return render_template("template.html", my_string="Wheeee !", my_list=[0,1,2,3,4,5], title="Firman Yuspriyadi",
    current_time=datetime.now())


@app.route("/home")
def home() :
    db = Database()
    emp = db.list_customer()
    print(emp)

    return render_template('template.html',
    my_string="HALOOOOO",
    my_list=[0,1,2,3,4,5],
    title="Home", current_time=datetime.now(), query = emp)

@app.route("/customer")
def customer():
    db = Database()
    cust = db.list_customer()
    return render_template('customer.html', customers = cust)

@app.route("/about")
def about() :
    return render_template('template.html',
    my_string="HALOOOOO",
    my_list=[0,1,2,3,4,5],
    title="About", current_time=datetime.now())

@app.route("/contact")
def contact() :
    return render_template('template.html',
    my_string="HALOOOOO",
    my_list=[0,1,2,3,4,5],
    title="Contact", current_time=datetime.now())


if __name__ == '__main__' :
    app.run(debug=True)