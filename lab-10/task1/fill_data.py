import psycopg2
from config import load_config
def insert_number(name,phone):
    """ Insert a new user and his phone into the phonebook """
    sql = """INSERT INTO phone_number(first_name,phone_number)
             VALUES(%s, %s);"""
    vendor_id = None
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql, (name,phone))
                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return vendor_id
    

if __name__ == '__main__':
    insert_number("Demid","+123456789")
    