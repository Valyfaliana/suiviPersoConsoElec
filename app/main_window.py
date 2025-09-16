from PySide6.QtWidgets import QMainWindow, QStackedWidget, QApplication

from app.controller.appareils.listeAppareilsController import ListeAppareilsController
from app.controller.auth.signInController import SignInController
from app.controller.auth.signUpController import SignUpController

PAGE_CONNEXION = 0
PAGE_INSCRIPTION = 1
PAGE_LISTE_APPAREILS = 2

class MainWindow(QMainWindow):
    user = []
    def __init__(self):
        super().__init__()

        self.stack = QStackedWidget()

        # Definir les pages
        self.pageSignIn = SignInController(self)
        self.pageSignUp = SignUpController(self.basculer_page)
        self.pageListeAppareils = ListeAppareilsController(self)

        # Ajouter les pages
        self.stack.addWidget(self.pageSignIn.view) # 0
        self.stack.addWidget(self.pageSignUp.view) # 1
        self.stack.addWidget(self.pageListeAppareils.view) # 2

        self.setCentralWidget(self.stack)

        self.setFixedSize(self.pageSignIn.view.size())

        # Afficher la page de connexion
        self.basculer_page("Connexion", 0)

    def basculer_page(self, titre, index):
        self.stack.setCurrentIndex(index)
        self.setWindowTitle(titre)
        current = self.stack.currentWidget()
        self.setFixedSize(current.size())

        # Refresh liste appareils si on va vers page liste appareils
        if index == PAGE_LISTE_APPAREILS:
            self.pageListeAppareils.refresh_liste_appareils()