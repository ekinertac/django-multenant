from multitenant.drivers.psql import psql_connection
from multitenant.drivers.sqlite import sqlite3_connection


def create_database(specs, db_name):

    if specs["ENGINE"] == 'django.db.backends.sqlite3':
        sqlite3_connection(db_name)

    if specs["ENGINE"] == 'django.db.backends.postgresql_psycopg2':
        psql_connection(specs, db_name)
