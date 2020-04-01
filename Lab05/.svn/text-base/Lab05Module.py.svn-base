# ######################################################
# Author : Mark Dunn
# email : dunn60@purdue.edu
# ID : ee364a12
# Date : 09/17/19
# ######################################################
import os # List of module import statements
import sys # Each one on a line
import glob
from collections import Counter
# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################

def getDriversFor(car: str) -> set:

    carDrivers = driversDict()

    return set(carDrivers[car])
def getCommonDriversFor(*args) -> set:
    peopleEligible = set([])
    carConv = carNametoID()
    peoplConv = driversDict()
    for index, value in enumerate(args):
        carID = carConv[value]
        peopleWhoCan = set(peoplConv[carID])
        if index is 0: peopleEligible = peopleWhoCan
        else: peopleEligible = peopleEligible.intersection(peopleWhoCan)

    return peopleEligible

def getCarsFor(names: set) -> dict:

    drivers = driversDict()
    cars = {v: k for k, v in carNametoID().items()}
    endResult = {}


    for name in names:
        endResult[name] = set([])
        for car in drivers.keys():
            carName = cars[car]
            if name in drivers[car]: endResult[name].add(carName)
    return endResult

def getBounds()-> dict:

    signalDict, _ = signalsReader()
    finalBounds ={}

    for signal in signalDict.keys():
        signalValues = signalDict[signal]
        maximum = round(max(signalValues), 3)
        minimum = round(min(signalValues), 3)
        average = round(sum(signalValues) / len(signalValues), 3)
        finalBounds[signal] = (minimum, average, maximum)
    return finalBounds

def getSampled(name: str) -> list:

    signalDict, times = signalsReader()
    signalValues = signalDict[name]

    integerTimeList =[]

    for index, value in enumerate(times):
        if(value %1) == 0: integerTimeList.append(signalValues[index])
    return integerTimeList

def getDuration(start: float, end: float) -> dict:

    signalDict, times = signalsReader()
    durationDict = {}

    for signal in signalDict.keys():
        durationDict[signal] = []
        signalValues = signalDict[signal]

        for index, value in enumerate(times):
            if start <= value <= end:
                curVal = signalValues[index]
                durationDict[signal].append(curVal)
    return durationDict

def getValueAt(name: str, timeStamp: float) -> float:

    signalDict, times = signalsReader()

    signalvalues = signalDict[name]

    exactTime = timeStamp in times

    for index, value in enumerate(times):

        if exactTime:
            if timeStamp == value:
                return signalvalues[index]
        else:
            if value <= timeStamp <= times[index+1]:
                if(timeStamp - value) < (times[index+1] - timeStamp):
                    return signalvalues[index]
                else:
                    return signalvalues[index+1]
    return None




##HELPER
def signalsReader() -> dict:
    with open("labfiles/signals.dat") as file:
        data = file.readlines()
    signalNames = data[0].split()
    del signalNames[0]
    del data[0]; del data[0]
    compSignals = {}
    for name in signalNames: compSignals[name] = []
    times =[]

    for value in data:
        signalValues = value.split()
        times.append(float(signalValues[0]))
        del signalValues[0]
        for index, element in enumerate(signalValues):
            compSignals[signalNames[index]].append(float(element))

    return (compSignals, times)

def driversDict()-> dict:

    drivers = {}
    with open("labfiles/drivers.dat") as file:
        data = file.readlines()
    del data[0]
    del data[1]
    carIds = data[0].split()
    for car in carIds: drivers[car] = []
    del data[0]
    for value in data:
        personList = value.split("|")
        person = personList[0].strip()
        del personList[0]
        for index, car in enumerate(personList):
            if car.strip() == "X": drivers[carIds[index]].append(person)

    return drivers

def carNametoID() -> dict:
    with open("labfiles/cars.dat") as file:
        data = file.readlines()

    del data[0]; del data[0]
    returnDict = {}
    for value in data:
        carID = value.split("|")[0].strip()
        carName = value.split("|")[1].strip()
        returnDict[carName] = carID
    return returnDict

# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################


if __name__ == "__main__":
    # Write anything here to test your code .
    print(getDriversFor("C-583"))
    print(len(getDriversFor("C-583")))
    print(getCommonDriversFor("Chevrolet 1500", "Pontiac Montana", "Isuzu Rodeo", "Geo Tracker"))
    print(len(getCommonDriversFor("Mercedes Sprinter", "Honda Accord", "Ford Focus")))
    names = {"Sang, Chanell", "Chock, Velvet"}
    print(getCarsFor(names))
    print(getBounds()["NIK876"])
    print(getSampled("ISO610"))
    print(len(getSampled("ISO610")))
    signalMap = getDuration(1.0, 2.0)
    print(signalMap["AFW481"])
    print(getValueAt("TNP064", 1.1))
    print(getValueAt("XDF846", 15.817))