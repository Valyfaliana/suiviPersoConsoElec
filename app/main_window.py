from PySide6.QtWidgets import QMainWindow, QStackedWidget, QApplication
from app.controller.auth.signInController import SignInController
from app.controller.auth.signUpController import SignUpController

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.stack = QStackedWidget()

        # Definir les pages
        self.pageSignIn = SignInController(self.basculer_page)
        self.pageSignUp = SignUpController(self.basculer_page)

        # Ajouter les pages
        self.stack.addWidget(self.pageSignIn.view) # 0
        self.stack.addWidget(self.pageSignUp.view) # 1

        self.setCentralWidget(self.stack)

        self.setFixedSize(self.pageSignIn.view.size())

        # Afficher la page de connexion
        self.basculer_page("Connexion", 0)

    def basculer_page(self, titre, index):
        self.stack.setCurrentIndex(index)
        self.setWindowTitle(titre)
        current = self.stack.currentWidget()
        self.setFixedSize(current.size())