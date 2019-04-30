import sys
import os
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def query_one(conn):
    cur = conn.cursor()
    cur.execute("select * from people;")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def query_one(conn):
    cur = conn.cursor()
    cur.execute("select * from people;")

    rows = cur.fetchall()

    for row in rows:
        print(row)


if len(sys.argv) == 1:
    print("""
    This is a Python module called "sql_task" used query a SQLiteDB database.
    
    Usage:
        python -m sql_task [options]
    
    Options:
        --task-one
            Returns results of a query of the then people
            who have visited the most sites.
            
        --task-two
            Returns a table called FrequentBrowsers containing
            the top ten users in descending order based on the 
            number of sites they've visited.
    """)
elif len(sys.argv) == 2:
    current_dir = os.path.dirname(__file__)
    database_path = os.path.join(current_dir, 'testdb.db')
    conn = create_connection(database_path)
    with conn:
        for param in sys.argv:
            if param == "--task-one":
                print("processing --task-one ")
                query_one(conn)
            elif param == "--task-two":
                print("processing  --task-two")
                query_two(conn)
            elif "sql_task" in param:
                pass
            else:
                print("Parameter " + str(param) + " not recognized. " \
                      + "Please try again or type 'python -m sql_task' for help.")
else:
    print("Too many parameters entered.\nPlease try again or type" \
          + " 'python -m sql_task' for help.")
