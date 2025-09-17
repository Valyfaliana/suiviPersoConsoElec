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

        # Styliser les headers du tableview
        self.listeAppareils.horizontalHeader().setStyleSheet("""
            QHeaderView::section {
                background-color: black;
                color: white;
                border: 1px solid #555;
                font-weight: bold;
            }
        """)

        # Styliser le vertical header (numéros de ligne)
        self.listeAppareils.verticalHeader().setStyleSheet("""
            QHeaderView::section {
                font-weight: bold;
                border: 1px solid #555;
                padding: 5px;
            }
        """)

        # Styliser la sélection et les headers
        self.listeAppareils.setStyleSheet("""
            /* Lignes sélectionnées */
            QTableView::item:selected {
                background-color: #3399ff;
                color: white;
            }

            /* Lignes alternées */
            QTableView {
                alternate-background-color: #f0f8ff;
            }
            
            QTableView { background-color: rgb(147, 147, 145); }
        """)

        # Enleve la bordure
        self.listeAppareils.setFrameStyle(0)


    def _on_ajout_appareil(self):
        nom = self.nomAppareilLineEdit.text()
        puissance = self.puissanceConsommerDoubleSpinBox.value()

        if nom and puissance:
            self.ajout_appareil_signal.emit(nom, puissance)

