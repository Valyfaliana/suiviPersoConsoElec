from app.models.userModel import UserModel
from app.ui.components.dialog.waringDialog import WarningDialog
from app.ui.pages.pageSignUp import PageSignUp
from app.utils.passwordHasher import hash_password

class SignUpController:
    def __init__(self, basculer_page):
        from app.main_window import PAGE_CONNEXION

        self.page = PageSignUp()
        self.view = self.page.widget
        self.model = UserModel()

        self.page.add_user_signal.connect(self._add_user)

        # Quand on clique sur le btn se connecter
        self.page.btnConnecter.clicked.connect(lambda: basculer_page("Connexion", PAGE_CONNEXION))

    def _add_user(self, nom:str, prenoms:str, pseudo:str, password:str, password1:str):
        if password == password1:
            self.model.add_user(nom, prenoms, pseudo, hash_password(password))
            self.page.nomLineEdit.clear()
            self.page.prenomsLineEdit.clear()
            self.page.pseudoLineEdit.clear()
            self.page.passwordLineEdit.clear()
            self.page.passwordLineEdit_2.clear()
            print("User creer avec succes.")
            self.page.btnConnecter.click()
        else:
            dlg = WarningDialog("Mot de passe non confirmer.", self.view)
            dlg.exec()