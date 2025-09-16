from PySide6.QtWidgets import QDialog

from app.ui.components.dialog.warningDlg import Ui_w_warningDlg


class WarningDialog(QDialog):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.ui = Ui_w_warningDlg()
        self.ui.setupUi(self)
        self.ui.label.setText(text)
