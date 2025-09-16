from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QWidget
from app.ui.auth.signIn import Ui_w_signIn

class PageSignIn(QObject ,Ui_w_signIn):
    connexion_signal = Signal(str, str)

    def __init__(self):
        super().__init__()
        self.widget = QWidget()
        self.setupUi(self.widget)
        self.widget.setFixedSize(self.widget.size())

        # Clique du btnConnexion
        self.btnConnection.clicked.connect(self._on_connexion)

    def _on_connexion(self):
        pseudo = self.pseudoLineEdit.text()
        password = self.motDePasseLineEdit.text()

        if password and pseudo:
            self.connexion_signal.emit(pseudo, password)
