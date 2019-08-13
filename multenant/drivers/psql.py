import psycopg2
from django.db import connection
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def psql_connection(spec, db_name):
    psql_kwargs = {
        'dbname': spec['NAME'],
        'user': spec['USER'],
        'host': spec['HOST'],
        'password': spec['PASSWORD']
    }

    con = psycopg2.connect(**psql_kwargs)

    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()

    cur.execute("CREATE DATABASE %s;" % db_name)
