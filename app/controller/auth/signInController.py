from app.models.userModel import UserModel
from app.ui.components.dialog.waringDialog import WarningDialog
from app.ui.pages.pageSignIn import PageSignIn
from app.utils.passwordHasher import verify_password


class SignInController:
    def __init__(self, mainWin):
        from app.main_window import PAGE_INSCRIPTION

        self.page = PageSignIn()
        self.view = self.page.widget
        self.model = UserModel()
        # fenetre principale
        self.mainWin = mainWin

        # Quand il y a tentative de connecation
        self.page.connexion_signal.connect(self.do_connexion)

        # Quand on clique sur le btn Inscription
        self.page.btnInscription.clicked.connect(lambda: mainWin.basculer_page("Inscription", PAGE_INSCRIPTION))

    def do_connexion(self, pseudo, password):
        from app.main_window import PAGE_LISTE_APPAREILS

        user = self.model.get_user_by_pseudo(pseudo)
        if user:
            if verify_password(user["password"], password):
                self.mainWin.user = user
                # reinitialiser les champs
                self.page.pseudoLineEdit.clear()
                self.page.motDePasseLineEdit.clear()
                self.mainWin.basculer_page("Liste appareils de l'utilisateur", PAGE_LISTE_APPAREILS)
            else:
                dlg = WarningDialog("Mot de passe incorrect.", self.view)
                dlg.exec()
        else:
            dlg = WarningDialog("Identifiant invalide.", self.view)
            dlg.exec()