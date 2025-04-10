import psycopg2
from config import load_config

def update_name(id, first_name):
    sql = """ UPDATE phone_number
                SET first_name = %s
                WHERE id = %s"""
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the UPDATE statement
                cur.execute(sql, (first_name, id))
            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return 'Done'
    
def update_number(id, phone_number):
    sql = """ UPDATE phone_number
                SET phone_number = %s
                WHERE id = %s"""
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the UPDATE statement
                cur.execute(sql, (phone_number, id))
            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return 'Done'


def delete_number(first_name):
    sql = """ DELETE FROM phone_number WHERE first_name = %s"""
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the UPDATE statement
                cur.execute(sql, (first_name,))
            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return 'Done'
    


if __name__ == '__main__':
    delete_number('Charlie')
    