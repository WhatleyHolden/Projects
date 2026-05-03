# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'asn8.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setMinimumSize(QSize(500, 300))
        MainWindow.setMaximumSize(QSize(500, 300))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.PInfo = QGroupBox(self.centralwidget)
        self.PInfo.setObjectName(u"PInfo")
        self.PInfo.setGeometry(QRect(0, 0, 291, 181))
        self.gridLayout = QGridLayout(self.PInfo)
        self.gridLayout.setObjectName(u"gridLayout")
        self.LastName = QLineEdit(self.PInfo)
        self.LastName.setObjectName(u"LastName")

        self.gridLayout.addWidget(self.LastName, 2, 1, 1, 1)

        self.Last = QLabel(self.PInfo)
        self.Last.setObjectName(u"Last")
        self.Last.setStyleSheet(u"background-color: blue;\n"
"color: white;")

        self.gridLayout.addWidget(self.Last, 2, 0, 1, 1)

        self.Email = QLabel(self.PInfo)
        self.Email.setObjectName(u"Email")

        self.gridLayout.addWidget(self.Email, 3, 0, 1, 1)

        self.Email_2 = QLineEdit(self.PInfo)
        self.Email_2.setObjectName(u"Email_2")

        self.gridLayout.addWidget(self.Email_2, 3, 1, 1, 1)

        self.PhoneNumber = QLineEdit(self.PInfo)
        self.PhoneNumber.setObjectName(u"PhoneNumber")

        self.gridLayout.addWidget(self.PhoneNumber, 4, 1, 1, 1)

        self.First = QLabel(self.PInfo)
        self.First.setObjectName(u"First")
        self.First.setStyleSheet(u"background-color: blue;\n"
"color: white;")

        self.gridLayout.addWidget(self.First, 0, 0, 1, 1)

        self.FirstName = QLineEdit(self.PInfo)
        self.FirstName.setObjectName(u"FirstName")

        self.gridLayout.addWidget(self.FirstName, 0, 1, 1, 1)

        self.Phone = QLabel(self.PInfo)
        self.Phone.setObjectName(u"Phone")

        self.gridLayout.addWidget(self.Phone, 4, 0, 1, 1)

        self.Buttons = QFrame(self.centralwidget)
        self.Buttons.setObjectName(u"Buttons")
        self.Buttons.setGeometry(QRect(0, 180, 501, 91))
        self.Buttons.setFrameShape(QFrame.StyledPanel)
        self.Buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Buttons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Submit = QPushButton(self.Buttons)
        self.Submit.setObjectName(u"Submit")

        self.horizontalLayout.addWidget(self.Submit)

        self.Reset = QPushButton(self.Buttons)
        self.Reset.setObjectName(u"Reset")

        self.horizontalLayout.addWidget(self.Reset)

        self.Quit = QPushButton(self.Buttons)
        self.Quit.setObjectName(u"Quit")

        self.horizontalLayout.addWidget(self.Quit)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.PInfo.setTitle(QCoreApplication.translate("MainWindow", u"Personal Information", None))
        self.Last.setText(QCoreApplication.translate("MainWindow", u"Last Name:", None))
        self.Email.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.First.setText(QCoreApplication.translate("MainWindow", u"First Name:", None))
        self.Phone.setText(QCoreApplication.translate("MainWindow", u"Phone:", None))
        self.Submit.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.Reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.Quit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
    # retranslateUi

