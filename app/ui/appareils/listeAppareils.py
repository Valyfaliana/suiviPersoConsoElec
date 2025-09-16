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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFormLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableView, QWidget)

class Ui_w_listeAppareils(object):
    def setupUi(self, w_listeAppareils):
        if not w_listeAppareils.objectName():
            w_listeAppareils.setObjectName(u"w_listeAppareils")
        w_listeAppareils.resize(579, 459)
        self.listeAppareils = QTableView(w_listeAppareils)
        self.listeAppareils.setObjectName(u"listeAppareils")
        self.listeAppareils.setGeometry(QRect(0, 40, 561, 211))
        self.listeAppareils.setGridStyle(Qt.PenStyle.SolidLine)
        self.listeAppareils.setSortingEnabled(True)
        self.listeAppareils.horizontalHeader().setCascadingSectionResizes(False)
        self.formLayoutWidget = QWidget(w_listeAppareils)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 270, 551, 141))
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

        self.btnAjouterAppareil = QPushButton(self.formLayoutWidget)
        self.btnAjouterAppareil.setObjectName(u"btnAjouterAppareil")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.btnAjouterAppareil)

        self.btnQuitter = QPushButton(w_listeAppareils)
        self.btnQuitter.setObjectName(u"btnQuitter")
        self.btnQuitter.setGeometry(QRect(390, 0, 181, 31))

        self.retranslateUi(w_listeAppareils)

        QMetaObject.connectSlotsByName(w_listeAppareils)
    # setupUi

    def retranslateUi(self, w_listeAppareils):
        w_listeAppareils.setWindowTitle(QCoreApplication.translate("w_listeAppareils", u"Liste des appareils de l'utilisateur", None))
        self.nomAppareilLabel.setText(QCoreApplication.translate("w_listeAppareils", u"Nom appareil :", None))
        self.puissanceConsommerLabel.setText(QCoreApplication.translate("w_listeAppareils", u"Puissance consommer :", None))
        self.btnAjouterAppareil.setText(QCoreApplication.translate("w_listeAppareils", u"Ajouter", None))
        self.btnQuitter.setText(QCoreApplication.translate("w_listeAppareils", u"Quitter", None))
    # retranslateUi

