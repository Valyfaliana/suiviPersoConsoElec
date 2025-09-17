# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signIn.ui'
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

class Ui_w_signIn(object):
    def setupUi(self, w_signIn):
        if not w_signIn.objectName():
            w_signIn.setObjectName(u"w_signIn")
        w_signIn.resize(534, 446)
        w_signIn.setStyleSheet(u"background-color: rgb(246, 245, 244);\n"
"color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.formFrame = QFrame(w_signIn)
        self.formFrame.setObjectName(u"formFrame")
        self.formFrame.setGeometry(QRect(220, 260, 291, 81))
        self.formLayout = QFormLayout(self.formFrame)
        self.formLayout.setObjectName(u"formLayout")
        self.pseudoLabel = QLabel(self.formFrame)
        self.pseudoLabel.setObjectName(u"pseudoLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.pseudoLabel)

        self.pseudoLineEdit = QLineEdit(self.formFrame)
        self.pseudoLineEdit.setObjectName(u"pseudoLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.pseudoLineEdit)

        self.motDePasseLabel = QLabel(self.formFrame)
        self.motDePasseLabel.setObjectName(u"motDePasseLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.motDePasseLabel)

        self.motDePasseLineEdit = QLineEdit(self.formFrame)
        self.motDePasseLineEdit.setObjectName(u"motDePasseLineEdit")
        self.motDePasseLineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.motDePasseLineEdit)

        self.partieGauche = QGroupBox(w_signIn)
        self.partieGauche.setObjectName(u"partieGauche")
        self.partieGauche.setGeometry(QRect(0, 0, 191, 451))
        self.partieGauche.setStyleSheet(u"background-color: rgb(38, 152, 207);\n"
"color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(self.partieGauche)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.partieGauche)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(19)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.partieGauche)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_3 = QLabel(w_signIn)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(290, 40, 151, 151))
        self.label_3.setPixmap(QPixmap(u":/Main/icon/mainLog.png"))
        self.label_3.setScaledContents(True)
        self.groupBtn = QFrame(w_signIn)
        self.groupBtn.setObjectName(u"groupBtn")
        self.groupBtn.setGeometry(QRect(250, 350, 241, 81))
        self.verticalLayout_2 = QVBoxLayout(self.groupBtn)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btnConnection = QPushButton(self.groupBtn)
        self.btnConnection.setObjectName(u"btnConnection")
        font1 = QFont()
        font1.setBold(True)
        self.btnConnection.setFont(font1)
        self.btnConnection.setStyleSheet(u"background-color: rgb(38, 152, 207);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.btnConnection)

        self.btnInscription = QPushButton(self.groupBtn)
        self.btnInscription.setObjectName(u"btnInscription")

        self.verticalLayout_2.addWidget(self.btnInscription)


        self.retranslateUi(w_signIn)

        QMetaObject.connectSlotsByName(w_signIn)
    # setupUi

    def retranslateUi(self, w_signIn):
        w_signIn.setWindowTitle(QCoreApplication.translate("w_signIn", u"Connection", None))
        self.pseudoLabel.setText(QCoreApplication.translate("w_signIn", u"Pseudo :", None))
        self.motDePasseLabel.setText(QCoreApplication.translate("w_signIn", u"Mot de passe :", None))
        self.label.setText(QCoreApplication.translate("w_signIn", u"<html><head/><body><p><span style=\" color:#66a23c;\">ECO</span>WATT</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("w_signIn", u"G\u00e9rez votre \u00e9nergie, sans prise de t\u00eate.", None))
        self.label_3.setText("")
        self.btnConnection.setText(QCoreApplication.translate("w_signIn", u"Connecter", None))
        self.btnInscription.setText(QCoreApplication.translate("w_signIn", u"S'inscrire ?", None))
    # retranslateUi

