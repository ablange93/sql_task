import sys
import os

if len(sys.argv) == 1:
    print(""""
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
    print("will proccess either --task-one or --task-two")
else:
    print("Too many parameters entered. Type 'python -m sql_task' for help")
