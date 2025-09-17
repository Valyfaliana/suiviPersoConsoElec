from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QWidget
from app.ui.usages.listeUsage.listeUsage import Ui_w_listeUsage


class PageListeUsages(QObject ,Ui_w_listeUsage):
    def __init__(self):
        super().__init__()
        self.widget = QWidget()
        self.setupUi(self.widget)
        self.widget.setFixedSize(self.widget.size())