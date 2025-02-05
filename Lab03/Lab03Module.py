# ######################################################
# Author : Mark Dunn
# email : dunn60@purdue.edu
# ID: ee364a12
# Date : 09/10/19
# ######################################################

import os # List of module import statements
import sys # Each one on a line

# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################
def getMonthlyVolume() -> dict:
    monthVol ={}
    with open("stocks.dat") as file:
        data = file.readlines()

    del data[0]
    del data[0]

    for index, value in enumerate(data):
        data[index] = (value.strip()).split(",")
        curDat = data[index][0].split("/")
        if(curDat[0]+"/"+curDat[1]) not in monthVol.keys():
            monthVol[curDat[0]+"/"+curDat[1]] = int(float(data[index][2]))
        else:
            monthVol[curDat[0]+"/"+curDat[1]] += int(float(data[index][2]))

    return monthVol

def getCommonDays(year1: str, year2:str) -> set:

    with open("stocks.dat") as file:
        data = file.readlines()
    del data[0]
    del data[0]
    firstYearSet = set([])
    secondYearSet = set([])

    for index, value in enumerate(data):
        data[index] = value.strip().split(",")

        curDate = data[index][0].split("/")

        if year1 == curDate[0]: firstYearSet.add((curDate[1], curDate[2]))
        if year2 == curDate[0]: secondYearSet.add((curDate[1], curDate[2]))

    comDays = firstYearSet.intersection(secondYearSet)
    return comDays

def getNamesBySymbol(n: int) -> dict:
    nTrades = {}
    personDict = {}
    with open("transactions.dat") as file:
        data = file.readlines()

    for index, value in enumerate(data):
        data[index] = data[index].strip().split(":")
        personDict[data[index][0]] = data[index][1].strip(" ").split(", ")


    return nTrades

# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################
if __name__ == "__main__":
    print(getMonthlyVolume())
    #Write anything here to test your code .
