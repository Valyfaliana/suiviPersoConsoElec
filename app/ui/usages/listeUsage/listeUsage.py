# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'listeUsage.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableView, QWidget)

class Ui_w_listeUsage(object):
    def setupUi(self, w_listeUsage):
        if not w_listeUsage.objectName():
            w_listeUsage.setObjectName(u"w_listeUsage")
        w_listeUsage.resize(567, 489)
        self.listeUsage = QTableView(w_listeUsage)
        self.listeUsage.setObjectName(u"listeUsage")
        self.listeUsage.setGeometry(QRect(20, 170, 531, 231))
        self.listeUsage.setSortingEnabled(True)
        self.label = QLabel(w_listeUsage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 70, 411, 71))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btnQuitter = QPushButton(w_listeUsage)
        self.btnQuitter.setObjectName(u"btnQuitter")
        self.btnQuitter.setGeometry(QRect(420, 20, 111, 31))
        self.btnListeAppareils = QPushButton(w_listeUsage)
        self.btnListeAppareils.setObjectName(u"btnListeAppareils")
        self.btnListeAppareils.setGeometry(QRect(40, 20, 121, 31))

        self.retranslateUi(w_listeUsage)

        QMetaObject.connectSlotsByName(w_listeUsage)
    # setupUi

    def retranslateUi(self, w_listeUsage):
        w_listeUsage.setWindowTitle(QCoreApplication.translate("w_listeUsage", u"Liste d'utilisation", None))
        self.label.setText(QCoreApplication.translate("w_listeUsage", u"Vos consommations electrique", None))
        self.btnQuitter.setText(QCoreApplication.translate("w_listeUsage", u"Quitter", None))
        self.btnListeAppareils.setText(QCoreApplication.translate("w_listeUsage", u"Appareils", None))
    # retranslateUi

