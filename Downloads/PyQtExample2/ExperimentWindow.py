# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ExperimentWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(387, 264)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblName = QtWidgets.QLabel(self.centralwidget)
        self.lblName.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.lblName.setObjectName("lblName")
        self.lblMessage = QtWidgets.QLabel(self.centralwidget)
        self.lblMessage.setGeometry(QtCore.QRect(10, 120, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lblMessage.setFont(font)
        self.lblMessage.setText("")
        self.lblMessage.setObjectName("lblMessage")
        self.txtName = QtWidgets.QLineEdit(self.centralwidget)
        self.txtName.setGeometry(QtCore.QRect(140, 30, 113, 20))
        self.txtName.setText("")
        self.txtName.setObjectName("txtName")
        self.btnShow = QtWidgets.QPushButton(self.centralwidget)
        self.btnShow.setGeometry(QtCore.QRect(20, 90, 101, 23))
        self.btnShow.setObjectName("btnShow")
        self.chkItalic = QtWidgets.QCheckBox(self.centralwidget)
        self.chkItalic.setGeometry(QtCore.QRect(280, 30, 70, 17))
        self.chkItalic.setChecked(True)
        self.chkItalic.setObjectName("chkItalic")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 387, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblName.setText(_translate("MainWindow", "Full Name"))
        self.btnShow.setText(_translate("MainWindow", "Show Name"))
        self.chkItalic.setText(_translate("MainWindow", "Italic"))

