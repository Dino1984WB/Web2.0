import os
import psycopg2


def getConnectionUSERS():
    dbConn = psycopg2.connect(
            host="localhost",
            database="Flask",
            port=5433,
            user='admin',
            password='password')

    return dbConn