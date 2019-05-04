import sys
import os
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    # generate database path relative to working directory
    current_dir = os.path.dirname(__file__)
    database_path = os.path.join(current_dir, db_file)
    try:
        conn = sqlite3.connect(database_path)
        return conn
    except Error as e:
        print(e)
    return None


def generate_list(conn):
    # generate the list of top 10 users who visited the most sites
    cur = conn.cursor()
    query_string = """ SELECT personId, COUNT(DISTINCT siteId) as qtyOfSitesVisited FROM visits GROUP BY personId 
                ORDER BY qtyOfSitesVisited DESC LIMIT 10;"""
    cur.execute(query_string)
    rows = cur.fetchall()
    freq_users = [row for row in rows]
    return freq_users


def insert_row(conn, values):
    # insert a tuple into the frequent_browsers table
    query_string = """INSERT INTO frequent_browsers(person_id,num_sites_visited)
                      VALUES(?,?);"""
    cur = conn.cursor()
    cur.execute(query_string, values)
    return cur.lastrowid  # should return 15::11


def table_wipe(conn):
    # wipe the frequent_browsers table before inserting values
    cur = conn.cursor()
    query_string = "DELETE FROM frequent_browsers;"
    cur.execute(query_string)


def list_table(conn):
    # query all values from frequent_browsers table & display neatly in console
    cur = conn.cursor()
    query_string = "SELECT * FROM frequent_browsers;"
    cur.execute(query_string)
    rows = cur.fetchall()
    freq_users_table_list = [row for row in rows]
    print("person_id  |  num_sites_visited\n-------------------------------")
    for row in freq_users_table_list:
        if row[0] < 10:
            print(str(row[0]) + "            " + str(row[1]))
        else:
            print(str(row[0]) + "           " + str(row[1]))


if len(sys.argv) == 1:
    if sys.argv[0] == "test_sql_task.py":
        # don't print if you're running unit tests
        pass
    else:
        # no command line arguments returns help section
        print("""
        This is a Python module called "sql_task" used query a SQLiteDB database.
    
        Usage:
          $ python -m sql_task [options]
            
            Example(s):
              $ python -m sql_task --task-one
                
              $ python -m sql_task --task-two 
    
        Options:
            --task-one
                Returns results of a query of the then people
                who have visited3 the most sites.
    
            --task-two
                Inserts the values returned from the above query
                into the 'frequent_users' table. Once all values
                are inserted, the table is displayed.
                
    """)
elif len(sys.argv) == 2:
    # one command line argument entered
    print("\nEstablishing database connection...\n")
    conn = create_connection('testdb.db')
    with conn:
        for param in sys.argv:
            # iteratively check each parameter
            if param == "--task-one":
                # TASK ONE | Query 'visits' table to find & display top 10 users who visited most sites
                print("Generating list of top 10 frequent users...\n\n")
                freq_users = generate_list(conn)
                print("person_id  |  num_sites_visited\n-------------------------------")
                for user in freq_users:
                    if user[0] < 10:
                        print(str(user[0]) + "            " + str(user[1]))
                    else:
                        print(str(user[0]) + "           " + str(user[1]))
                print("\nRun '--task-two' to insert the above values into the frequent_users table")

            elif param == "--task-two":
                # TASK 2 | Inserts values from TASK ONE into 'frequent_browsers' table & displays table
                print("Inserting list into frequent_users table...\n")
                table_wipe(conn)
                freq_users = generate_list(conn)
                for user in freq_users:
                    insert_row(conn, user)
                print("Displaying values from newly created frequent_users table...\n")
                list_table(conn)
            elif "sql_task" in param:
                pass
            elif "-m unittest" in param:
                pass
            else:
                print("Parameter " + str(param) + " not recognized. " \
                      + "Please try again or type 'python -m sql_task' for help.")
else:
    print("Too many parameters entered.\nPlease try again or type" \
          + " 'python -m sql_task' for help.")
