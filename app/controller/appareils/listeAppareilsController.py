from app.controller.usages.ajoutUsageController import AjoutUsageController
from app.models.appareilModel import AppareilModel
from app.ui.pages.pageListeAppareils import PageListeAppareils
from PySide6.QtSql import QSqlTableModel
from PySide6.QtCore import QSortFilterProxyModel

class ListeAppareilsController:
    def __init__(self, mainWin):
        from app.main_window import PAGE_CONNEXION, PAGE_LISTE_USAGES
        self.mainWin = mainWin

        self.page = PageListeAppareils()
        self.view = self.page.widget
        self.model = AppareilModel()

        # Quand on clique sur le btn quitte
        self.page.btnQuitter.clicked.connect(lambda: mainWin.basculer_page("Connexion", PAGE_CONNEXION))

        # Quand on clique sur le btn consommation
        self.page.btnListeUsages.clicked.connect(lambda: mainWin.basculer_page("Liste consommation", PAGE_LISTE_USAGES))

        # Btn ajouter appareil
        self.page.ajout_appareil_signal.connect(self.do_ajout_appareil)

        # Btn suppression appareils
        self.page.btnSupprimer.clicked.connect(self.supprimer_appareils)

        # Btn utilisation appareils
        self.page.btnUtiliser.clicked.connect(self.utiliser_appareil)

    def refresh_liste_appareils(self):
        # Recuperer les data de la base de donnee
        model = QSqlTableModel()
        model.setTable("appareils")
        model.setFilter(f"user_id={self.mainWin.user["id"]}")
        model.select()

        # Proxy pour tri/filtre
        proxy = QSortFilterProxyModel()
        proxy.setSourceModel(model)

        # Relier le tableau aux donnees de la base de donnee
        self.page.listeAppareils.setModel(proxy)

        # Cacher les colonnes inutiles
        self.page.listeAppareils.setColumnHidden(0, True) # colonne des id
        self.page.listeAppareils.setColumnHidden(3, True) # colonne des user_id

    def do_ajout_appareil(self, nom:str, puissance:float):
        self.model.add_appareil(nom, puissance, self.mainWin.user["id"])
        self.refresh_liste_appareils()

    def supprimer_appareils(self):
        model = QSqlTableModel()
        model.setTable("appareils")
        model.select()

        # Recuperer les elements selectionnee
        selected = self.page.listeAppareils.selectionModel().selectedRows()
        # Recuperer le proxy connect au tableview
        proxy = self.page.listeAppareils.model()
        for index in selected:
            # Conversion index proxy -> index modèle source
            source_index = proxy.mapToSource(index)
            model.removeRow(source_index.row())

        self.refresh_liste_appareils()

    def utiliser_appareil(self):
        from app.main_window import PAGE_LISTE_USAGES

        model = QSqlTableModel()
        model.setTable("appareils")
        model.select()

        # Recuperer les elements selectionnee
        selected = self.page.listeAppareils.selectionModel().selectedRows()
        if len(selected) <= 0:
            return

        # Recuperer le proxy connect au tableview
        proxy = self.page.listeAppareils.model()

        # Conversion index proxy -> index modèle source
        source_index = proxy.mapToSource(selected[0])
        record = model.record(source_index.row()) # recuperer les data de l'appareil

        # Afficher la boite de dialog pour l'ajout de usage
        usage_controller = AjoutUsageController(record, self.mainWin)
        usage_controller.view.exec()

        # Basculer a la page liste usage
        self.mainWin.basculer_page("Liste consommation", PAGE_LISTE_USAGES)

