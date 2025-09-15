# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginForm.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_w_loginForm(object):
    def setupUi(self, w_loginForm):
        if not w_loginForm.objectName():
            w_loginForm.setObjectName(u"w_loginForm")
        w_loginForm.resize(488, 462)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(w_loginForm.sizePolicy().hasHeightForWidth())
        w_loginForm.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QWidget(w_loginForm)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 10, 451, 391))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(w_loginForm)

        QMetaObject.connectSlotsByName(w_loginForm)
    # setupUi

    def retranslateUi(self, w_loginForm):
        w_loginForm.setWindowTitle(QCoreApplication.translate("w_loginForm", u"Login", None))
        self.label.setText(QCoreApplication.translate("w_loginForm", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("w_loginForm", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("w_loginForm", u"PushButton", None))
    # retranslateUi

