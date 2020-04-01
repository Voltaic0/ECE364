#######################################################
#   Author:     Mark Dunn
#   email:      dunn60
#   ID:         ee364a12
#   Date:       11/12/19
#######################################################


# Import PyQt5 classes
import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
import re

from calculator import *

class MathConsumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MathConsumer, self).__init__(parent)
        self.setupUi(self)

        self.btnCalculate.clicked.connect(self.performOperation)


    def performOperation(self):
        operand1 = self.edtNumber1.displayText()
        operand2 = self.edtNumber2.displayText()
        if operand1 == "" or operand2 == "":
            self.edtResult.setText("E")
            return
        try:
            floats = re.search(r"\.",operand1)
            floats2 = re.search(r"\.",operand2)
            if floats == None and floats2 == None:
                op1 = int(operand1)
                op2 = int(operand2)
            else:
                op1 = float(operand1)
                op2 = float(operand2)
        except ValueError:
            self.edtResult.setText("E")
            return

        self.edtResult.setText("Testing")
        operation = self.cboOperation.currentText()

        if operation == "+":
            self.edtResult.setText(str(op1+op2))
        elif operation == "*":
            self.edtResult.setText(str(op1 * op2))
        elif operation == "-":
            self.edtResult.setText(str(op1 - op2))
        else:
            res = float(op1) / float(op2)
            self.edtResult.setText(str(res))



if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = MathConsumer()

    currentForm.show()
    sys.exit(currentApp.exec_())