# # Author : Mark Dunn
# email : dunn60@purdue.edu
# ID : ee364a12
# Date : 11/14/19
import os # List of module import statements
import sys  # Each one on a line
import numpy as np
import scipy.ndimage as ndimage
import imageio
import scipy.interpolate as interpolate
from scipy.spatial import Delaunay
import matplotlib.path as mplPath
import time

# # No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !

class Triangle:

    def __init__(self, verts):
        try:
            if type(verts) is not np.ndarray: raise ValueError("Values input must be Numpy Array!")
            if verts.dtype != np.float64: raise ValueError("Vertices must have type np.float64!")
            if verts.shape != (3, 2): raise ValueError("Vertices must have shape 3x2!")
        except AttributeError:
            raise TypeError("Input must be of type np.ndarray!")

        self.vertices = verts
        self.leftMat = np.array([])
        self.rightMat = np.array([])

    def __repr__(self):
        return str(self.vertices)

    def getPoints(self):

        x1, y1 = self.vertices[0]
        x2, y2 = self.vertices[1]
        x3, y3 = self.vertices[2]

        lowX = np.int(min([x1, x2, x3]))
        if lowX > min([x1, x2, x3]): lowX -= 1
        lowY = np.int(min([y1, y2, y3]))
        if lowY > min([y1, y2, y3]): lowY -= 1

        maxX = np.int(max([x1, x2, x3]))
        if maxX < max([x1, x2, x3]): maxX += 1
        maxY = np.int(max([y1, y2, y3]))
        if maxY < max([y1, y2, y3]): maxY += 1

        x, y = np.meshgrid(np.arange(lowX, maxX), np.arange(lowY, maxY))  # make a canvas with coordinates
        x, y = x.flatten(), y.flatten()
        points = np.vstack((x, y)).T
        bbpath = mplPath.Path(self.vertices)
        grid = bbpath.contains_points(points, radius=0.1)
        ones = np.nonzero(grid)
        newtest = points[ones]
        return newtest

class Morpher:

    def __init__(self, lImage, lTri, rImage, rTri):

        try:
            if lImage.dtype != np.uint8: raise TypeError("Image loaded must have data points of type uint8.")
            if rImage.dtype != np.uint8: raise TypeError("Image loaded must have data points of type uint8.")
        except AttributeError:
            raise TypeError("Image input must be a numpy array!")

        self.leftImage = lImage
        self.rightImage = rImage
        if type(lTri) is not list or not all(isinstance(x, Triangle) for x in lTri): raise TypeError("Second Parameter"
                                                                                                     " must be list of"
                                                                                                     " Triangle Types.")
        self.leftTriangles = lTri
        if type(rTri) is not list or not all(isinstance(x, Triangle) for x in rTri): raise TypeError("Fourth Parameter"
                                                                                                     " must be list of"
                                                                                                     " Triangle Types.")
        self.rightTriangles = rTri

    def getImageAtAlpha(self, alpha):
        target = []

        if alpha == 0:
            return self.leftImage.copy()
        elif alpha == 1:
            return self.rightImage.copy()

        for l, r in zip(self.leftTriangles, self.rightTriangles):
            newTri = (1-alpha)*l.vertices + alpha*r.vertices
            target.append(Triangle(newTri))

        for l, r, t in zip(self.leftTriangles, self.rightTriangles, target):
            t.leftMat = self.hInverse(l, t)
            t.rightMat = self.hInverse(r, t)
        # Blending Process Begins
        blendedImage = np.zeros(self.leftImage.shape).astype("uint8")
        originalShape = blendedImage.shape
        blendedImage = blendedImage.flatten()

        bigTest = interpolate.RectBivariateSpline(np.arange(self.rightImage.shape[0]),
                                                  np.arange(self.rightImage.shape[1]), self.rightImage)
        bigTest2 = interpolate.RectBivariateSpline(np.arange(self.leftImage.shape[0]),
                                                  np.arange(self.leftImage.shape[1]), self.leftImage)

        for tri in target:
            pointArray = tri.getPoints()

            onesArr = [1] * len(pointArray[:, 0])
            flatIndex = pointArray[:, 0] + pointArray[:, 1] * originalShape[1]

            oldSpots1 = np.dot(tri.leftMat, np.array([pointArray[:, 0], pointArray[:, 1], onesArr]))
            oldSpots2 = np.dot(tri.rightMat, np.array([pointArray[:, 0], pointArray[:, 1], onesArr]))

            newLeftY = oldSpots1[1, :]
            newLeftX = oldSpots1[0, :]
            newRightY = oldSpots2[1, :]
            newRightX = oldSpots2[0, :]

            color1 = bigTest2.ev(newLeftY, newLeftX)
            color2 = bigTest.ev(newRightY, newRightX)

            newColor = np.uint8((1 - alpha) * color1 + alpha * color2)

            blendedImage[flatIndex] = newColor
        blendedImage = blendedImage.reshape(originalShape)
        return blendedImage

    def saveVideo(self, targetFilePath, frameCount, frameRate, includeReversed):

        alphas = np.linspace(0, 1, frameCount)
        os.makedirs("tmp")
        for index, ap in enumerate(alphas):
            temp = self.getImageAtAlpha(ap)

            imageio.imwrite(f"tmp/Image{(index+1):02d}.png", temp)
            if includeReversed is True:
                number = frameCount *2 - index
                imageio.imwrite(f"tmp/Image{number:02d}.png", temp)
            print(f"DONE{index}")

        os.system(f"ffmpeg -f image2 -r {frameRate} -i tmp/Image%02d.png -vcodec mpeg4 -y {targetFilePath}")
        filelist = [f for f in os.listdir("tmp")]
        for f in filelist:
            os.remove(os.path.join("tmp", f))

        os.rmdir("tmp")


    def hInverse(self, tri1, tri2):

        row1 = list(tri1.vertices[0]) + [1, 0, 0, 0]
        row2 = [0, 0, 0] + list(tri1.vertices[0]) + [1]
        row3 = list(tri1.vertices[1]) + [1, 0, 0, 0]
        row4 = [0, 0, 0] + list(tri1.vertices[1]) + [1]
        row5 = list(tri1.vertices[2]) + [1, 0, 0, 0]
        row6 = [0, 0, 0] + list(tri1.vertices[2]) + [1]

        aMat = np.array([row1, row2, row3, row4, row5, row6])

        bMat = np.array([[tri2.vertices[0][0]], [tri2.vertices[0][1]], [tri2.vertices[1][0]], [tri2.vertices[1][1]],
                        [tri2.vertices[2][0]], [tri2.vertices[2][1]]])

        hMat = np.linalg.solve(aMat, bMat)

        bigHMat = np.array([[hMat[0][0], hMat[1][0], hMat[2][0]], [hMat[3][0], hMat[4][0], hMat[5][0]], [0, 0, 1]])

        return np.linalg.inv(bigHMat)

class ColorMorpher(Morpher):

    def __init__(self, limage, liangle, rimage, riangle):
        super().__init__(limage, liangle, rimage, riangle)

    def getImageAtAlpha(self, alpha):
        target = []

        if alpha == 0:
            return self.leftImage.copy()
        elif alpha == 1:
            return self.rightImage.copy()

        for l, r in zip(self.leftTriangles, self.rightTriangles):
            newTri = (1-alpha)*l.vertices + alpha*r.vertices
            target.append(Triangle(newTri))

        for l, r, t in zip(self.leftTriangles, self.rightTriangles, target):
            t.leftMat = self.hInverse(l, t)
            t.rightMat = self.hInverse(r, t)
        # Blending Process Begins
        blendedImage = self.leftImage.copy()
        originalShape = blendedImage.shape
        blendedImage = blendedImage.transpose(2, 0, 1).reshape(3, -1)

        bigTest = interpolate.RectBivariateSpline(np.arange(self.rightImage.shape[0]),
                                                  np.arange(self.rightImage.shape[1]), self.rightImage)
        bigTest2 = interpolate.RectBivariateSpline(np.arange(self.leftImage.shape[0]),
                                                  np.arange(self.leftImage.shape[1]), self.leftImage)

        for tri in target:
            pointArray = tri.getPoints()

            onesArr = [1] * len(pointArray[:, 0])
            flatIndex = pointArray[:, 0] + pointArray[:, 1] * originalShape[1]

            oldSpots1 = np.dot(tri.leftMat, np.array([pointArray[:, 0], pointArray[:, 1], onesArr]))
            oldSpots2 = np.dot(tri.rightMat, np.array([pointArray[:, 0], pointArray[:, 1], onesArr]))

            newLeftY = oldSpots1[1, :]
            newLeftX = oldSpots1[0, :]
            newRightY = oldSpots2[1, :]
            newRightX = oldSpots2[0, :]

            color1 = bigTest2.ev(newLeftY, newLeftX)
            color2 = bigTest.ev(newRightY, newRightX)

            newColor = np.uint8((1 - alpha) * color1 + alpha * color2)

            blendedImage[flatIndex] = newColor
        blendedImage = blendedImage.reshape(originalShape)
        return blendedImage

def loadTriangles(leftPath:str, rightPath:str):

    with open(leftPath) as file:
        leftPoints = file.readlines()
    with open(rightPath) as file:
        rightPoints = file.readlines()

    leftPoints = [left.split() for left in leftPoints]
    rightPoints = [right.split() for right in rightPoints]
    tri = Delaunay(leftPoints)

    lt = [Triangle(np.array([np.float64(leftPoints[p1]), np.float64(leftPoints[p2]), np.float64(leftPoints[p3])])) for p1, p2, p3 in tri.simplices]
    rt = [Triangle(np.array([np.float64(rightPoints[p1]), np.float64(rightPoints[p2]), np.float64(rightPoints[p3])])) for p1, p2, p3 in tri.simplices]

    return lt, rt


# This block is optional and can be used for testing .
# We will NOT look into its content .
# 

if __name__ == "__main__":
    lefty, righty = loadTriangles("/home/ecegridfs/a/ee364a12/Lab12/LeftGray.png.txt", "points.right.txt")

    newt = lefty[0].getPoints()
    # print()
    image1 = imageio.imread("LeftGray.png")
    image2 = imageio.imread("RightGray.png")
    test = Morpher(image1, lefty, image2, righty)
    t0 = time.time()
    new = test.getImageAtAlpha(.5)
    t1 = time.time()
    print(f"Triangle done: {t1 - t0}!")
    imageio.imwrite("FirstBlend.png", new)

    # test.saveVideo("Video.mp4", 40, 30, True)

    # image1 = imageio.imread("LeftColor.png")
    # image2 = imageio.imread("RightColor.png")
    # color = ColorMorpher(image1, lefty, image2, righty)
    #
    # t0 = time.time()
    # new = color.getImageAtAlpha(0.5)
    # t1 = time.time()
    # print(f"Triangle done: {t1 - t0}!")
    # imageio.imwrite("ColorBlend.png", new)
# Write anything here to test your code .