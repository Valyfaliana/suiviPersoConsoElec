from .database import get_connection_db

class UserModel:
    def __init__(self):
        self._init_table()

    @staticmethod
    def _init_table():
        conn = get_connection_db()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                prenoms TEXT NOT NULL,
                pseudo TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    @staticmethod
    def add_user(nom: str, prenoms: str, pseudo: str, password: str):
        conn = get_connection_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (nom, prenoms, pseudo, password) VALUES (?, ?, ?, ?)", (nom, prenoms, pseudo, password))
        conn.commit()
        conn.close()

    @staticmethod
    def get_users(self):
        conn = get_connection_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
        conn.close()
        return [r for r in rows]

    @staticmethod
    def get_user_by_pseudo(_pseudo:str):
        conn = get_connection_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE pseudo=?", (_pseudo,))
        res = cur.fetchone()
        conn.close()
        return res
