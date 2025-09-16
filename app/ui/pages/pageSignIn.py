from PySide6.QtCore import QObject
from PySide6.QtWidgets import QWidget
from app.ui.auth.signIn import Ui_w_signIn

class PageSignIn(QObject ,Ui_w_signIn):

    def __init__(self):
        super().__init__()
        self.widget = QWidget()
        self.setupUi(self.widget)
        self.widget.setFixedSize(self.widget.size())
