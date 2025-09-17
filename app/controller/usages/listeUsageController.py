from app.models.usageModel import UsageModel
from app.ui.pages.pageListeUsages import PageListeUsages
from PySide6.QtSql import QSqlTableModel


class ListeUsageController:
    def __init__(self, mainWin):
        from app.main_window import PAGE_CONNEXION, PAGE_LISTE_APPAREILS

        self.mainWin = mainWin
        self.page = PageListeUsages()
        self.view = self.page.widget
        self.model = UsageModel()

        # Quand on clique sur le btn quitter
        self.page.btnQuitter.clicked.connect(lambda: mainWin.basculer_page("Connexion", PAGE_CONNEXION))

        # Quand on clique sur le btn Appareils
        self.page.btnListeAppareils.clicked.connect(lambda: mainWin.basculer_page("Liste appareils", PAGE_LISTE_APPAREILS))

    def refresh_liste_usages(self):
        # Recuperer les data de la base de donnee
        model = QSqlTableModel()
        model.setTable("usages")
        model.setFilter(f"user_id={self.mainWin.user["id"]}")
        model.select()

        # Relier le tableau aux donnees de la base de donnee
        self.page.listeUsage.setModel(model)

        # Cacher les colonnes inutiles
        # self.page.listeUsage.setColumnHidden(0, True) # colonne des id
        # self.page.listeUsage.setColumnHidden(3, True) # colonne des user_id
