# # Author : Mark Dunn
# email : dunn60@purdue.edu
# ID : ee364a12
# Date : 09/26/19
# import os # List of module import statements
import sys  # Each one on a line

# Import PyQt5 classes
import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
import PyQt5.Qt as Qt


from MorphingGui import *
from Morphing import *


class MorphingApp(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MorphingApp, self).__init__(parent)
        self.setupUi(self)


        self.imagesLoaded = [False, False]
        self.tempPoints = [None, None]
        self.activePoints = [None, None]
        self.leftImg = 0
        self.rightImg = 0
        self.rightTri = ""
        self.leftTri = ""

        self.chkTriangles.setDisabled(True)
        self.sliderAlpha.setDisabled(True)
        self.txtAlpha.setDisabled(True)
        self.btnBlend.setDisabled(True)
        self.btnStartImage.clicked.connect(self.loadStartImage)
        self.btnEndImage.clicked.connect(self.loadEndImage)

        self.sliderAlpha.sliderMoved.connect(self.alphaConnection)
        self.sliderAlpha.valueChanged.connect(self.alphaConnection)
        self.btnBlend.clicked.connect(self.blendImage)
        self.grphStart.mousePressEvent = self.pressEventMagicL
        self.grphEnd.mousePressEvent = self.pressEventMagicR
        self.keyPressEvent = self.checkKey
        self.mousePressEvent = self.commitPoints
        self.chkTriangles.stateChanged.connect(self.checkTriangles)
        self.rightLines = []
        self.leftLines = []

        self.mostRecentPoint = None
        self.ellipsi = [None, None]

    def checkTriangles(self):
        if self.chkTriangles.checkState() == 2:
            if os.path.isfile(self.rightTri):
                with open(self.leftTri) as file:
                    leftPoints = file.readlines()
                with open(self.rightTri) as file:
                    rightPoints = file.readlines()

                leftPoints = [left.split() for left in leftPoints]
                rightPoints = [right.split() for right in rightPoints]
                tri = Delaunay(leftPoints)

                lt = [(float(leftPoints[p1][0]), float(leftPoints[p1][1]), float(leftPoints[p2][0]),
                       float(leftPoints[p2][1]), float(leftPoints[p3][0]), float(leftPoints[p3][1])) for p1, p2, p3 in tri.simplices]

                rt = [(float(rightPoints[p1][0]), float(rightPoints[p1][1]), float(rightPoints[p2][0]),
                       float(rightPoints[p2][1]), float(rightPoints[p3][0]), float(rightPoints[p3][1])) for p1, p2, p3 in tri.simplices]

                pen = Qt.QPen(Qt.QColor(0, 255, 200, 255))
                pen.setWidth(2)

                for l, r in zip(lt, rt):
                    self.leftLines.append(self.grphStart.scene().addLine(l[0], l[1], l[2], l[3], pen))
                    self.leftLines.append(self.grphStart.scene().addLine(l[0], l[1], l[4], l[5], pen))
                    self.leftLines.append(self.grphStart.scene().addLine(l[4], l[5], l[2], l[3], pen))

                    self.rightLines.append(self.grphEnd.scene().addLine(r[0], r[1], r[2], r[3], pen))
                    self.rightLines.append(self.grphEnd.scene().addLine(r[0], r[1], r[4], r[5], pen))
                    self.rightLines.append(self.grphEnd.scene().addLine(r[4], r[5], r[2], r[3], pen))

        else:
            for line in self.leftLines:
                self.grphStart.scene().removeItem(line)
            self.leftLines = []
            for line in self.rightLines:
                self.grphEnd.scene().removeItem(line)
            self.rightLines = []


    def commitPoints(self, ev):
        if self.activePoints[0] and self.activePoints[1]:
            self.grphStart.scene().removeItem(self.ellipsi[0])
            self.pointAdd(self.grphStart.scene(), self.tempPoints[0][0], self.tempPoints[0][1], 2)
            self.grphEnd.scene().removeItem(self.ellipsi[1])
            self.pointAdd(self.grphEnd.scene(), self.tempPoints[1][0], self.tempPoints[1][1], 2)
            self.activePoints = [False, False]

            if os.path.isfile(self.leftTri):
                with open(self.leftTri, "a") as file:
                    file.write(f"\n{round(self.tempPoints[0][0], 1)}   {round(self.tempPoints[0][1], 1)}")
            else:
                with open(self.leftTri, "a") as file:
                    file.write(f"{round(self.tempPoints[0][0], 1)}   {round(self.tempPoints[0][1], 1)}")
            if os.path.isfile(self.rightTri):
                with open(self.rightTri, "a") as file:
                    file.write(f"\n{round(self.tempPoints[1][0], 1)}   {round(self.tempPoints[1][1], 1)}")
            else:
                with open(self.rightTri, "a") as file:
                    file.write(f"{round(self.tempPoints[1][0], 1)}   {round(self.tempPoints[1][1], 1)}")

            for line in self.leftLines:
                self.grphStart.scene().removeItem(line)
            self.leftLines = []
            for line in self.rightLines:
                self.grphEnd.scene().removeItem(line)
            self.rightLines = []
            self.checkTriangles()

    def checkKey(self, ev:Qt.QKeyEvent):
        if ev.key() == QtCore.Qt.Key_Backspace:
            if self.activePoints[0] and self.activePoints[1]:
                self.activePoints[1] = False
                self.grphEnd.scene().removeItem(self.ellipsi[1])
                self.grphEnd.show()
            elif self.activePoints[0] and self.activePoints[1] is False:
                self.activePoints[0] = False
                self.grphStart.scene().removeItem(self.ellipsi[0])
                self.grphStart.show()


    def pressEventMagicL(self, ev):
        if self.activePoints[0] and self.activePoints[1]:
            self.commitPoints("Lol bad Argument")
        if self.activePoints[0] is False:
            position = ev.pos()
            x = float(position.x()) * 4
            y = float(position.y()) * 4
            self.tempPoints[0] = (x, y)
            self.activePoints[0] = True
            self.ellipsi[0] = self.pointAdd(self.grphStart.scene(), x-23, y-23, 1)
            self.grphStart.show()

    def pressEventMagicR(self, ev):
        if self.activePoints[1] is False and self.activePoints[0]:
            position = ev.pos()
            x = float(position.x()) * 4
            y = float(position.y()) * 4
            self.tempPoints[1] = (x, y)
            self.activePoints[1] = True
            self.ellipsi[1] = self.pointAdd(self.grphEnd.scene(), x-23, y-23, 1)
            self.grphEnd.show()




    def blendImage(self):
        lt, rt = loadTriangles(self.leftTri, self.rightTri)
        morphingTime = Morpher(self.leftImg, lt, self.rightImg, rt)
        imgArray = morphingTime.getImageAtAlpha(float(self.txtAlpha.displayText()))
        imageio.imwrite("aq1234q.png", imgArray)
        newPath = os.getcwd() + "/aq1234q.png"
        tester = QtGui.QPixmap(newPath)
        testing = Qt.QGraphicsScene()
        tester = tester.scaled(self.grphBlended.size())
        testing.addPixmap(tester)
        self.grphBlended.setScene(testing)
        self.grphBlended.show()
        os.remove("aq1234q.png")

    def alphaConnection(self, val):
        value = val / 20
        self.txtAlpha.setText(f"{value}")

    def loadData(self):
        """
        *** DO NOT MODIFY THIS METHOD! ***
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        You must modify the method below.
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open png or jpg file ...', filter="Image Files (*.png *.jpg)")

        if not filePath:
            return
        return filePath

    def imageHandling(self, pos):
        filePath = self.loadData()
        if filePath is None: return
        pointPath = filePath + ".txt"

        image = imageio.imread(filePath)
        shaped = image.shape

        tester = QtGui.QPixmap(filePath)

        if pos == 0:
            leftScene = Qt.QGraphicsScene()
            leftScene.addPixmap(tester)
            self.leftImg = image
            self.imagesLoaded[0] = True
            if self.imagesLoaded[0] and self.imagesLoaded[1]: self.enableButtons()
            self.leftTri = pointPath
            if os.path.isfile(pointPath):
                with open(pointPath) as file:
                    data = file.readlines()
                for point in data:
                    xc, yc = point.split()
                    self.pointAdd(leftScene, int(float(xc))-11.5, int(float(yc))-11.5, 0)
            leftScene.setSceneRect(0, 0, shaped[1], shaped[0])
            self.grphStart.setScene(leftScene)
            self.grphStart.fitInView(leftScene.sceneRect(), QtCore.Qt.KeepAspectRatio)
            self.grphStart.show()
        else:
            rightScene = Qt.QGraphicsScene()
            rightScene.addPixmap(tester)
            self.grphEnd.setScene(rightScene)
            self.grphEnd.show()
            self.rightImg = image
            self.imagesLoaded[1] = True
            if self.imagesLoaded[0] and self.imagesLoaded[1]: self.enableButtons()
            self.rightTri = pointPath
            if os.path.isfile(pointPath):
                with open(pointPath) as file:
                    data = file.readlines()
                for point in data:
                    xc, yc = point.split()
                    self.pointAdd(rightScene, int(float(xc))-11.5, int(float(yc))-11.5, 0)
            rightScene.setSceneRect(0, 0, shaped[1], shaped[0])
            self.grphEnd.setScene(rightScene)
            self.grphEnd.fitInView(rightScene.sceneRect(), QtCore.Qt.KeepAspectRatio)
            self.grphEnd.show()

    def loadStartImage(self):
        self.imageHandling(0)

    def loadEndImage(self):
        self.imageHandling(1)

    def pointAdd(self, scene: Qt.QGraphicsScene, xc: int, yc: int, col: int) -> Qt.QGraphicsScene:
        colour = Qt.QBrush()
        colour.setStyle(QtCore.Qt.SolidPattern)
        if col == 0:
            colour.setColor(Qt.QColor(255, 0, 0, 255))
        elif col == 1:
            colour.setColor(Qt.QColor(0, 255, 0, 255))
        else:
            colour.setColor(Qt.QColor(0, 0, 255, 255))

        return scene.addEllipse(xc, yc, 23, 23, Qt.QPen(), colour)

    def enableButtons(self):
        self.sliderAlpha.setEnabled(True)
        self.chkTriangles.setEnabled(True)
        self.txtAlpha.setEnabled(True)
        self.btnBlend.setEnabled(True)
        self.activePoints = [False, False]
        return


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = MorphingApp()

    currentForm.show()
    sys.exit(currentApp.exec_())

