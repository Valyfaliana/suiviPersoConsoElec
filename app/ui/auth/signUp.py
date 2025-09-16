# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signUp.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_w_SignUpForm(object):
    def setupUi(self, w_SignUpForm):
        if not w_SignUpForm.objectName():
            w_SignUpForm.setObjectName(u"w_SignUpForm")
        w_SignUpForm.setEnabled(True)
        w_SignUpForm.resize(704, 494)
        w_SignUpForm.setAutoFillBackground(False)
        w_SignUpForm.setStyleSheet(u"background-color: rgb(153, 193, 241);")
        self.formFrame = QFrame(w_SignUpForm)
        self.formFrame.setObjectName(u"formFrame")
        self.formFrame.setGeometry(QRect(240, 150, 451, 161))
        self.formFrame.setStyleSheet(u"background-color: rgb(255, 120, 0);")
        self.formLayout = QFormLayout(self.formFrame)
        self.formLayout.setObjectName(u"formLayout")
        self.nomLabel = QLabel(self.formFrame)
        self.nomLabel.setObjectName(u"nomLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.nomLabel)

        self.prenomsLabel = QLabel(self.formFrame)
        self.prenomsLabel.setObjectName(u"prenomsLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.prenomsLabel)

        self.prenomsLineEdit = QLineEdit(self.formFrame)
        self.prenomsLineEdit.setObjectName(u"prenomsLineEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.prenomsLineEdit)

        self.emailLabel = QLabel(self.formFrame)
        self.emailLabel.setObjectName(u"emailLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.emailLabel)

        self.pseudoLineEdit = QLineEdit(self.formFrame)
        self.pseudoLineEdit.setObjectName(u"pseudoLineEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.pseudoLineEdit)

        self.passwordLabel = QLabel(self.formFrame)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.passwordLabel)

        self.passwordLineEdit = QLineEdit(self.formFrame)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.passwordLineEdit)

        self.password1Label = QLabel(self.formFrame)
        self.password1Label.setObjectName(u"password1Label")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.password1Label)

        self.passwordLineEdit_2 = QLineEdit(self.formFrame)
        self.passwordLineEdit_2.setObjectName(u"passwordLineEdit_2")
        self.passwordLineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.passwordLineEdit_2)

        self.nomLineEdit = QLineEdit(self.formFrame)
        self.nomLineEdit.setObjectName(u"nomLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nomLineEdit)

        self.verticalFrame = QFrame(w_SignUpForm)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setGeometry(QRect(10, 10, 221, 471))
        self.verticalFrame.setStyleSheet(u"background-color: rgb(255, 190, 111);")
        self.verticalLayout = QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnInscription = QPushButton(w_SignUpForm)
        self.btnInscription.setObjectName(u"btnInscription")
        self.btnInscription.setGeometry(QRect(360, 340, 191, 26))
        self.linkConnection = QLabel(w_SignUpForm)
        self.linkConnection.setObjectName(u"linkConnection")
        self.linkConnection.setGeometry(QRect(360, 380, 191, 51))
        self.linkConnection.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.linkConnection.setOpenExternalLinks(True)

        self.retranslateUi(w_SignUpForm)

        QMetaObject.connectSlotsByName(w_SignUpForm)
    # setupUi

    def retranslateUi(self, w_SignUpForm):
        w_SignUpForm.setWindowTitle(QCoreApplication.translate("w_SignUpForm", u"Inscription", None))
        self.nomLabel.setText(QCoreApplication.translate("w_SignUpForm", u"Nom :", None))
        self.prenomsLabel.setText(QCoreApplication.translate("w_SignUpForm", u"Prenoms :", None))
        self.emailLabel.setText(QCoreApplication.translate("w_SignUpForm", u"Pseudo :", None))
        self.passwordLabel.setText(QCoreApplication.translate("w_SignUpForm", u"Mot de passe :", None))
        self.password1Label.setText(QCoreApplication.translate("w_SignUpForm", u"Confirmer mot de passe : ", None))
        self.btnInscription.setText(QCoreApplication.translate("w_SignUpForm", u"S'inscrire", None))
        self.linkConnection.setText(QCoreApplication.translate("w_SignUpForm", u"<html><head/><body><a href=\"connecter\">connecter ?</a></body></html>", None))
    # retranslateUi

