# ######################################################
# Author : Mark Dunn
# email : dunn60@purdue.edu
# ID: ee364a12
# Date : 08/22/19
# ######################################################

import os # List of module import statements
import sys # Each one on a line
import re

# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################



def find(pattern: str) -> list :
    with open("sequence.txt") as file:
        data = file.read()
    file.close()

    subSequences = [data[i:i+len(pattern)] for i in range(0, len(data)- len(pattern)+ 1)]  # Creates all possible subsequences from data
    foundList =[]
    match = True
    j = 0

    for i in range(len(subSequences)):
        while match is True and j is not len(pattern):
            if pattern[j] is not "X" and pattern[j] is not subSequences[i][j]:
                match = False
            j += 1
        if match is True: foundList.append(subSequences[i])
        match = True
        j = 0
    return foundList


def getStreakProduct(sequence: str, maxSize: int, product: int) -> list:

    foundProducts = []
    total = 1

    for i in range(len(sequence) - 1):
        j = 0
        total = 1

        while total < product and j <= maxSize and i + j < len(sequence):
            total *= int(sequence[i+j])
            if total is product:
                foundProducts.append(sequence[i:i+j+1])
            j += 1

    return foundProducts

def writePyramids(filePath: str, baseSize: int, count :int, char:str) :
    pyramid = ""
    pyrLines = []
    for i in range(baseSize // 2 +1):
        for j in range(baseSize):
            if i +1 > 1 and ((j + 1 < i + 1) or (j  >= (baseSize - i))):
                pyramid += " "
            else:
                pyramid += char
        #if i is  0: pyramid += "\n"
        pyrLines.insert(0,pyramid)
        pyramid =""
    with open(filePath, 'w') as file:
        for i in range(baseSize //2 +1):
            file.write(pyrLines[i])
            for j in range(count- 1):
                file.write(" " + pyrLines[i])
            if i is not range(baseSize //2 +1):file.write("\n")
    file.close()

    return

def getStreaks(sequence: str, letters: str) -> list:
    foundStreaks = []

    seqList = list(sequence)
    findLet = list(letters)
    streak = ""
    for i in range(len(sequence)):
        if seqList[i] in findLet:
            streak += seqList[i]
            if i is not len(sequence) - 1 and seqList[i + 1] is not seqList[i]:
                foundStreaks.append(streak)
                streak = ""
            if i is len(sequence) - 1 and streak is not "": foundStreaks.append(streak)
    return foundStreaks

def getNames(names: list, part: str, name: str) -> str:
    foundNames = []
    return foundNames
def convertToBoolean(num: int, size:int) -> list:
    boolList = []

    if isinstance(size, int) is False or isinstance(num, int) is False: return boolList

    boolList = list(str(bin(num)))
    del boolList[0]
    del boolList[0]

    if len(boolList) <= size:
        for i in range(size - len(boolList)): boolList.insert(0, 0)
    boolList = list(map(int, boolList))
    boolList = list(map(bool, boolList))

    return boolList
def convertToInteger(boolList: list) -> int:

    if isinstance(boolList, list) is False or (len(boolList) is 0): return None

    for value in boolList:
        if type(value) is not bool: return None

    number = ""
    intList = list(map(int,boolList))
    number = number.join(map(str, intList))
    number = "0b" + number

    convertedForm = int(number, 2)

    return convertedForm


# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################
if __name__ == "__main__":
    # Write anything here to test your code .
    z = convertToBoolean(1305, 12)
    y = convertToInteger([False, True, False, True, False, False, False, True, True, False, False, True])
    sequence = "AAASSSSSSAPPPSSPPBBCCCSSS"
    x = getStreaks(sequence, "SAWT")
    writePyramids('pyramid13000.txt',13, 6, 'X')
    print (z)
    print(y)
    print(x)
