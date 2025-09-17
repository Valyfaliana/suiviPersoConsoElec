# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'listeAppareils.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDoubleSpinBox, QFormLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableView, QWidget)
import Icons_rc

class Ui_w_listeAppareils(object):
    def setupUi(self, w_listeAppareils):
        if not w_listeAppareils.objectName():
            w_listeAppareils.setObjectName(u"w_listeAppareils")
        w_listeAppareils.resize(561, 572)
        w_listeAppareils.setStyleSheet(u"background-color: rgb(213, 212, 210);\n"
"color: rgb(0, 0, 0);")
        self.listeAppareils = QTableView(w_listeAppareils)
        self.listeAppareils.setObjectName(u"listeAppareils")
        self.listeAppareils.setGeometry(QRect(20, 150, 521, 211))
        self.listeAppareils.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(147, 147, 145);\n"
"\n"
"\n"
"")
        self.listeAppareils.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed|QAbstractItemView.EditTrigger.DoubleClicked|QAbstractItemView.EditTrigger.EditKeyPressed)
        self.listeAppareils.setGridStyle(Qt.PenStyle.SolidLine)
        self.listeAppareils.setSortingEnabled(True)
        self.listeAppareils.horizontalHeader().setCascadingSectionResizes(False)
        self.listeAppareils.horizontalHeader().setStretchLastSection(True)
        self.listeAppareils.verticalHeader().setCascadingSectionResizes(False)
        self.listeAppareils.verticalHeader().setMinimumSectionSize(24)
        self.listeAppareils.verticalHeader().setDefaultSectionSize(35)
        self.formLayoutWidget = QWidget(w_listeAppareils)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(120, 430, 331, 61))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.nomAppareilLabel = QLabel(self.formLayoutWidget)
        self.nomAppareilLabel.setObjectName(u"nomAppareilLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.nomAppareilLabel)

        self.nomAppareilLineEdit = QLineEdit(self.formLayoutWidget)
        self.nomAppareilLineEdit.setObjectName(u"nomAppareilLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nomAppareilLineEdit)

        self.puissanceConsommerLabel = QLabel(self.formLayoutWidget)
        self.puissanceConsommerLabel.setObjectName(u"puissanceConsommerLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.puissanceConsommerLabel)

        self.puissanceConsommerDoubleSpinBox = QDoubleSpinBox(self.formLayoutWidget)
        self.puissanceConsommerDoubleSpinBox.setObjectName(u"puissanceConsommerDoubleSpinBox")
        self.puissanceConsommerDoubleSpinBox.setDecimals(2)
        self.puissanceConsommerDoubleSpinBox.setMaximum(50000.000000000000000)
        self.puissanceConsommerDoubleSpinBox.setSingleStep(10.000000000000000)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.puissanceConsommerDoubleSpinBox)

        self.btnQuitter = QPushButton(w_listeAppareils)
        self.btnQuitter.setObjectName(u"btnQuitter")
        self.btnQuitter.setGeometry(QRect(450, 0, 111, 41))
        self.btnQuitter.setStyleSheet(u"background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u":/utils/icon/disruption (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnQuitter.setIcon(icon)
        self.btnSupprimer = QPushButton(w_listeAppareils)
        self.btnSupprimer.setObjectName(u"btnSupprimer")
        self.btnSupprimer.setGeometry(QRect(310, 380, 141, 31))
        self.btnSupprimer.setStyleSheet(u"background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.btnSupprimer.setIcon(icon1)
        self.btnUtiliser = QPushButton(w_listeAppareils)
        self.btnUtiliser.setObjectName(u"btnUtiliser")
        self.btnUtiliser.setGeometry(QRect(120, 380, 141, 31))
        self.btnUtiliser.setStyleSheet(u"background-color: rgb(102, 162, 60);\n"
"color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u":/utils/icon/clock (2).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnUtiliser.setIcon(icon2)
        self.btnListeUsages = QPushButton(w_listeAppareils)
        self.btnListeUsages.setObjectName(u"btnListeUsages")
        self.btnListeUsages.setGeometry(QRect(320, 0, 121, 41))
        self.btnListeUsages.setStyleSheet(u"background-color: rgb(102, 162, 60);\n"
"color: rgb(255, 255, 255);")
        icon3 = QIcon()
        icon3.addFile(u":/utils/icon/responsible-consumption (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnListeUsages.setIcon(icon3)
        self.btnAjouterAppareil = QPushButton(w_listeAppareils)
        self.btnAjouterAppareil.setObjectName(u"btnAjouterAppareil")
        self.btnAjouterAppareil.setGeometry(QRect(220, 500, 131, 31))
        font = QFont()
        font.setBold(True)
        self.btnAjouterAppareil.setFont(font)
        self.btnAjouterAppareil.setStyleSheet(u"background-color: rgb(38, 152, 207);\n"
"color: rgb(255, 255, 255);")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.btnAjouterAppareil.setIcon(icon4)
        self.labelBienvenue = QLabel(w_listeAppareils)
        self.labelBienvenue.setObjectName(u"labelBienvenue")
        self.labelBienvenue.setGeometry(QRect(130, 80, 311, 61))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.labelBienvenue.setFont(font1)
        self.labelBienvenue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelBienvenue.setWordWrap(True)
        self.label_3 = QLabel(w_listeAppareils)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 41, 41))
        self.label_3.setPixmap(QPixmap(u":/Main/icon/mainLog.png"))
        self.label_3.setScaledContents(True)
        self.label = QLabel(w_listeAppareils)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 540, 531, 21))

        self.retranslateUi(w_listeAppareils)

        QMetaObject.connectSlotsByName(w_listeAppareils)
    # setupUi

    def retranslateUi(self, w_listeAppareils):
        w_listeAppareils.setWindowTitle(QCoreApplication.translate("w_listeAppareils", u"Liste des appareils de l'utilisateur", None))
#if QT_CONFIG(tooltip)
        self.listeAppareils.setToolTip(QCoreApplication.translate("w_listeAppareils", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.nomAppareilLabel.setText(QCoreApplication.translate("w_listeAppareils", u"Nom appareil :", None))
        self.puissanceConsommerLabel.setText(QCoreApplication.translate("w_listeAppareils", u"Puissance consommer :", None))
        self.btnQuitter.setText(QCoreApplication.translate("w_listeAppareils", u"Deconnecter", None))
        self.btnSupprimer.setText(QCoreApplication.translate("w_listeAppareils", u"supprimer", None))
        self.btnUtiliser.setText(QCoreApplication.translate("w_listeAppareils", u"Utiliser", None))
        self.btnListeUsages.setText(QCoreApplication.translate("w_listeAppareils", u"Consommation", None))
        self.btnAjouterAppareil.setText(QCoreApplication.translate("w_listeAppareils", u"Ajouter", None))
        self.labelBienvenue.setText(QCoreApplication.translate("w_listeAppareils", u"<html><head/><body><p>Texte</p></body></html>", None))
        self.label_3.setText("")
        self.label.setText(QCoreApplication.translate("w_listeAppareils", u"*Astuce : cliquer sur le numero de ligne pour selectionner un element", None))
    # retranslateUi

