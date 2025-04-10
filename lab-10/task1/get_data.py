import psycopg2
from config import load_config
def get_data():
    """ Retrieve data from the phone_number table """
    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT first_name, phone_number FROM phone_number ORDER BY first_name")
                print("The number of contacts :", cur.rowcount)
                row = cur.fetchone()
                while row is not None:
                    print(f"{row[0]} : {row[1]}")
                    row = cur.fetchone()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
if __name__ == '__main__':
    get_data()