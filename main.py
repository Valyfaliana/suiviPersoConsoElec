import sys
from PySide6.QtWidgets import QApplication
from app.main_window import MainWindow
from app.models.database import PATH_DB
from PySide6.QtSql import QSqlDatabase
import sys

def main():
    app = QApplication(sys.argv)

    # Init la base de donnees
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(PATH_DB)
    if not db.open():
        print("Erreur connexion base de données")
        sys.exit(1)

    # Création de la fenêtre principale
    window = MainWindow()
    window.show()

    # Boucle d’événements
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
