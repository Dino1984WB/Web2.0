from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2

def getConnectionUSERS():
    dbConn = psycopg2.connect(
            host="localhost",
            database="Flask",
            port=5433,
            user='admin',
            password='password')

    connFinal = dbConn.cursor()
    return connFinal