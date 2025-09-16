from .database import get_connection_db
from .userModel import UserModel


class AppareilModel:
    def __init__(self):
        self._init_table()

    @staticmethod
    def _init_table():
        conn = get_connection_db()
        cur = conn.cursor()
        # Creer table user si pas encore creer
        UserModel()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS appareils (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                puissance REAL NOT NULL,
                FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
            )
        """)
        conn.commit()
        conn.close()

    @staticmethod
    def add_appareil(nom: str, puissance: float, user_id: int):
        conn = get_connection_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO appareils (nom, puissance, user_id) VALUES (?, ?, ?)", (nom, puissance, user_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_appareils_by_user_id(self, user_id:int):
        conn = get_connection_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM appareils WHERE user_id=?", (user_id,))
        rows = cur.fetchall()
        conn.close()
        return [r for r in rows]
