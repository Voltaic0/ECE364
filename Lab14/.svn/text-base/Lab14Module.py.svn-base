# # Author : Mark Dunn
# email : dunn60@purdue.edu
# ID : ee364a12
# Date : 11/26/19
# import os # List of module import statements
import sys  # Each one on a line
import glob
from enum import Enum
import re
from measurement import *
from collections import Counter
import copy

# # No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# 
# This block is optional and can be used for testing .
# We will NOT look into its content .
# 

class Direction(Enum):
    Incoming = "Incoming"
    Outgoing = "Outgoing"
    Both = "Both"

class Leg:
    def __init__(self, start: str, end: str):
        self.source = start
        self.destination = end

    def __repr__(self):
        src = re.search(r"[0-9]{5}", self.source)[0]
        dest = re.search(r"[0-9]{5}", self.destination)[0]
        return f"{src} => {dest}"

    def __str__(self):
        src = re.search(r"[0-9]{5}", self.source)[0]
        dest = re.search(r"[0-9]{5}", self.destination)[0]
        return f"{src} => {dest}"

    def calculateLength(self, locationMap: dict):
        src = re.search(r"[0-9]{5}", self.source)
        dest = re.search(r"[0-9]{5}", self.destination)
        srcZipCoords = locationMap[src[0]]
        destZipCoords = locationMap[dest[0]]
        dist = calculateDistance(srcZipCoords, destZipCoords)
        return round(dist, 2)

class Trip:
    def __init__(self, per, lgs: list):
        self.person = per
        self.legs = lgs

    def calculateLength(self, locationMap):
        totDist = 0
        for leg in self.legs:
            src = re.search(r"[0-9]{5}", leg.source)
            dest = re.search(r"[0-9]{5}", leg.destination)
            srcZipCoords = locationMap[src[0]]
            destZipCoords = locationMap[dest[0]]
            dist = calculateDistance(srcZipCoords, destZipCoords)
            totDist += dist
        return round(totDist, 2)

    def getLegsByZip(self, zipCode: str, dir: Direction):
        legTime =[]
        if dir == Direction.Incoming:
            for leg in self.legs:
                dest = re.search(r"[0-9]{5}", leg.destination)[0]
                if dest == zipCode:
                    legTime.append(leg)
        elif dir == Direction.Outgoing:
            for leg in self.legs:
                src = re.search(r"[0-9]{5}", leg.source)[0]
                if src == zipCode:
                    legTime.append(leg)
        else:
            for leg in self.legs:
                src = re.search(r"[0-9]{5}", leg.source)[0]
                dest = re.search(r"[0-9]{5}", leg.destination)[0]
                if src == zipCode or dest == zipCode:
                    legTime.append(leg)
        return legTime

    def getLegsByState(self, state: str, dir: Direction):
        legTime = []
        if dir == Direction.Incoming:
            for leg in self.legs:
                dest = re.search(r"[A-Z]{2}", leg.destination)[0]
                if dest == state:
                    legTime.append(leg)
        elif dir == Direction.Outgoing:
            for leg in self.legs:
                src = re.search(r"[A-Z]{2}", leg.source)[0]
                if src == state:
                    legTime.append(leg)
        else:
            for leg in self.legs:
                src = re.search(r"[A-Z]{2}", leg.source)[0]
                dest = re.search(r"[A-Z]{2}", leg.destination)[0]
                if src == state or dest == state:
                    legTime.append(leg)
        return legTime

    def __add__(self, other):
        if type(other) is not Leg and type(other) is not Trip: raise TypeError("Must add trip or leg types only!")
        if type(other) is Leg:
            if other.source != self.legs[len(self.legs) - 1].destination:
                raise ValueError("New leg must have a source equal to destination of Previous Leg!")
            else:
                newTrip = copy.deepcopy(self)
                newTrip.legs.append(other)
                return newTrip
        elif type(other) is Trip:
            if self.person != other.person: raise ValueError("Trips added together must have the same person!")
            newtrip = copy.deepcopy(self)
            for lg in other.legs:
                newTrip = newtrip + lg
            return newTrip


class RoundTrip(Trip):
    def __init__(self, per, lgs):
        if lgs[0].source != lgs[len(lgs) -1].destination:
            raise ValueError("This is not a valid Round Trip!")
        super().__init__(per, lgs)



def getTotalDistanceFor(person:str):
    with open("trips.dat") as file:
        datum = file.readlines()
    with open("locations.dat") as file:
        data = file.readlines()
    mapTime = {}
    del data[0]
    for line in data:
        new = line.split(",")
        new[3]=float(new[3].strip('" '))
        new[2] = float(new[2].strip('" '))
        mapTime[new[0].strip('"')] = (new[2], new[3])

    totalDist = 0

    for line in datum:
        legList = []
        new = line.split(":")
        name = new[0].strip('"')
        if name == person:
            locations = re.findall(r'".+?"', new[1])

            for index, v in enumerate(locations):
                if index != len(locations) -1:
                    legList.append(Leg(v.strip('"'), locations[index+1].strip('"')))
            tripTime = Trip(name, legList)
            totalDist += tripTime.calculateLength(mapTime)

    return round(totalDist, 2)

def getRoundTripCount():
    with open("trips.dat") as file:
        datum = file.readlines()
    total = 0
    for line in datum:
        new = line.split(":")
        locations = re.findall(r'".+?"', new[1])
        if locations[0] == locations[len(locations) -1]:
            total += 1
    return total

def getTrafficCount(**kwargs):
    with open("trips.dat") as file:
        datum = file.readlines()


    if "direction" not in kwargs.keys(): raise ValueError("Need to include a command 'direction='!")
    if type(kwargs["direction"]) is not Direction: raise ValueError("direction must be Direction Enum!")
    if "code" not in kwargs.keys() and "state" not in kwargs.keys(): raise ValueError("Must have argument 'code=' or 'state='!")
    if "code" in kwargs.keys():
        count = 0
        legList = []
        for line in datum:
            new = line.split(":")
            locations = re.findall(r'".+?"', new[1])
            for index, v in enumerate(locations):
                if index != len(locations) - 1:
                    legList.append(Leg(v.strip('"'), locations[index + 1].strip('"')))
            tripTime = Trip(new[0], legList)
            count =+ len(tripTime.getLegsByZip(kwargs["code"], kwargs["direction"]))
        return count
    elif "state" in kwargs.keys():
        count = 0
        legList = []
        for line in datum:
            new = line.split(":")
            locations = re.findall(r'".+?"', new[1])
            for index, v in enumerate(locations):
                if index != len(locations) - 1:
                    legList.append(Leg(v.strip('"'), locations[index + 1].strip('"')))
            tripTime = Trip(new[0], legList)
            count =+ len(tripTime.getLegsByZip(kwargs["state"], kwargs["direction"]))
        return count







if __name__ == "__main__":

    with open("locations.dat") as file:
        data = file.readlines()
    mapTime = {}
    del data[0]
    for liner in data:
        new = liner.split(",")
        new[3]=float(new[3].strip('" '))
        new[2] = float(new[2].strip('" '))
        mapTime[new[0].strip('"')] = (new[2], new[3])
    l = Leg("Morganton, NC 28655", "Groton, MA 01450")
    l1 = Leg("Packwood, WA 98361", "Naples, FL 34108")
    l2 = Leg("Naples, FL 34108", "Hilliard, FL 32046")
    l3 = Leg("Hilliard, FL 32046", "Putnam Station, NY 12861")
    t = Trip("Taylor, Brian", [l1, l2, l3])

    print(t.getLegsByZip("34108", Direction.Incoming))
    print(t.getLegsByZip("34108", Direction.Both))
    print(t.getLegsByZip("99999", Direction.Both))
    print(t.getLegsByState("FL", Direction.Outgoing))
    print(t.getLegsByState("TX", Direction.Both))
    print(t.calculateLength(mapTime))
    print(l.calculateLength(mapTime))
    print(getTotalDistanceFor("Coleman, Lori"))
    print(getTotalDistanceFor("Garcia, Martha"))
    print(getRoundTripCount())

# Write anything here to test your code .