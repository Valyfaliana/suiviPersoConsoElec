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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import Icons_rc

class Ui_w_SignUpForm(object):
    def setupUi(self, w_SignUpForm):
        if not w_SignUpForm.objectName():
            w_SignUpForm.setObjectName(u"w_SignUpForm")
        w_SignUpForm.setEnabled(True)
        w_SignUpForm.resize(534, 446)
        w_SignUpForm.setAutoFillBackground(False)
        w_SignUpForm.setStyleSheet(u"background-color: rgb(241, 240, 240);\n"
"color: rgb(0, 0, 0);")
        self.formFrame = QFrame(w_SignUpForm)
        self.formFrame.setObjectName(u"formFrame")
        self.formFrame.setGeometry(QRect(200, 160, 321, 161))
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

        self.btnInscription = QPushButton(w_SignUpForm)
        self.btnInscription.setObjectName(u"btnInscription")
        self.btnInscription.setGeometry(QRect(260, 330, 191, 31))
        font = QFont()
        font.setBold(True)
        self.btnInscription.setFont(font)
        self.btnInscription.setStyleSheet(u"background-color: rgb(38, 152, 207);\n"
"color: rgb(255, 255, 255);")
        self.btnInscription.setAutoDefault(False)
        self.btnInscription.setFlat(False)
        self.btnConnecter = QPushButton(w_SignUpForm)
        self.btnConnecter.setObjectName(u"btnConnecter")
        self.btnConnecter.setGeometry(QRect(260, 370, 191, 31))
        self.btnConnecter.setFont(font)
        self.btnConnecter.setStyleSheet(u"background-color: rgb(153, 153, 153);\n"
"color: rgb(255, 255, 255);")
        self.partieGauche = QGroupBox(w_SignUpForm)
        self.partieGauche.setObjectName(u"partieGauche")
        self.partieGauche.setGeometry(QRect(-10, 0, 191, 451))
        self.partieGauche.setStyleSheet(u"background-color: rgb(38, 152, 207);\n"
"color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(self.partieGauche)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.partieGauche)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(19)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.partieGauche)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_3 = QLabel(w_SignUpForm)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(290, 0, 151, 151))
        self.label_3.setPixmap(QPixmap(u":/Main/icon/mainLog.png"))
        self.label_3.setScaledContents(True)

        self.retranslateUi(w_SignUpForm)

        self.btnInscription.setDefault(False)


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
        self.btnConnecter.setText(QCoreApplication.translate("w_SignUpForm", u"se connecter ?", None))
        self.label.setText(QCoreApplication.translate("w_SignUpForm", u"<html><head/><body><p><span style=\" font-style:italic; color:#66a23c;\">ECO</span><span style=\" font-style:italic;\">WATT</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("w_SignUpForm", u"G\u00e9rez votre \u00e9nergie, sans prise de t\u00eate.", None))
        self.label_3.setText("")
    # retranslateUi

