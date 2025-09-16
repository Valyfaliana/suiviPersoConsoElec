from PySide6.QtWidgets import QMainWindow, QStackedWidget

from app.controller.auth.signUpController import SignUpController

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.stack = QStackedWidget()

        # Definir les pages
        self.pageSignUp = SignUpController()

        # Ajouter les pages
        self.stack.addWidget(self.pageSignUp.view)

        self.setCentralWidget(self.stack)
        self.setFixedSize(self.pageSignUp.view.size())
