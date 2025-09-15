import sys
from PySide6.QtWidgets import QApplication
from app.ui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)

    # Création de la fenêtre principale
    window = MainWindow()
    window.show()

    # Boucle d’événements
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
