from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QWidget
from app.ui.appareils.listeAppareils import Ui_w_listeAppareils

class PageListeAppareils(QObject ,Ui_w_listeAppareils):
    ajout_appareil_signal = Signal(str, float)

    def __init__(self):
        super().__init__()
        self.widget = QWidget()
        self.setupUi(self.widget)
        self.widget.setFixedSize(self.widget.size())

        # Btn ajouter appareils
        self.btnAjouterAppareil.clicked.connect(self._on_ajout_appareil)

    def _on_ajout_appareil(self):
        nom = self.nomAppareilLineEdit.text()
        puissance = self.puissanceConsommerDoubleSpinBox.value()

        if nom and puissance:
            self.ajout_appareil_signal.emit(nom, puissance)

