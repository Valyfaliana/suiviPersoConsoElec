from app.models.appareilModel import AppareilModel
from app.ui.pages.pageListeAppareils import PageListeAppareils
from PySide6.QtSql import QSqlDatabase, QSqlQueryModel

class ListeAppareilsController:
    def __init__(self, mainWin):
        from app.main_window import PAGE_CONNEXION
        self.mainWin = mainWin

        self.page = PageListeAppareils()
        self.view = self.page.widget
        self.model = AppareilModel()

        # Quand on clique sur le btn quitte
        self.page.btnQuitter.clicked.connect(lambda: mainWin.basculer_page("Connexion", PAGE_CONNEXION))

        # Btn ajouter appareil
        self.page.ajout_appareil_signal.connect(self.do_ajout_appareil)

    def refresh_liste_appareils(self):
        db = QSqlDatabase.database()

        # Recuperer les data de la base de donnee
        model = QSqlQueryModel()
        model.setQuery(f"SELECT nom,puissance FROM appareils WHERE user_id={self.mainWin.user["id"]}", db)

        if model.lastError().isValid():
            print("Erreur SQL :", model.lastError().text())

        # Relier le tableau aux donnees de la base de donnee
        self.page.listeAppareils.setModel(model)

    def do_ajout_appareil(self, nom:str, puissance:float):
        self.model.add_appareil(nom, puissance, self.mainWin.user["id"])
        self.refresh_liste_appareils()

