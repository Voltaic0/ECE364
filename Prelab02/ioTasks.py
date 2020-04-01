# ######################################################
# Author : Mark Dunn
# email : dunn60@purdue.edu
# ID : ee364a12
# Date : 08/29/19
# ######################################################
import os # List of module import statements
import sys # Each one on a line
import glob
import os.path as Path
# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################

def getMaxDifference(company: str) -> str:

    compFile = company.upper() +".dat"
    if Path.isfile(compFile) is False: return None
    highestDif = ""

    with open(compFile) as file:
        data = file.readlines()
    del data[0]
    del data[0]
    largestDif = 0

    for i in range(len(data)):
        data[i] = (data[i].rstrip()).split(",")
        if((float(data[i][4])-float(data[i][5])) > largestDif):
            largestDif = float(data[i][4])-float(data[i][5])
            highestDif = data[i][0]

    return highestDif

def getGainPercent(symbol: str) -> float:

    compFile = symbol.upper() + ".dat"
    if Path.isfile(compFile) is False: return None

    with open(compFile) as file:
        data = file.readlines()
    del data[0]
    del data[0]

    days = 0
    for i in range(len(data)):
        data[i] = (data[i].rstrip()).split(",")
        if float(data[i][1]) > float(data[i][3]): days +=1

    percentHigher = round((days / len(data) * 100), 4)

    return percentHigher

def getVolumeSum(symbol: str, date1:str, date2:str) -> int:
    compFile = symbol.upper() + ".dat"
    if Path.isfile(compFile) is False: return None

    with open(compFile) as file:
        data = file.readlines()
    del data[0]
    del data[0]

    first = date1.split("/")
    second = date2.split("/")

    if int(first[0]) > int(second[0]):
        return None
    if int(first[0]) == int(second[0]):
        if int(first[1]) == int(second[1]):
            if int(first[2]) >= int(second[2]): return None
        if int(first[1]) > int(second[1]): return None

    adding = False
    tranVol = 0.0

    for i in range(len(data)):
        data[i] = (data[i].rstrip()).split(",")
        curVol = float(data[i][2])

        data[i] = data[i][0].split("/")
        if adding is True: tranVol += curVol

        if(int(data[i][0]) == int(first[0]) and int(data[i][1]) == int(first[1]) and int(data[i][2]) == int(first[2])):
            adding = False

        if ((int(data[i][0]) == int(second[0])) and (int(data[i][1]) == int(second[1])) and (int(data[i][2]) == int(second[2]))):
            adding = True
            tranVol = curVol

    return int(tranVol)

def getBestGain(date: str) -> float:

    fileList = glob.glob("*.dat")
    date = date.split("/") #[Year, Month, Day]
    highPer = -100

    for j in range(len(fileList)):
        with open(fileList[j]) as file:
            data = file.readlines()
        del data[0]
        del data[0]

        for i in range(len(data)):
            data[i] = (data[i].rstrip()).split(",")
            op = float(data[i][3])
            cl = float(data[i][1])

            data[i] = data[i][0].split("/")

            if (int(data[i][0]) == int(date[0]) and int(data[i][1]) == int(date[1]) and int(data[i][2]) == int(date[2])):
                if((cl - op)/op) > highPer:
                    highPer = (((cl -op)/op) *100)

    return round(highPer, 4)

def getAveragePrice(symbol: str, year: int) -> float:

    compFile = symbol.upper() + ".dat"

    if Path.isfile(compFile) is False: return None

    with open(compFile) as file:
        data = file.readlines()
    del data[0]
    del data[0]

    days = 0
    total = 0

    for i in range(len(data)):
        data[i] = (data[i].rstrip()).split(",")
        op = float(data[i][3])
        cl = float(data[i][1])

        data[i] = data[i][0].split("/")
        if(int(data[i][0]) == year):
            days += 1
            total += (cl +op) /2

    avgPrice = total / days
    return round(avgPrice, 4)

def getCountOver(symbol: str, price: float) -> int:

    compFile = symbol.upper() + ".dat"
    if Path.isfile(compFile) is False: return None

    with open(compFile) as file:
        data = file.readlines()
    del data[0]
    del data[0]

    days = 0

    for i in range(len(data)):
        data[i] = (data[i].rstrip()).split(",")
        if(float(data[i][1]) >= price and float(data[i][3]) >= price and float(data[i][4]) >= price and float(data[i][5]) >= price): days +=1

    return days
# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################
if __name__ == "__main__":
# Write anything here to test your code .
    z = getCountOver("aapl", 0)
    y = getAveragePrice("amzn", 2016)
    x = getBestGain("2019/01/11")
    w = getVolumeSum("fb", "2017/01/10", "2018/01/10")
    v = getMaxDifference("msft")
    u = getGainPercent("tsla")
    print(z)
    print(y)
    print(x)
    print(w)
    print(v)
    print(u)
