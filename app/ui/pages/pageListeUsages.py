from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QWidget
from app.ui.usages.listeUsage.listeUsage import Ui_w_listeUsage


class PageListeUsages(QObject ,Ui_w_listeUsage):
    def __init__(self):
        super().__init__()
        self.widget = QWidget()
        self.setupUi(self.widget)
        self.widget.setFixedSize(self.widget.size())

        # Styliser les headers du tableview
        self.listeUsage.horizontalHeader().setStyleSheet("""
            QHeaderView::section {
                background-color: #2698cf;
                color: white;
                border: 1px solid #555;
                font-weight: bold;
                border-left: none;
            }
        """)

        # Styliser le vertical header (numéros de ligne)
        self.listeUsage.verticalHeader().setStyleSheet("""
            QHeaderView::section {
                font-weight: bold;
                border: 1px solid #555;
                padding: 5px;
            }
        """)

        # Styliser la sélection et les headers
        self.listeUsage.setStyleSheet("""
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
        self.listeUsage.setFrameStyle(0)