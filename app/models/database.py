import sqlite3

def get_connection_db():
    conn = sqlite3.connect("app/data/suiviConsoElec.db")
    conn.execute("PRAGMA foreign_keys = ON") # pour les foreign key
    conn.row_factory = sqlite3.Row
    return conn

