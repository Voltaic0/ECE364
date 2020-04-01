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
def getDifference(provider1: str, provider2: str) -> set:

    providers = glob.glob("providers/*.dat")

    if ("providers/" + provider1 + ".dat") not in providers:
        raise ValueError(f"Provider: {provider1} does not exist!")
    elif ("providers/" + provider2 + ".dat") not in providers:
        raise ValueError(f"Provider: {provider2} does not exist!")

    prov1Comp = set(provDict(provider1).keys())
    prov2Comp = set(provDict(provider2).keys())

    return prov1Comp.difference(prov2Comp)

def getPriceOf(sbc: str, provider: str) -> float:
    providers = glob.glob("providers/*.dat")
    if ("providers/" + provider + ".dat") not in providers:
        raise ValueError(f"Provider: {provider} does not exist!")

    provDictionary = provDict(provider)

    return provDictionary[sbc]

def checkAllPrices(sbcSet: set) ->dict:
    providers = glob.glob("providers/*.dat")
    sbcDictPrices ={}
    sbcDictProviders = {}
    for value in sbcSet:
        sbcDictPrices[value] = 100000000
    for provider in providers:
        prov = provider.split("/")[1].strip(".dat")
        provDictionary = provDict(prov)

        for value in sbcSet:
            if value in provDictionary.keys():
                if provDictionary[value] < sbcDictPrices[value]:
                    sbcDictPrices[value] = provDictionary[value]
                    sbcDictProviders[value] = prov
    sbcReturn ={}
    for value in sbcSet:
        sbcReturn[value] = (sbcDictPrices[value], sbcDictProviders[value])

    return sbcReturn


######HELPER
def provDict(provider: str)-> dict:
    provDictionary ={}
    with open("providers/"+provider+".dat") as file:
        data = file.readlines()
    del data[0]
    del data[0]
    del data[0]
    for value in data:
        component = value.split(",")[0].strip()
        price = value.split(",")[1].strip()
        provDictionary[component] = float(price.strip("$"))
    return provDictionary

# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################


if __name__ == "__main__":
    # Write anything here to test your code .
    print(getDifference("provider2", "provider4"))
    print(getPriceOf("Rasp. Pi-4702MQ", "provider2"))
    print(checkAllPrices({'Rasp. Pi-6700TE', 'Rasp. Pi-5750HQ', 'Rasp. Pi-6700', 'Rasp. Pi-5650U', 'Rasp. Pi-6770HQ', 'Rasp. Pi-6700T'}))