import datetime

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog, QDialogButtonBox
from app.ui.usages.dialogAjout.dlgAjoutUsage import Ui_d_ajoutUsage


class DialogAjoutUsage(QDialog):
    ajout_usage_signal = Signal(float, datetime.date)

    def __init__(self, nomAppareil, parent=None):
        super().__init__(parent)
        self.ui = Ui_d_ajoutUsage()
        self.ui.setupUi(self)

        # Nom de l'appareil comme titre
        self.ui.nomAppareil.setText(nomAppareil)

        # Btn Enregistrer
        btn_enregistrer = self.ui.buttonBox.button(QDialogButtonBox.Save)
        btn_enregistrer.clicked.connect(self._on_ajout_usage)
        btn_enregistrer.setText("Enregistrer")

        # Styliser le bouton “Enregistrer”
        btn_enregistrer.setStyleSheet("""
            QPushButton {
                background-color: #28a745;   /* vert */
                color: white;
                padding: 6px 12px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #218838;
            }
            QPushButton:pressed {
                background-color: #1e7e34;
            }
        """)

        # Btn Cancel
        cancel_btn = self.ui.buttonBox.button(QDialogButtonBox.Cancel)
        cancel_btn.setText("Annuler")

        # Styliser le bouton “Cancel”
        cancel_btn.setStyleSheet("""
            QPushButton {
                background-color: #dc3545;   /* rouge */
                color: white;
                padding: 6px 12px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c82333;
            }
            QPushButton:pressed {
                background-color: #bd2130;
            }
        """)

    def _on_ajout_usage(self, event):
        duree = self.ui.dureeDUtilisationDoubleSpinBox.value()
        date_usage = self.ui.dateDUtilisationDateEdit.date().toPython() # converti en datetime.date

        if duree and date_usage:
            self.ajout_usage_signal.emit(duree, date_usage)
