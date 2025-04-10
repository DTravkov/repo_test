import psycopg2
from config import load_config

config = None
def connect():
    """ Connect to the PostgreSQL database server """
    try:
        global config
        # connecting to the PostgreSQL server
        config = load_config()
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    connect()