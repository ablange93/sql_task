import sys
import os
import sqlite3
from sqlite3 import Error
import unittest
from sql_task import create_connection, generate_list


class TestDbComponents(unittest.TestCase):

    def test_create_connection(self):
        # test if the DB connection is working
        conn = create_connection('testdb.db')
        with conn:
            conn_type = type(conn)
        self.assertEqual(conn_type, sqlite3.Connection)


    def test_generate_list(self):
        # test if --task-one's query is valid
        conn = create_connection('testdb.db')
        with conn:
            list_output = generate_list(conn)
        list_values = [(30, 23), (19, 16), (3, 15), (6, 15), (2, 13),
                       (14, 12), (26, 12), (9, 11), (11, 11), (15, 11)]
        self.assertEqual(list_output, list(list_values))


if __name__ == '__main__':
    unittest.main()
