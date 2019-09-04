from app import db

class Customer(db.Model) :
    cust_no = db.Column(db.Integer, primary_key=True),
    nama = db.Column(db.String(30)),
    alamat = db.Column(db.String(100))

    def __repr__(self) :
        return '<Customer {}>'.format(self.nama)


class Genre(db.Model) :
    genre_id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(30))
    films = db.relationship('Film', backref='movie', lazy='dynamic' )

    def __repr__(self) :
        return '<Genre {}>'.format(self.nama)



class Film(db.Model) :
    film_no = db.Column(db.Integer, primary_key=True),
    judul = db.Column(db.String(50)),
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.genre_id'))