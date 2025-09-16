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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_w_signIn(object):
    def setupUi(self, w_signIn):
        if not w_signIn.objectName():
            w_signIn.setObjectName(u"w_signIn")
        w_signIn.resize(535, 446)
        self.frame = QFrame(w_signIn)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 191, 431))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayoutWidget = QWidget(w_signIn)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(230, 120, 281, 71))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.pseudoLabel = QLabel(self.formLayoutWidget)
        self.pseudoLabel.setObjectName(u"pseudoLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.pseudoLabel)

        self.pseudoLineEdit = QLineEdit(self.formLayoutWidget)
        self.pseudoLineEdit.setObjectName(u"pseudoLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.pseudoLineEdit)

        self.motDePasseLabel = QLabel(self.formLayoutWidget)
        self.motDePasseLabel.setObjectName(u"motDePasseLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.motDePasseLabel)

        self.motDePasseLineEdit = QLineEdit(self.formLayoutWidget)
        self.motDePasseLineEdit.setObjectName(u"motDePasseLineEdit")
        self.motDePasseLineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.motDePasseLineEdit)

        self.btnConnection = QPushButton(w_signIn)
        self.btnConnection.setObjectName(u"btnConnection")
        self.btnConnection.setGeometry(QRect(300, 230, 161, 26))
        self.btnInscription = QPushButton(w_signIn)
        self.btnInscription.setObjectName(u"btnInscription")
        self.btnInscription.setGeometry(QRect(330, 280, 94, 26))

        self.retranslateUi(w_signIn)

        QMetaObject.connectSlotsByName(w_signIn)
    # setupUi

    def retranslateUi(self, w_signIn):
        w_signIn.setWindowTitle(QCoreApplication.translate("w_signIn", u"Connection", None))
        self.pseudoLabel.setText(QCoreApplication.translate("w_signIn", u"Pseudo :", None))
        self.motDePasseLabel.setText(QCoreApplication.translate("w_signIn", u"Mot de passe :", None))
        self.btnConnection.setText(QCoreApplication.translate("w_signIn", u"Connecter", None))
        self.btnInscription.setText(QCoreApplication.translate("w_signIn", u"incription", None))
    # retranslateUi

