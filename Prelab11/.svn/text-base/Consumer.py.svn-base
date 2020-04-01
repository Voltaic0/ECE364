
#######################################################
#   Author:     <Your Full Name>
#   email:      <Your Email>
#   ID:         <Your course ID, e.g. ee364j20>
#   Date:       <Start Date>
#######################################################

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from BasicUI import *
import re


class Consumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)

        self.btnSave.setDisabled(True)
        self.btnLoad.clicked.connect(self.loadData)
        self.btnClear.clicked.connect(self.clearState)
        self.componentCountList = [self.txtComponentCount_1, self.txtComponentCount_2, self.txtComponentCount_3,
                                  self.txtComponentCount_4, self.txtComponentCount_5, self.txtComponentCount_6,
                                  self.txtComponentCount_7, self.txtComponentCount_8, self.txtComponentCount_9,
                                  self.txtComponentCount_10, self.txtComponentCount_11, self.txtComponentCount_12,
                                  self.txtComponentCount_13, self.txtComponentCount_14, self.txtComponentCount_15,
                                  self.txtComponentCount_16, self.txtComponentCount_17, self.txtComponentCount_18,
                                  self.txtComponentCount_19, self.txtComponentCount_20]
        self.componentNameList = [self.txtComponentName_1, self.txtComponentName_2, self.txtComponentName_3,
                                  self.txtComponentName_4, self.txtComponentName_5, self.txtComponentName_6,
                                  self.txtComponentName_7, self.txtComponentName_8, self.txtComponentName_9,
                                  self.txtComponentName_10, self.txtComponentName_11, self.txtComponentName_12,
                                  self.txtComponentName_13, self.txtComponentName_14, self.txtComponentName_15,
                                  self.txtComponentName_16, self.txtComponentName_17, self.txtComponentName_18,
                                  self.txtComponentName_19, self.txtComponentName_20]
        # DISABLE LOAD BUTTON AFTER EDIT AND ENABLE SAVE BUTTON
        for count, name in zip(self.componentCountList, self.componentNameList):
            count.textEdited.connect(self.endLoad)
            name.textChanged.connect(self.endLoad)
        self.txtStudentName.textEdited.connect(self.endLoad)
        self.txtStudentID.textEdited.connect(self.endLoad)
        self.chkGraduate.stateChanged.connect(self.endLoad)
        self.cboCollege.activated.connect(self.endLoad)
        # Save Functionality
        self.btnSave.clicked.connect(self.saveTime)




    def loadData(self):
        """
        *** DO NOT MODIFY THIS METHOD! ***
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        You must modify the method below.
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)

    def loadDataFromFile(self, filePath):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.
        
        *** YOU MUST USE THIS METHOD TO LOAD DATA FILES. ***
        *** This method is required for unit tests! ***
        """
        with open(filePath) as file:
            data = file.read()
        name = re.search(r'<StudentName graduate=".+?">(.+?)</StudentName>', data)
        self.txtStudentName.setText(name[1])

        name = re.search(r'<StudentName graduate="(.+?)">.+?</StudentName>', data)
        if name[1] == "true": self.chkGraduate.setChecked(True)
        else: self.chkGraduate.setChecked(False)

        name = re.search(r'<StudentID>(.+?)</StudentID>', data)
        self.txtStudentID.setText(name[1])

        name = re.search(r'<College>(.+?)</College>', data)
        self.cboCollege.setCurrentText(name[1])

        name = re.findall(r'<Component name="(.+?)" count="(.+?)" />', data)

        for val, box, count in zip(name, self.componentNameList, self.componentCountList):
            box.setText(val[0])
            count.setText(val[1])


        pass

    def clearState(self):
        self.chkGraduate.setCheckState(False)
        self.cboCollege.setCurrentIndex(0)
        self.txtStudentID.clear()
        self.txtStudentName.clear()
        for cot, name in zip(self.componentCountList, self.componentNameList):
            cot.clear()
            name.clear()
        self.btnSave.setDisabled(True)
        self.btnLoad.setDisabled(False)

    def endLoad(self):
        self.btnLoad.setDisabled(True)
        self.btnSave.setDisabled(False)

    def saveTime(self):
        with open("target.xml","w") as file:
            file.write('<?xml version="1.0" encoding="UTF-8"?>\n<Content>\n')
            if self.chkGraduate.checkState() == 2:
                file.write(f'\t<StudentName graduate="true">{self.txtStudentName.displayText()}</StudentName>\n')
            else:
                file.write(f'\t<StudentName graduate="false">{self.txtStudentName.displayText()}</StudentName>\n')

            file.write(f"\t<StudentID>{self.txtStudentID.displayText()}</StudentID>\n")
            file.write(f"\t<College>{self.cboCollege.currentText()}</College>\n")
            file.write(f"\t<Components>\n")
            for comp, count in zip(self.componentNameList, self.componentCountList):
                if comp.displayText() != "":
                    file.write(f'\t\t<Component name="{comp.displayText()}" count="{count.displayText()}" />\n')
            file.write("\t</Components>\n</Content>")






if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()
