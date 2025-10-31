# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowAeHrKB.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"	background-color: black;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color:  rgb(58, 205, 213);\n"
"	min-height: 40px;\n"
"	border-radious: 5px;\n"
"	padding-left: 20px;\n"
"	font-size: 15px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color:  rgb(246, 28, 91);\n"
"	min-height: 40px;\n"
"	border-radious: 5px;\n"
"	font-size: 15px;\n"
"	font-weight: bold;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 196, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setMaximumSize(QSize(300, 100))
        self.logo.setPixmap(QPixmap(u"tiktok-downloader/download.gif"))
        self.logo.setScaledContents(True)

        self.verticalLayout.addWidget(self.logo, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.link_edit = QLineEdit(self.frame)
        self.link_edit.setObjectName(u"link_edit")

        self.horizontalLayout.addWidget(self.link_edit)

        self.download_button = QPushButton(self.frame)
        self.download_button.setObjectName(u"download_button")
        self.download_button.setMinimumSize(QSize(130, 42))

        self.horizontalLayout.addWidget(self.download_button)


        self.verticalLayout.addWidget(self.frame)

        self.verticalSpacer_2 = QSpacerItem(20, 196, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText("")
        self.link_edit.setText("")
        self.link_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Insert the video link here", None))
        self.download_button.setText(QCoreApplication.translate("MainWindow", u"Download", None))
    # retranslateUi

