import psycopg2
import psycopg2.errorcodes
import time
import logging
import random

def create_accounts(conn) :
    with conn.cursor() as cur :
        cur.execute('CREATE TABLE IF NOT EXISTS accounts (id INT PRIMARY KEY, balance INT)')
        cur.execute('UPSERT INTO accounts (id, balance) VALUES (1, 1000), (2, 250)')
        logging.debug("create_accounts() : status message : {}".format(cur.statusmessage))
    conn.commit()

def print_balaces(conn) :
    with conn.cursor() as cur :
        cur.execute("SELECT id, balance FROM accounts")
        logging.debug("print_balance() : stats message {}".format(cur.statusmessage))
        rows = cur.fetchall()
        conn.commit()
        print("Balance at {}".format(time.asctime()))
        for row in rows :
            print([str(cell) for cell in row])

def delete_accounts(conn) :
    with conn.cursor() as cur :
        cur.execute('DELETE FROM bank.accounts')
        logging.debug("delete_accounts() : status message {}".format(cur.statusmessage))
    conn.commit()

# wrapper for a transaction
# this automically re-calls "op" with the open transaction
# as long as the database server asks for the transaction
def run_transaction(conn, op) :
    retries = 0
    max_retries = 3
    with conn :
        while True :
            retries +=1
            if retries == max_retries :
                err_msg = "Transaction did not succest after {} retries".format(max_retries)
                raise ValueError(err_msg)

            try :
                op(conn)
                # If we reach this point, we were able to commit, so we break
                # from the retry loop.
                break 
            except psycopg2.Error as e :
                logging.debug("e.pgcode {}".format(e.pgcode))
                if e.pgcode == '40001' :
                    # This is a retry error, so we roll back the current
                    # transaction and sleep for a bit before retrying. The
                    # sleep time increases for each failed transaction.
                    conn.rollback()
                    logging.debug("EXECUTE SERIALIZATIO_FAILURE BRANCH")
                    sleep_ms = (2**retries) * 0.1 * (random.random() + 0.5)
                    logging.debug("Sleeping {} seconds ".format(sleep_ms))
                    time.sleep(sleep_ms)
                    continue
                else :
                    logging.debug('EXECUTE NO-SERIALIZATION_FAILURE_BRANCH')
                    raise e


def test_retry_loop(conn) :
    with conn.cursor() as cur :
        cur.execute('SELECT now()')
        cur.execute("SELECT crdb_internal.force_retry('ls'::INTERVAL)")
    logging.debug("test_retry_loop() : status message : {}".format(cur.status))


def transfer_funds(conn, frm, to, amount) :
    with conn.cursor() as cur :
        cur.execute("SELECT balance FROM accounts WHERE id= " + str(frm))
        from_balance = cur.fetchone()[0]
        if from_balance < amount :
            err_msg = "Insufficient funds in account {} : have {}, need {}".format(frm, from_balance, amount)
            raise RuntimeError(err_msg)

        cur.execute("UPDATE accounts SET balance = balance - %s WHERE id = %s",(amount, frm))
        cur.execute("UPDATE accounts SET balance = balance + %s WHERE id = %s", (amount, to))
    conn.commit()
    logging.debug("transfer_fnds() : status message : {}".format(cur.statusmessage))


def main() :
    dsn = 'postgresql://maxroach@localhost:26257/bank?sslmode=disable'
    conn = psycopg2.connect(dsn)

    create_accounts(conn)
    print_balaces(conn)

    ammount=100
    fromId = 1
    toId = 2

    try :
        run_transaction(conn, lambda conn: transfer_funds(conn, fromId, toId, ammount))
    except ValueError as ve :
        logging.debug("run_transaction(conn, op) failed : {}".format(ve) )
        pass

    print_balaces(conn)

    delete_accounts(conn)
    conn.close()


if  __name__ == '__main__' :
    main()


