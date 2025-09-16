from PySide6.QtCore import Signal, QObject
from PySide6.QtWidgets import QWidget
from app.ui.auth.signUp import Ui_w_SignUpForm

class PageSignUp(QObject ,Ui_w_SignUpForm):
    add_user_signal = Signal(str, str, str, str, str)

    def __init__(self):
        super().__init__()
        self.widget = QWidget()
        self.setupUi(self.widget)
        self.widget.setFixedSize(self.widget.size())

        # Pour la creation d'un nouveau user
        self.btnInscription.clicked.connect(self._on_add_user)

    def _on_add_user(self):
        nom = self.nomLineEdit.text()
        prenoms = self.prenomsLineEdit.text()
        pseudo = self.pseudoLineEdit.text()
        password = self.passwordLineEdit.text()
        password1 = self.passwordLineEdit_2.text()

        if nom and prenoms and pseudo and password and password1:
            self.add_user_signal.emit(nom, prenoms, pseudo, password, password1)
