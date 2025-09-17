# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'warningDlg.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QWidget)
import Icons_rc

class Ui_w_warningDlg(object):
    def setupUi(self, w_warningDlg):
        if not w_warningDlg.objectName():
            w_warningDlg.setObjectName(u"w_warningDlg")
        w_warningDlg.resize(377, 187)
        icon = QIcon()
        icon.addFile(u":/utils/icon/crisis.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        w_warningDlg.setWindowIcon(icon)
        w_warningDlg.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.buttonBox = QDialogButtonBox(w_warningDlg)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(20, 140, 341, 32))
        self.buttonBox.setStyleSheet(u"background-color: rgb(147, 147, 145);")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)
        self.label = QLabel(w_warningDlg)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 30, 377, 91))
        font = QFont()
        font.setPointSize(14)
        font.setWeight(QFont.DemiBold)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet(u"background-color: rgb(222, 221, 218);\n"
"color: rgb(0, 0, 0);")
        self.label.setTextFormat(Qt.TextFormat.AutoText)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)

        self.retranslateUi(w_warningDlg)
        self.buttonBox.accepted.connect(w_warningDlg.accept)
        self.buttonBox.rejected.connect(w_warningDlg.reject)

        QMetaObject.connectSlotsByName(w_warningDlg)
    # setupUi

    def retranslateUi(self, w_warningDlg):
        w_warningDlg.setWindowTitle(QCoreApplication.translate("w_warningDlg", u"Avertissement", None))
        self.label.setText(QCoreApplication.translate("w_warningDlg", u"Mot de passe non identique.", None))
    # retranslateUi

