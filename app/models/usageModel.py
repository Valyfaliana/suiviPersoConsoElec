import datetime

from .appareilModel import AppareilModel
from .database import get_connection_db
from .userModel import UserModel


class UsageModel:
    def __init__(self):
        self._init_table()

    @staticmethod
    def _init_table():
        conn = get_connection_db()
        cur = conn.cursor()
        # Creer table appareil si pas encore creer
        AppareilModel()
        # Creer table users si pas encore creer
        UserModel()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS usages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                duree REAL NOT NULL,
                date_usage DATE NOT NULL,
                appareil_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                FOREIGN KEY(appareil_id) REFERENCES appareils(id) ON DELETE CASCADE,
                FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
            )
        """)
        conn.commit()
        conn.close()

    @staticmethod
    def add_usage(duree: float, date_usage: datetime.date, appareil_id: int, user_id:int):
        conn = get_connection_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO usages (duree, date_usage, appareil_id, user_id) VALUES (?, ?, ?, ?)", (duree, date_usage, appareil_id, user_id))
        conn.commit()

    @staticmethod
    def supprimer_usage(_id:int):
        conn = get_connection_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM usages WHERE id = ?", (_id,))
        conn.commit()
        conn.close()


    @staticmethod
    def get_usages_by_user_id(self, user_id:int):
        conn = get_connection_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM usages WHERE user_id=?", (user_id,))
        rows = cur.fetchall()
        conn.close()
        return [r for r in rows]
