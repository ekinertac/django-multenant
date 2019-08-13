import sqlite3
from sqlite3 import Error


def sqlite3_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(f"{db_file}")
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()
