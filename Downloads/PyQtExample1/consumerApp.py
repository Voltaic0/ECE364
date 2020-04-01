
##############################
#### Lecture 11: GUI Programming with Python using PyQt5
##############################

"""
References:

* PyQt 5 Tutorials:                 http://zetcode.com/gui/pyqt5/
                                    https://doc.qt.io/qtforpython/tutorials/index.html

* References:
    - PyQt4:                        https://www.riverbankcomputing.com/static/Docs/PyQt4/classes.html
    - PyQt5:                        https://www.riverbankcomputing.com/static/Docs/PyQt5/
                                    https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qtwidgets-module.html
    - PySide 2:                     https://doc.qt.io/qtforpython/
                                    https://doc.qt.io/qtforpython/PySide2/QtWidgets/index.html
    - C++ Qt                        https://doc.qt.io/qt-5/classes.html

Creating a PyQt Application:

1- Create a UI file using the QtDesigner.

2- Convert the UI file to a Python file using the conversion tool:
    /package/eda/anaconda3/bin/pyuic5 <fileName.ui> -o <fileName.py>
   The generated file must NOT be modified, as indicated in the header warning!
   
3- Use the given file <blank.py> to create a consumer Python file, and write the code that drives the UI.

"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from myApp import *

class Consumer(QMainWindow, Ui_mainWindow):

    def __init__(self, parent=None):
        super(Consumer, self).__init__(parent)
        self.setupUi(self)

        self.btnSayHi.clicked.connect(self.displayName)

    def displayName(self):

        if self.edtFirstName.text() == 'Alex':
            message = "Another 'Alex'? No Way!"
        else:
            message = "Greetings, {} {}".format(self.edtFirstName.text(), self.edtLast.text())

        boxTitle = "Greetings From Qt"
        QMessageBox.information(self, boxTitle, message)


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()

