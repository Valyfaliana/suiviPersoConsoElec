import sqlite3

def get_connection_db():
    conn = sqlite3.connect("app/data/suiviConsoElec.db")
    return conn

