import sqlite3
import sys, os

def resource_path(relative_path):
    """Retourne le chemin vers le fichier, même quand packagé avec PyInstaller"""
    if hasattr(sys, '_MEIPASS'):
        # Mode exe
        return os.path.join(sys._MEIPASS, relative_path)
    # Mode normal (Python)
    return os.path.join(os.path.abspath("."), relative_path)

PATH_DB = resource_path("app/data/suiviConsoElec.db")

def get_connection_db():
    conn = sqlite3.connect(PATH_DB)
    conn.execute("PRAGMA foreign_keys = ON") # pour les foreign key
    conn.row_factory = sqlite3.Row
    return conn

