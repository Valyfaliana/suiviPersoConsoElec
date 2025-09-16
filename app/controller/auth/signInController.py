from app.models.userModel import UserModel
from app.ui.components.dialog.waringDialog import WarningDialog
from app.ui.pages.pageSignIn import PageSignIn
from app.utils.passwordHasher import verify_password


class SignInController:
    def __init__(self, basculer_page):
        from app.main_window import PAGE_INSCRIPTION
        
        self.page = PageSignIn()
        self.view = self.page.widget
        self.model = UserModel()

        # Quand il y a tentative de connecation
        self.page.connexion_signal.connect(self.do_connexion)

        # Quand on clique sur le btn Inscription
        self.page.btnInscription.clicked.connect(lambda: basculer_page("Inscription", PAGE_INSCRIPTION))

    def do_connexion(self, pseudo, password):
        user = self.model.get_user_by_pseudo(pseudo)

        if user:
            if verify_password(user["password"], password):
                print("Connexion reussi.")
            else:
                dlg = WarningDialog("Mot de passe incorrect.", self.view)
                dlg.exec()
        else:
            dlg = WarningDialog("Identifiant invalide.", self.view)
            dlg.exec()