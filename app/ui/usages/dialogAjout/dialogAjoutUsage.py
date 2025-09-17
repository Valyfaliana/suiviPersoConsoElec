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

    def _on_ajout_usage(self, event):
        duree = self.ui.dureeDUtilisationDoubleSpinBox.value()
        date_usage = self.ui.dateDUtilisationDateEdit.date().toPython() # converti en datetime.date

        if duree and date_usage:
            self.ajout_usage_signal.emit(duree, date_usage)
