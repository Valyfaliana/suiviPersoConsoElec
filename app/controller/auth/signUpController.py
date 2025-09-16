from app.models.userModel import UserModel
from app.ui.components.waringDialog import WarningDialog
from app.ui.pages.pageSignUp import PageSignUp
from app.utils.passwordHasher import hash_password

class SignUpController:
    def __init__(self):
        self.page = PageSignUp()
        self.view = self.page.widget
        self.model = UserModel()

        self.page.add_user_signal.connect(self._add_user)

    def _add_user(self, nom:str, prenoms:str, pseudo:str, password:str, password1:str):
        if password == password1:
            self.model.add_user(nom, prenoms, pseudo, hash_password(password))
            print("User creer avec succes.")
        else:
            dlg = WarningDialog("Mot de passe non confirmer.", self.view)
            dlg.exec()