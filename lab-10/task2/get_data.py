import psycopg2
from config import load_config


def get_data():
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                sql = "SELECT * FROM score;"
                cur.execute(sql)
                rows = cur.fetchall()
                return rows
    except (psycopg2.DatabaseError,Exception) as error:
        print(error)

def delete_db():
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                sql = ("DELETE FROM score;","ALTER TABLE score DROP COLUMN id;","ALTER TABLE score ADD COLUMN id SERIAL PRIMARY KEY;")
                for command in sql:
                    cur.execute(command)
    except (psycopg2.DatabaseError,Exception) as error:
        print(error)

def get_names():
    return [x[0] for x in get_data()]

if __name__ == '__main__':
    print(get_data())