import psycopg2
import psycopg2.errorcodes
import time
import logging 
import random


def create_table(conn) :
    with conn.cursor() as cur :
        cur.execute("CREATE TABLE IF NOT EXISTS customer ("
        "  cust_no INT NOT NULL PRIMARY KEY,"
        "  nama STRING,"
        "  alamat STRING)")

        cur.execute(
            "CREATE TABLE IF NOT EXISTS genre ("
        "  genre_id INT NOT NULL PRIMARY KEY,"
        "  nama STRING)")
        cur.execute(
            "CREATE TABLE IF NOT EXISTS film ("
        "  film_no INT NOT NULL PRIMARY KEY ,"
        "  judul STRING NOT NULL,"
        "  genre_id INT NOT NULL REFERENCES genre (genre_id) ON DELETE CASCADE)")

        cur.execute(
            "CREATE TABLE IF NOT EXISTS sewa ("
        " sewa_id INT NOT NULL PRIMARY KEY,"
        " cust_no INT NOT NULL REFERENCES customer (cust_no) ON DELETE CASCADE,"
        " banyak INT NOT NULL)")

        cur.execute(
            "CREATE TABLE IF NOT EXISTS sewa_detail ("
        " sewa_detail_id INT NOT NULL PRIMARY KEY,"
        " cust_no INT NOT NULL REFERENCES customer (cust_no) ON DELETE CASCADE, "
        " sewa_id INT NOT NULL REFERENCES sewa (sewa_id) ON DELETE CASCADE,"
        " film_no INT NOT NULL REFERENCES film (film_no) ON DELETE CASCADE)")

        cur.execute("Insert INTO customer (cust_no, nama, alamat) VALUES (1, 'Firman', 'Bogor'), (2, 'Cherry Fonna', 'Bojong'),"
            "(3, 'Nikhesia', 'Bojong'), (4, 'Khaira', 'Bojong')")
        cur.execute("UPSERT INTO genre (genre_id, nama) VALUES (1,'Action'), (2,'Horror'), (3,'Drama'), (4,'Serial')")
        cur.execute("UPSERT INTO film (film_no, judul, genre_id) VALUES (1,'John Wick', 1),(2,'Spiderman', 1), (3,'Tayo', 1), (4,'Anabele', 2),"
                "(5,'Batman', 4), (6,'Transformers', 3)")
        cur.execute("UPSERT INTO sewa (sewa_id, cust_no, banyak) VALUES (1,1,2), (2,4,1), (3,2,2), (4,3,2)")
        cur.execute("UPSERT INTO sewa_detail (sewa_detail_id, cust_no, sewa_id, film_no)"
            "VALUES (1,1,1,1), (2,1,1,2), (3,4,2,3), (4,2,3,4), (5,2,3,1), (6,3,4,3), (7, 3,4,2)")

    conn.commit()

def print_sewa(conn) :
    with conn.cursor() as cur :
        cur.execute("select c.nama, f.judul "
        "from customer c "
        "left join sewa_detail s "
        "on c.cust_no = s.cust_no "
        "left join film f "
        "on f.film_no = s.film_no "
        "where c.nama ='Firman'")
        rows = cur.fetchall()
        conn.commit()
        print("Penyewa : ")
        for row in rows :
            print([str(cell) for cell in row])



def run_transaction(conn) :
    retries = 0
    max_retries =3 
    with conn :
        while True :
            retries +=1
            if retries == max_retries :
                err_msg = "Transaction did not succest after {} retries".format(max_retries)
                raise ValueError(err_msg)
            
            try :
                op(conn)
                break 
            except psycopg2.Error as e :
                logging.debug("e.pgcode {}".format(e.pgcode))
                if e.pgcode == '40001' :
                    conn.rollback()
                    logging.debug("EXECUTE SERIALIZATIO_FAILURE BRANCH")
                    sleep_ms = (2**retries) * 0.1 * (random.random() + 0.5)
                    logging.debug("Sleeping {} seconds".format(sleep_ms))
                    time.sleep(sleep_ms)
                    continue
                else :
                    logging.debug("EXECUTE NO-SERIALIZATION_FAILURE_BRANCH")
                    raise e
            
def test_retry_loop(conn) :
    with conn.cursor() as cur :
        cur.execute("SELECT row()")
        cur.execute("SELECT crdb_internal.force_retry('ls'::INTERVAL)")
    logging.debug("test_retry_loop : status message : ".format()(cur.statusmessage))



def main() :
    dsn = 'postgresql://maxroach@localhost:26257/penyewaan?sslmode=disable'
    conn = psycopg2.connect(dsn)

    create_table(conn)
    print_sewa(conn)
    conn.close()


if __name__ == '__main__' :
    main()