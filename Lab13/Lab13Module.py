# # Author : Mark Dunn
# email : dunn60@purdue.edu
# ID : ee364a12
# Date : 11/19/19
# import os # List of module import statements
import sys  # Each one on a line
import re
from measurement import calculateDistance
from functools import total_ordering
def calculateCost(sourceZip: str, destinationZip: str) -> float:

    with open("coordinates.dat") as file:
        data = file.readlines()
    for line in data:
        split = line.split(",")
        if split[0] == ('"' + sourceZip + '"'):
            lat1 = split[2].strip(' "')
            long1 = split[3].strip(' "')
        if split[0] == ('"' + destinationZip + '"'):
            lat2 = split[2].strip(' "')
            long2 = split[3].strip(' "')

    distance = calculateDistance((float(lat1), float(long1)), (float(lat2), float(long2)))
    cost = round(.01 * distance, 2)
    return cost
@total_ordering
class Package:
    def __init__(self, companyName, sourceAddress, destinationAddress):

        self.company = companyName
        self.source = sourceAddress
        self.destination = destinationAddress

        sourcezip = re.search(r' ([0-9]{5})', self.source)
        destzip = re.search(r' ([0-9]{5})', self.destination)
        self.cost = calculateCost(sourcezip[1], destzip[1])

    def __str__(self):
        sourcezip = re.search(r' ([0-9]{5})', self.source)
        destzip = re.search(r' ([0-9]{5})', self.destination)

        return f"{sourcezip[1]} => {destzip[1]}, Cost = ${self.cost}"

    def __repr__(self):
        sourcezip = re.search(r' ([0-9]{5})', self.source)
        destzip = re.search(r' ([0-9]{5})', self.destination)

        return f"{sourcezip[1]} => {destzip[1]}, Cost = ${self.cost}"

    def __add__(self, other):

        if type(other) is not Package: raise TypeError("Addition must be performed between two Package classes.")
        if other.company != self.company: raise ValueError("Both packages must be from the same Company.")

        return PackageGroup(self.company, [self, other])

    def __lt__(self, other):
        if type(other) is not Package: raise TypeError("Comparison must be performed between two Package classes.")
        return self.cost < other.cost
    def __eq__(self, other):
        if type(other) is not Package: raise TypeError("Comparison must be performed between two Package classes.")
        return  self.cost == other.cost

@total_ordering
class PackageGroup:

    def __init__(self, name, packageList):

        self.company = name
        packageList.sort()
        packageList.reverse()
        self.packages = packageList
        self.cost = 0
        for pack in packageList:
            self.cost += pack.cost
        self.cost = round(self.cost, 2)

    def __str__(self):
        return f"{self.company}, {len(self.packages):03d} Shipments, Cost = ${self.cost}"

    def getByZip(self, thing:set):
        if len(thing) == 0: raise ValueError("Set to test against is empty!")
        applies =[]
        for pack in self.packages:
            sourcezip = re.search(r' ([0-9]{5})', pack.source)[1]
            destzip = re.search(r' ([0-9]{5})', pack.destination)[1]

            if sourcezip in thing or destzip in thing:
                applies.append(pack)
        return applies

    def getByState(self, states:set):
        if len(states) == 0: raise ValueError("Set of States cannot be empty!")

        applies = []
        for pack in self.packages:
            sourcestat = re.search(r' ([A-Z]{2}) [0-9]{5}', pack.source)[1]
            deststat = re.search(r' ([A-Z]{2}) [0-9]{5}', pack.destination)[1]

            if sourcestat in states or deststat in states:
                applies.append(pack)
        return applies

    def getByCity(self, cities:set):
        if len(cities) == 0: raise ValueError("Set of States cannot be empty!")

        applies = []
        for pack in self.packages:
            sourceCit = re.search(r', ([a-zA-Z ]+?), [A-Z]{2} [0-9]{5}', pack.source)[1]
            destCit = re.search(r', ([a-zA-Z ]+?), [A-Z]{2} [0-9]{5}', pack.destination)[1]

            if sourceCit in cities or destCit in cities:
                applies.append(pack)
        return applies

    def __contains__(self, item):
        if type(item) is not Package: raise TypeError("Item to be checked within PackageGroup must be type Package!")

        for pack in self.packages:
            if pack.destination == item.destination and pack.source == item.source and pack.company == item.company:
                return True

        return False

    def __add__(self, other):
        if type(other) is not Package: raise TypeError("Only Package types can be added to a PackageGroup!")

        if self.company != other.company: raise ValueError("Company of Package is different than that of Package Group")

        if other not in self:
            self.packages.append(other)
            self.packages.sort()
            self.packages.reverse()
            self.cost += round(self.cost + other.cost, 2)
            return self
        else:
            return self
    def __lt__(self, other):
        return self.company < other.company

    def __eq__(self, other):
        return self.company == other.company

def loadPackages():

    with open("packages.dat") as file:
        data = file.readlines()
        all = file.read()
    companySet = set()
    del data[0]
    for comp in data:
        company = comp.split(",")[0].strip('"')
        companySet.add(company)

    for comp in list(companySet):
        packList =[]
        for line in data:
            company = line.split(",")[0].strip('"')
            if comp == company:
                start = re.search(r', "(.+?)')
                packList.append(1)

    return companySet
# # No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# 
# This block is optional and can be used for testing .
# We will NOT look into its content .
# 

if __name__ == "__main__":
    source = "14120"
    dest = "71280"
    print(calculateCost(source, dest))
    pack1 = Package("Prophecy_Arts", "3 N. Ocean Court, Victoria, TX 77904", "4 Elm Road, North Haven, CT 06473")
    pack2 = Package("Prophecy_Arts", "9725 Sheffield Avenue, Mount Vernon, NY 10550", "9679 Edgewater Lane, Lorton, VA 22079")
    print(pack1)
    print(pack2)
    group1 = pack1 + pack2
    group = PackageGroup("Prophecy_Arts", [pack1, pack2])
    print(group.getByZip({"77904", "22079"}))
    print(group.getByState({"NY"}))
    print(group.getByCity({"Victoria", "Lorton"}))
    print(group)
    print(group1)
    print(loadPackages())
# Write anything here to test your code .