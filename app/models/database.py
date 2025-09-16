import sqlite3

PATH_DB = "app/data/suiviConsoElec.db"

def get_connection_db():
    conn = sqlite3.connect(PATH_DB)
    conn.execute("PRAGMA foreign_keys = ON") # pour les foreign key
    conn.row_factory = sqlite3.Row
    return conn

