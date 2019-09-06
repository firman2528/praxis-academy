from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///penyewaan.db'
db = SQLAlchemy(app)


class Customer(db.Model) :
    __tablename__='customer'
    cust_no = db.Column('cust_no',db.Integer, primary_key=True),
    nama = db.Column('nama',db.String(20))
    alamat = db.Column('alamat',db.String(30))

    def __repr__(self) :
        return '<Customer {}>'.format(self.nama)