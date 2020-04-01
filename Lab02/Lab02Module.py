# ######################################################
# Author : Mark Dunn
# email : dunn60@purdue.edu
# ID : ee364a12
# Date : 9/03/19
# ######################################################
import os # List of module import statements
import sys # Each one on a line
import glob
# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################

def getLeastFrequent() -> int:
    count = []

    with open("numbers.dat") as file:
        data = file.readlines()

    for i in range(100):
        count.append(0)
        data[i] = (data[i].rstrip()).split(" ")

    for i in range(100):
        for j in range(100):
            count[int(data[i][j])] += 1

    lowestApp = 10000

    for i in range(100):
        if count[i] < lowestApp:
            least = i
            lowestApp = count[i]

    return least

def getCodeFor(coordinate: float) -> list:
    zipCodes = []

    with open("coordinates.dat") as file:
        data = file.readlines()

    del data[0]
    del data[0]

    for i in range(len(data)):
        data[i] = data[i].split()

    for i in range(len(data)):
        if(float(data[i][0]) == coordinate or float(data[i][1]) == coordinate): zipCodes.append(data[i][2])

    zipCodes.sort()

    return zipCodes

def getSubMatrixSum( startRowIndex: int, endRowIndex: int, startColumnIndex: int, endColumnIndex: int) -> int:

    with open("numbers.dat") as file:
        data = file.readlines()

    for i in range(100):
        data[i] = (data[i].rstrip()).split(" ")

    total = 0
    for i in range(endRowIndex - startRowIndex + 1):
        for j in range(endColumnIndex - startColumnIndex + 1):
            total += int(data[i+startRowIndex][j+startColumnIndex])



    return total
# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################
if __name__ == "__main__" :
# Write anything here to test your code .
    z = getSubMatrixSum(98,99,98,99)
    print( z )