# ######################################################
# Author : Mark Dunn
# email : dunn60@purdue.edu
# ID : ee364a12
# Date : 09/13/19
# ######################################################
import os # List of module import statements
import sys # Each one on a line
import glob
from collections import Counter
# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################

def getTechWork(techName: str) -> dict:
    techWork ={}
    reportList = glob.glob("reports/*.dat")

    techID = techNameIDDictionary()[techName]

    for report in reportList:
        repTechId, virusUsed = reportHandler(report)

        if techID == repTechId:
            techWork = Counter(techWork) + Counter(virusUsed)

    return dict(techWork)

def getStrainConsumption(virusName: str) ->dict:

    strainConsum = Counter()
    reportList = glob.glob("reports/*.dat")
    virusID = virusDictionaries()[0][virusName]

    techName = {v: k for k, v in techNameIDDictionary().items()}

    for report in reportList:
        techID, virusUsed = reportHandler(report)
        if virusID in virusUsed.keys():
            strainConsum.update({techName[techID]: virusUsed[virusID]})

    return dict(strainConsum)

def getTechSpending() -> dict:
    reportList = glob.glob("reports/*.dat")
    techSpend = Counter({})
    virusCosts = virusDictionaries()[1]
    techDic = {v: k for k, v in techNameIDDictionary().items()}
    totalCost = 0
    for report in reportList:
        techID, virusesUsed = reportHandler(report)

        for virus in virusesUsed.keys():
            totalCost += virusesUsed[virus] * virusCosts[virus]



        techSpend += Counter({techDic[techID]: totalCost})
        totalCost = 0
    roundTechSpend = {k: round(v, 2) for k, v in techSpend.items()}
    return dict(roundTechSpend)

def getStrainCost() -> dict:
    reportList = glob.glob("reports/*.dat")
    strainCost = Counter({})

    virusName, virusCosts = virusDictionaries()
    virusIDs = {v: k for k, v in virusName.items()}

    for report in reportList:
        virusesUsed = reportHandler(report)[1]
        curVirusCosts = {virusIDs[k]: (v * virusCosts[k]) for k, v in virusesUsed.items()}

        strainCost += Counter(curVirusCosts)
        curVirusCosts.clear()

    roundedCosts = {k: round(v, 2) for k, v in strainCost.items()}

    return dict(roundedCosts)

def getAbsentTechs() -> set:
    techDictionary = {v: k for k, v in techNameIDDictionary().items()}
    allTechs = set(techDictionary.values())
    workingTechs = set()
    reportList = glob.glob("reports/*.dat")

    for report in reportList:
        techID = reportHandler(report)[0]
        workingTechs.add(techDictionary[techID])

    return allTechs.difference(workingTechs)

def getUnusedStrains() -> set:
    virDict = {v: k for k, v in virusDictionaries()[0].items()}
    allViruses = set(virDict.values())
    virusSet = set([])

    reportList = glob.glob("reports/*.dat")

    for report in reportList:
        virusUsed = reportHandler(report)[1]
        virusSet = virusSet.union(set([virDict[value] for value in virusUsed.keys()]))

    return allViruses.difference(virusSet)

###HELPER FUNCTIONS TO CREATE USEFUL DICTIONARIES

#Returns Dictionary in form of {TecName: TechID}
def techNameIDDictionary() -> dict:

    with open("maps/technicians.dat") as file:
        data = file.readlines()[2:]

    # tech = {techName(value): techId(value) for value in data}

    tech = {}
    for value in data:
        techName = value.split("|")[0].strip()
        techID = value.split("|")[1].strip()
        tech[techName] = techID
    return tech

#Returns a list of dictionaries as[{virusNmae/VirusID ; VirusID/VirusName}, {VirusID: VirusCost Per Unit}]
def virusDictionaries() -> list:

    with open("maps/viruses.dat") as file:
        data = file.readlines()
    del data[0]
    del data[0]
    virus = {}
    virus2 ={}
    for value in data:
        virusID = value.split("|")[1].strip()
        virusName = value.split("|")[0].strip()
        virusCost = value.split("|")[2].strip()

        virus[virusName] = virusID
        virus2[virusID] = float(virusCost.strip("$"))
    return [virus, virus2]

#Reutnrs a list as [TechID, {VirusID: UnitsUsed}]
def reportHandler(report: str) -> list:

    with open(report) as file:
        data = file.readlines()
    virus ={}
    userId = data[0].split(":")[1].strip()

    del data[0]
    del data[0]
    del data[0]
    del data[0]

    for value in data:
        virusId = value.split()[1]
        units = int(value.split()[2])
        virus[virusId] = units

    return [userId, virus]


# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################


if __name__ == "__main__":
    # Write anything here to test your code .
    print(getTechWork("Morris, Heather"))
    print(getStrainConsumption("Betapapillomavirus"))
    print(getTechSpending())
    print(getStrainCost())
    print(getAbsentTechs())
    print(getUnusedStrains())