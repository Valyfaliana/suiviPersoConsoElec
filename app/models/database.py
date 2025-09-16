import sqlite3

def get_connection_db():
    conn = sqlite3.connect("app/data/suiviConsoElec.db")
    conn.row_factory = sqlite3.Row
    return conn

