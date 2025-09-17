from app.models.usageModel import UsageModel
from app.ui.pages.pageListeUsages import PageListeUsages
from PySide6.QtSql import QSqlQueryModel, QSqlDatabase
from PySide6.QtCore import QSortFilterProxyModel


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
        db = QSqlDatabase.database()

        # Recuperer les data de la base de donnee
        model = QSqlQueryModel()
        query = """
        SELECT a.nom AS Nom,
               u.duree AS Duree_heures,
               u.date_usage AS Date_utilisation,
               (u.duree * a.puissance / 1000) AS Consommation_KWh
        FROM usages u
        JOIN appareils a ON u.appareil_id = a.id
        """
        model.setQuery(query, db)

        # Pour activer le trie avec QSqlQueryModel
        proxy = QSortFilterProxyModel()
        proxy.setSourceModel(model)

        # Relier le tableau aux donnees de la base de donnee
        self.page.listeUsage.setModel(proxy)
