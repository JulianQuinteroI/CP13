import sqlite3
from sqlite3 import Error


def get_db():
    try:
        dbconnect = sqlite3.connect("./db/database.db")
        return dbconnect
    except Error:
        print(Error)


def close_db(dbconnect):
    dbconnect.close()
