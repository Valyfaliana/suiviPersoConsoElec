from PySide6.QtWidgets import QMainWindow, QLabel, QWidget, QVBoxLayout

from app.ui.loginForm import Ui_w_loginForm


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Config de la fenêtre
        self.setWindowTitle("Mon App PySide6")
        self.resize(800, 600)

        self.ui = Ui_w_loginForm()
        self.ui.setupUi(self)
