# # Author : Mark Dunn
# email : dunn60@purdue.edu
# ID : ee364a12
# Date : 10/15/19
# import os # List of module import statements
import sys  # Each one on a line


# # No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !

class Rectangle:
    def __init__(self, llPoint, urPoint):
        if(llPoint[0] >= urPoint[0]) or (llPoint[1] >= urPoint[1]):
            raise ValueError("Coordinates provided are incorrect for x or y values upperright coordinates must both be greater.")
        self.lowerLeft = llPoint
        self.upperRight = urPoint
    def isSquare(self):
        if self.upperRight[0]-self.lowerLeft[0] is self.upperRight[1]- self.lowerLeft[1]:
            return True
        else:
            return False
    def intersectsWith(self,rect):

        corner2 = (rect.lowerLeft[0], rect.upperRight[1])
        corner4 = (rect.upperRight[0], rect.lowerLeft[1])
        examine = [rect.lowerLeft, rect.upperRight, corner2, corner4]
        for corner in examine:
            if (self.lowerLeft[0] < corner[0] < self.upperRight[0]) and (self.lowerLeft[1] < corner[1] < self.upperRight[1]):
                return True
        return False
    def __eq__(self, other):
        if type(other) is not Rectangle:
            raise TypeError("Comparison must be between two rectangles.")
        area1 = (self.upperRight[0] - self.lowerLeft[0]) * (self.upperRight[1]- self.lowerLeft[1])
        area2 = (other.upperRight[0] - other.lowerLeft[0]) * (other.upperRight[1]- other.lowerLeft[1])
        if area1 == area2:
            return True
        else:
            return False

class Circle:
    def __init__(self, cen, rad):
        self.center = cen
        if rad <= 0: raise ValueError("Radius must be greater than Zero.")
        self.radius = rad
    def intersectsWith(self, other):
        if type(other) is Circle:
            cenDistance = ((other.center[0] - self.center[0])**2 + (other.center[1] - self.center[1])**2)**(1/2)
            if cenDistance < (other.radius + self.radius):
                return True
            else:
                return False
        else:
            corner2 = (other.lowerLeft[0], other.upperRight[1])
            corner4 = (other.upperRight[0], other.lowerLeft[1])
            examine = [other.lowerLeft, other.upperRight, corner2, corner4]
            for corner in examine:
                cenDistance = ((corner[0] - self.center[0]) ** 2 + (corner[1] - self.center[1]) ** 2) ** (1/2)
                if cenDistance < self.radius:
                    return True
            return False

# This block is optional and can be used for testing .
# We will NOT look into its content .
# 

if __name__ == "__main__":
    rect1 = Rectangle((0, 0), (2, 4))
    rect2 = Rectangle((0, 0), (1, 4))
    print(rect1.isSquare())
    print(rect1.intersectsWith(rect2))
    print(rect1 == rect2)
# Write anything here to test your code .