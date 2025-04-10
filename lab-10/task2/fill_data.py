import psycopg2
from config import load_config


def insert_score(name,score):
    """ Insert a new user and his score into the score table """
    sql = """INSERT INTO score(name,score)
             VALUES(%s, %s);"""
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql, (name,score))
                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    
def update_score(score, name):
    sql = """ UPDATE score
                SET score = %s
                WHERE name = %s"""
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the UPDATE statement
                cur.execute(sql, (score, name))
            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return 'Done'



if __name__ == '__main__':
    pass
    