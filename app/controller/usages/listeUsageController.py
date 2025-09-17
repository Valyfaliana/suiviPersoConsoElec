from app.models.usageModel import UsageModel
from app.ui.components.dialog.waringDialog import WarningDialog
from app.ui.pages.pageListeUsages import PageListeUsages
from PySide6.QtSql import QSqlQueryModel, QSqlDatabase, QSqlQuery
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

        # Quand on clique sur btn supprimer
        self.page.btnSupprimer.clicked.connect(self.supprimer_usage)

    def refresh_liste_usages(self):
        db = QSqlDatabase.database()

        # Recuperer les data de la base de donnee
        model = QSqlQueryModel()
        query = QSqlQuery()
        query.prepare("""
        SELECT u.id,
               a.nom AS Nom,
               u.duree AS Duree_heures,
               u.date_usage AS Date_utilisation,
               (u.duree * a.puissance / 1000) AS Consommation_KWh
        FROM usages u
        JOIN appareils a ON u.appareil_id = a.id
        WHERE u.user_id=?
        """)
        query.addBindValue(self.mainWin.user["id"])
        query.exec()
        model.setQuery(query)

        # Pour activer le trie avec QSqlQueryModel
        proxy = QSortFilterProxyModel()
        proxy.setSourceModel(model)

        # Relier le tableau aux donnees de la base de donnee
        self.page.listeUsage.setModel(proxy)

        # Cacher les colonnes inutiles
        self.page.listeUsage.setColumnHidden(0, True)  # colonne des id

    def supprimer_usage(self):
        selection_model = self.page.listeUsage.selectionModel()
        if selection_model.hasSelection():
            # Récupère la première ligne sélectionnée
            index = selection_model.currentIndex()
            row = index.row()

            # Récupère la valeur de la colonne 0 (id)
            id_to_delete = self.page.listeUsage.model().index(row, 0).data()
            print("ID sélectionné :", id_to_delete)

            # Suppression avec QSqlQuery
            self.model.supprimer_usage(id_to_delete)
            self.refresh_liste_usages()
        else:
            dlg = WarningDialog("Veuillez selectionner un element.", self.mainWin)
            dlg.exec()
