# Import PyQt5 classes
import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication

from ExperimentWindow import *

class ConsumerApp(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(ConsumerApp, self).__init__(parent)
        self.setupUi(self)

        self.chkItalic.setDisabled(True)

        self.btnShow.clicked.connect(self.displayName)
        self.chkItalic.stateChanged.connect(self.modifyItalic)
        self.txtName.textChanged.connect(self.enableCheck)


    def enableCheck(self):
        self.chkItalic.setEnabled(True)

    def displayName(self):

        fullName = self.txtName.text()
        self.lblMessage.setText(fullName)

    def modifyItalic(self):

        isChecked = self.chkItalic.isChecked()

        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setItalic(isChecked)
        font.setBold(True)
        self.lblMessage.setFont(font)


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = ConsumerApp()

    currentForm.show()
    currentApp.exec_()
