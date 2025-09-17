from PySide6.QtWidgets import QMainWindow, QStackedWidget, QApplication
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize

from app.controller.appareils.listeAppareilsController import ListeAppareilsController
from app.controller.auth.signInController import SignInController
from app.controller.auth.signUpController import SignUpController
from app.controller.usages.listeUsageController import ListeUsageController

PAGE_CONNEXION = 0
PAGE_INSCRIPTION = 1
PAGE_LISTE_APPAREILS = 2
PAGE_LISTE_USAGES = 3

class MainWindow(QMainWindow):
    user = []
    def __init__(self):
        super().__init__()

        self.stack = QStackedWidget()

        # Definir l'icon
        icon = QIcon()
        icon.addFile(u":/Main/icon/mainLog.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.setWindowIcon(icon)

        # Definier titre
        self.setWindowTitle("EcoWatt")

        # Definir les pages
        self.pageSignIn = SignInController(self)
        self.pageSignUp = SignUpController(self.basculer_page)
        self.pageListeAppareils = ListeAppareilsController(self)
        self.pageListeUsages = ListeUsageController(self)

        # Ajouter les pages
        self.stack.addWidget(self.pageSignIn.view) # 0
        self.stack.addWidget(self.pageSignUp.view) # 1
        self.stack.addWidget(self.pageListeAppareils.view) # 2
        self.stack.addWidget(self.pageListeUsages.view) # 3

        self.setCentralWidget(self.stack)

        self.setFixedSize(self.pageSignIn.view.size())

        # Afficher la page de connexion
        self.basculer_page("Connexion", 0)

    def basculer_page(self, titre, index):
        self.stack.setCurrentIndex(index)
        # self.setWindowTitle(titre)
        current = self.stack.currentWidget()
        self.setFixedSize(current.size())

        # Refresh liste appareils si on va vers page liste appareils
        if index == PAGE_LISTE_APPAREILS:
            self.pageListeAppareils.refresh_liste_appareils()

        # Refresh liste usages si on va vers page liste usages
        if index == PAGE_LISTE_USAGES:
            self.pageListeUsages.refresh_liste_usages()