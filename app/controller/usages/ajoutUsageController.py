from app.models.usageModel import UsageModel
from app.ui.usages.dialogAjout.dialogAjoutUsage import DialogAjoutUsage


class AjoutUsageController:
    def __init__(self, recordAppareil, mainWin=None):
        self.appreil = recordAppareil
        self.view = DialogAjoutUsage(recordAppareil.value("nom"), mainWin)
        self.model = UsageModel()
        self.user = mainWin.user

        # Quand il y a enregistrement d'usage
        self.view.ajout_usage_signal.connect(self.do_ajout_usage)

    def do_ajout_usage(self, duree, date_usage):
        self.model.add_usage(duree, date_usage, self.appreil.value("id"), self.user["id"])

