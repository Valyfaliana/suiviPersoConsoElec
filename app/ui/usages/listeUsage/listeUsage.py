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
import Icons_rc
import Icons_rc

class Ui_w_listeUsage(object):
    def setupUi(self, w_listeUsage):
        if not w_listeUsage.objectName():
            w_listeUsage.setObjectName(u"w_listeUsage")
        w_listeUsage.resize(561, 408)
        w_listeUsage.setStyleSheet(u"background-color: rgb(213, 212, 210);\n"
"color: rgb(0, 0, 0);")
        self.listeUsage = QTableView(w_listeUsage)
        self.listeUsage.setObjectName(u"listeUsage")
        self.listeUsage.setGeometry(QRect(20, 150, 521, 211))
        self.listeUsage.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(147, 147, 145);")
        self.listeUsage.setSortingEnabled(True)
        self.listeUsage.horizontalHeader().setStretchLastSection(True)
        self.listeUsage.verticalHeader().setDefaultSectionSize(35)
        self.label = QLabel(w_listeUsage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(89, 80, 411, 61))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btnQuitter = QPushButton(w_listeUsage)
        self.btnQuitter.setObjectName(u"btnQuitter")
        self.btnQuitter.setGeometry(QRect(450, 0, 111, 41))
        self.btnQuitter.setStyleSheet(u"background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u":/utils/icon/disruption (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnQuitter.setIcon(icon)
        self.btnListeAppareils = QPushButton(w_listeUsage)
        self.btnListeAppareils.setObjectName(u"btnListeAppareils")
        self.btnListeAppareils.setGeometry(QRect(320, 0, 121, 41))
        self.btnListeAppareils.setStyleSheet(u"background-color: rgb(102, 162, 60);\n"
"color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u":/utils/icon/responsive (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnListeAppareils.setIcon(icon1)
        self.label_3 = QLabel(w_listeUsage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 41, 41))
        self.label_3.setPixmap(QPixmap(u":/Main/icon/mainLog.png"))
        self.label_3.setScaledContents(True)

        self.retranslateUi(w_listeUsage)

        QMetaObject.connectSlotsByName(w_listeUsage)
    # setupUi

    def retranslateUi(self, w_listeUsage):
        w_listeUsage.setWindowTitle(QCoreApplication.translate("w_listeUsage", u"Liste d'utilisation", None))
        self.label.setText(QCoreApplication.translate("w_listeUsage", u"Vos consommations electrique", None))
        self.btnQuitter.setText(QCoreApplication.translate("w_listeUsage", u"Deconnecter", None))
        self.btnListeAppareils.setText(QCoreApplication.translate("w_listeUsage", u"Appareils", None))
        self.label_3.setText("")
    # retranslateUi

