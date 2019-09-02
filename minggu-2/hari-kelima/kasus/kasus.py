import mysql.connector
from mysql.connector import errorcode

def main() :
    DB_NAME = "kasus"
    TABLES = {}
    
    TABLES['customer'] = (
        "CREATE TABLE `customer` ("
        "  `cust_no` int(11) NOT NULL AUTO_INCREMENT,"
        "  `nama` varchar(14) NOT NULL,"
        "  `alamat` varchar(16) NOT NULL,"
        "  PRIMARY KEY (`cust_no`)"
        ") ENGINE=InnoDB")

    TABLES['genre'] = (
        "CREATE TABLE `genre` ("
        "  `genre_id` int(11) NOT NULL AUTO_INCREMENT,"
        "  `nama` varchar(50) NOT NULL,"
        "  PRIMARY KEY (`genre_id`)"
        ") ENGINE=InnoDB")

    TABLES['film'] = (
        "CREATE TABLE `film` ("
        "  `film_no` int(11) NOT NULL AUTO_INCREMENT,"
        "  `judul` varchar(50) NOT NULL,"
        "  `genre_id` int(11) NOT NULL,"
        "  PRIMARY KEY (`film_no`),"
        "  CONSTRAINT `film_ibfk_1` FOREIGN KEY (`genre_id`) "
        "     REFERENCES `genre` (`genre_id`) ON DELETE CASCADE"
        ") ENGINE=InnoDB")

    TABLES['sewa'] = (
        "CREATE TABLE `sewa` ("
        " `sewa_id` int(11) NULL AUTO_INCREMENT,"
        " `cust_no` int(11) NOT NULL, "
        " `banyak` int(11) NOT NULL,"
        " PRIMARY KEY (`sewa_id`),"
        "  CONSTRAINT `sewa_ibfk1` FOREIGN KEY (`cust_no`) "
        "     REFERENCES `customer` (`cust_no`) ON DELETE CASCADE"
        ") ENGINE=InnoDB")

    TABLES['sewa_detail'] = (
         "CREATE TABLE `sewa_detail` ("
        " `sewa_detail_id` int(11) NOT NULL AUTO_INCREMENT,"
        " `cust_no` int(11) NOT NULL, "
        " `sewa_id` int(11) NOT NULL,"
        " `film_no` int(11) NOT NULL, "
        " PRIMARY KEY (`sewa_detail_id`),"
        "  CONSTRAINT `sewa_detail_ibfk_1` FOREIGN KEY (`cust_no`) "
        "     REFERENCES `customer` (`cust_no`) ON DELETE CASCADE,"
        "  CONSTRAINT `sewa_detail_ibfk_2` FOREIGN KEY (`sewa_id`) "
        "     REFERENCES `sewa` (`sewa_id`) ON DELETE CASCADE,"
        "  CONSTRAINT `sewa_detail_ibfk_3` FOREIGN KEY (`film_no`) "
        "     REFERENCES `film` (`film_no`) ON DELETE CASCADE"
        ") ENGINE=InnoDB")

    cnx = mysql.connector.connect(host='localhost', user='root', password='')
    cursor = cnx.cursor()

    # try :
    #     cursor.execute("USE {}".format(DB_NAME))
    # except mysql.connector.Error as err :
    #     if err.errno == errorcode.ER_BAD_DB_ERROR :
    #         create_database(cursor)
    #         print("Database {} created successfully".format(DB_NAME))
    #         cnx.database = DB_NAME
    #     else :
    #         print(err)
    #         exit(1)
        
    # for table in TABLES :
    #     table_description = TABLES[table]
    #     try :
    #         print("Creating table {}".format(table), end='')
    #         cursor.execute(table_description)
    #     except mysql.connector.Error as err :
    #         if err.errno == errorcode.ER_TABLE_EXISTS_ERROR :
    #             print("already exist")
    #         else :
    #             print(err.msg)
    #     else : 
    #         print("OK")

    ## INSERT DATA 
    cursor.execute("USE {}".format(DB_NAME))
    # CUSTOMERS = {}
    customers  = (
        "INSERT INTO customer (nama, alamat)"
        " VALUES (%(nama)s, %(alamat)s)")
    
    DATA_CUSTOMERS ={}
    DATA_CUSTOMERS["a"] = {
        'nama' : 'Firman',
        'alamat' : 'Bogor'
    }
    DATA_CUSTOMERS["b"] = {
        'nama' : 'Cherry',
        'alamat' : 'Bojong Gede'
    }
    DATA_CUSTOMERS["c"] = {
        'nama' : 'Nikhesia',
        'alamat' : 'Bojong Gede'
    }
    DATA_CUSTOMERS["d"] = {
        'nama' : 'Khaira',
        'alamat' : 'Bojong Gede'
    }

    jenis  = (
        "INSERT INTO genre (nama)"
        " VALUES (%(nama)s)")
    
    DATA_GENRE ={}
    DATA_GENRE["a"] = {
        'nama' : 'Action',
    }
    DATA_GENRE["b"] = {
        'nama' : 'Horror',
    }
    DATA_GENRE["c"] = {
        'nama' : 'Drama',
    }
    DATA_GENRE["d"] = {
        'nama' : 'Thriller',
    }

    films = ("INSERT INTO film (judul, genre_id) "
            "VALUES (%(judul)s, %(genre_id)s)")

    data_film = {}
    data_film["a"] = {
        'judul' : 'John Wick',
        'genre_id': int(1)
    }
    data_film["b"] =  {
        'judul' : 'Spiderman : Far From Home',
        'genre_id': int(1)
    }
    data_film["c"] = {
        'judul' : 'Annabele : Coming Home',
        'genre_id': int(2)
    }
    data_film["d"] = {
        'judul' : 'Transformers',
        'genre_id': int(3)
    }
    data_film["e"] = {
        'judul' : 'Batman',
        'genre_id': int(3)
    }
    data_film["f"] = {
        'judul' : 'Exorsist',
        'genre_id': int(3)
    }
    data_film["g"] = {
        'judul' : 'Uka Uka',
        'genre_id': int(4)
    }

    pinjam  = (
        "INSERT INTO sewa (cust_no, banyak)"
        " VALUES (%(cust_no)s, %(banyak)s)")
    
    DATA_SEWA ={}
    DATA_SEWA["a"] = {
        'cust_no' : 1,
        'banyak': 3
    }
    DATA_SEWA["b"] = {
        'cust_no' : 1,
        'banyak': 2
    }
    DATA_SEWA["c"] = {
        'cust_no' : 2,
        'banyak': 2
    }
    DATA_SEWA["d"] = {
        'cust_no' : 3,
        'banyak': 1
    }

    details  = (
        "INSERT INTO sewa_detail (cust_no, sewa_id, film_no)"
        " VALUES (%(cust_no)s, %(sewa_id)s, %(film_no)s)")
    
    DATAR_DETAIL ={}
    DATAR_DETAIL["a"] = {
        'cust_no' : 1,
        'sewa_id': 5,
        'film_no' :1
    }
    DATAR_DETAIL["b"] = {
        'cust_no' : 1,
        'sewa_id':5,
        'film_no' :2
    }
    DATAR_DETAIL["c"] = {
        'cust_no' : 1,
        'sewa_id': 5,
        'film_no' :3
    }
    DATAR_DETAIL["d"] = {
        'cust_no' : 1,
        'sewa_id': 6,
        'film_no' :4
    }
    DATAR_DETAIL["e"] = {
        'cust_no' : 1,
        'sewa_id': 6,
        'film_no' :1
    }
    DATAR_DETAIL["f"] = {
        'cust_no' : 2,
        'sewa_id': 7,
        'film_no' :1
    }
    DATAR_DETAIL["g"] = {
        'cust_no' : 2,
        'sewa_id': 7,
        'film_no' :1
    }
    DATAR_DETAIL["h"] ={
        'cust_no' : 3,
        'sewa_id': 8,
        'film_no' :1
    }

    # for i in DATA_CUSTOMERS :
    #     data = DATA_CUSTOMERS[i]
    #     print(customers,data)

    
    # for i in DATA_CUSTOMERS :
    #     try :
    #         cust = DATA_CUSTOMERS[i]
    #             # print(i)
    #         cursor.execute(customers, cust)
    #         cnx.database=DB_NAME
    #         cnx.commit()
    #         print("data customer telah terinput")
    #     except mysql.connector.Error as err :
    #         print(err.msg)

    # for a in DATA_GENRE :
    #     try :
    #         gen = DATA_GENRE[a]
    #         cursor.execute(jenis, gen)
    #         cnx.database = DB_NAME
    #         cnx.commit()
    #         print("data genre telah terinput")
    #     except mysql.connector.Error as err :
    #         print(err.msg)

    # for b in data_film :
    #     try :
    #         filem = data_film[b]
    #         cursor.execute(films, filem)
    #         cnx.database = DB_NAME
    #         cnx.commit()
    #         print("data film telah terinput")
    #     except mysql.connector.Error as err :
    #         print(err.msg)

    # for c in DATA_SEWA :
    #     try :
    #         pnjm = DATA_SEWA[c]
    #         cursor.execute(pinjam,pnjm)
    #         cnx.database = DB_NAME
    #         cnx.commit()
    #         print("data sewa telah terinput")
    #     except mysql.connector.Error as err :
    #         print(err.msg)

    # for d in DATAR_DETAIL :
    #     try :
    #         dtl = DATAR_DETAIL[d]
    #         cursor.execute(details, dtl)
    #         cnx.database= DB_NAME
    #         cnx.commit()
    #         print("data detail telah terinput")
    #     except mysql.connector.Error as err :
    #         print(err.msg)
    
    query = ("select c.nama, f.judul "
        "from customer c "
        "left join sewa_detail s "
        "on c.cust_no = s.cust_no "
        "left join film f "
        "on f.film_no = s.film_no "
        "where c.nama =%(nama)s")
    nama = {
        'nama':'Cherry Fonna'
    }
    try :
        cursor.execute(query,nama)
        # hasil = list(cursor)
        # print(map(lambda x: x, hasil[0] ))
        nama =[]
        for penyewa in cursor :
            nama.append(penyewa[0])
            if (nama.count(penyewa[0])==1) :
                print(penyewa[0])
            print(penyewa[1])
    except mysql.connector.Error as err :
        print(err.msg)

    cursor.close()
    cnx.close()

def create_database(cursor) :
    try :
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format('kasus'))
    except mysql.connector.Error as err :
        print("Failed to create database ")
        exit(1)


if __name__ == "__main__" :
    main()