# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myApp.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(429, 204)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.grpName = QtWidgets.QGroupBox(self.centralwidget)
        self.grpName.setGeometry(QtCore.QRect(10, 10, 251, 161))
        self.grpName.setObjectName("grpName")
        self.edtLast = QtWidgets.QLineEdit(self.grpName)
        self.edtLast.setGeometry(QtCore.QRect(120, 60, 113, 20))
        self.edtLast.setObjectName("edtLast")
        self.lblLastName = QtWidgets.QLabel(self.grpName)
        self.lblLastName.setGeometry(QtCore.QRect(20, 60, 81, 16))
        self.lblLastName.setObjectName("lblLastName")
        self.lblFirstName = QtWidgets.QLabel(self.grpName)
        self.lblFirstName.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.lblFirstName.setObjectName("lblFirstName")
        self.edtFirstName = QtWidgets.QLineEdit(self.grpName)
        self.edtFirstName.setGeometry(QtCore.QRect(120, 20, 113, 20))
        self.edtFirstName.setObjectName("edtFirstName")
        self.lblGreetings = QtWidgets.QLabel(self.grpName)
        self.lblGreetings.setGeometry(QtCore.QRect(120, 120, 101, 16))
        self.lblGreetings.setText("")
        self.lblGreetings.setObjectName("lblGreetings")
        self.btnSayHi = QtWidgets.QPushButton(self.centralwidget)
        self.btnSayHi.setGeometry(QtCore.QRect(280, 50, 92, 27))
        self.btnSayHi.setObjectName("btnSayHi")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 429, 25))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        mainWindow.setTabOrder(self.edtFirstName, self.edtLast)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "First Qt Application"))
        self.grpName.setTitle(_translate("mainWindow", "Name"))
        self.edtLast.setProperty("placeholderText", _translate("mainWindow", "Last Name"))
        self.lblLastName.setText(_translate("mainWindow", "Last Name"))
        self.lblFirstName.setText(_translate("mainWindow", "First Name"))
        self.edtFirstName.setProperty("placeholderText", _translate("mainWindow", "First Name"))
        self.btnSayHi.setText(_translate("mainWindow", "Say Hi"))

