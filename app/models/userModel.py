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
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    @staticmethod
    def add_user(nom: str, prenoms: str, email: str, password: str):
        conn = get_connection_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (nom, prenoms, email, password) VALUES (?, ?, ?, ?)", (nom, prenoms, email, password))
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
