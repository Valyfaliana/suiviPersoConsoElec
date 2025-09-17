# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlgAjoutUsage.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDateEdit, QDialog,
    QDialogButtonBox, QDoubleSpinBox, QFormLayout, QLabel,
    QSizePolicy, QWidget)

class Ui_d_ajoutUsage(object):
    def setupUi(self, d_ajoutUsage):
        if not d_ajoutUsage.objectName():
            d_ajoutUsage.setObjectName(u"d_ajoutUsage")
        d_ajoutUsage.resize(400, 300)
        self.buttonBox = QDialogButtonBox(d_ajoutUsage)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)
        self.buttonBox.setCenterButtons(True)
        self.formLayoutWidget = QWidget(d_ajoutUsage)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 110, 381, 80))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.dureeDUtilisationLabel = QLabel(self.formLayoutWidget)
        self.dureeDUtilisationLabel.setObjectName(u"dureeDUtilisationLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.dureeDUtilisationLabel)

        self.dureeDUtilisationDoubleSpinBox = QDoubleSpinBox(self.formLayoutWidget)
        self.dureeDUtilisationDoubleSpinBox.setObjectName(u"dureeDUtilisationDoubleSpinBox")
        self.dureeDUtilisationDoubleSpinBox.setMaximum(100.000000000000000)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.dureeDUtilisationDoubleSpinBox)

        self.dateDUtilisationLabel = QLabel(self.formLayoutWidget)
        self.dateDUtilisationLabel.setObjectName(u"dateDUtilisationLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.dateDUtilisationLabel)

        self.dateDUtilisationDateEdit = QDateEdit(self.formLayoutWidget)
        self.dateDUtilisationDateEdit.setObjectName(u"dateDUtilisationDateEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.dateDUtilisationDateEdit)

        self.nomAppareil = QLabel(d_ajoutUsage)
        self.nomAppareil.setObjectName(u"nomAppareil")
        self.nomAppareil.setGeometry(QRect(120, 40, 161, 41))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.nomAppareil.setFont(font)
        self.nomAppareil.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(d_ajoutUsage)
        self.buttonBox.accepted.connect(d_ajoutUsage.accept)
        self.buttonBox.rejected.connect(d_ajoutUsage.reject)

        QMetaObject.connectSlotsByName(d_ajoutUsage)
    # setupUi

    def retranslateUi(self, d_ajoutUsage):
        d_ajoutUsage.setWindowTitle(QCoreApplication.translate("d_ajoutUsage", u"Enregistrement", None))
        self.dureeDUtilisationLabel.setText(QCoreApplication.translate("d_ajoutUsage", u"Duree d'utilisation :", None))
        self.dateDUtilisationLabel.setText(QCoreApplication.translate("d_ajoutUsage", u"Date d'utilisation :", None))
        self.nomAppareil.setText(QCoreApplication.translate("d_ajoutUsage", u"TextLabel", None))
    # retranslateUi

