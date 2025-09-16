from app.models.userModel import UserModel
from app.ui.pages.pageSignIn import PageSignIn

class SignInController:
    def __init__(self, basculer_page):
        self.page = PageSignIn()
        self.view = self.page.widget
        self.model = UserModel()

        # Quand on clique sur le btn Inscription
        self.page.btnInscription.clicked.connect(lambda: basculer_page("Inscription", 1))