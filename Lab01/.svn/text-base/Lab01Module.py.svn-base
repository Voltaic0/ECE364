# ######################################################
# Author : Mark Dunn
# email : dunn60@purdue.edu
# ID: ee364a12
# Date : 08/27/19
# ######################################################

import os # List of module import statements
import sys # Each one on a line

# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################

def searchForNumber() -> int:

    found = False
    check = 100

    while found is not True:

        listCheck = [list(str(check)), list(str(check*2)), list(str(check*3)), list(str(check*4)), list(str(check*5)), list(str(check*6))]
        listCheck[0].sort()
        listCheck[1].sort()
        listCheck[2].sort()
        listCheck[3].sort()
        listCheck[4].sort()
        listCheck[5].sort()

        inside = True
        for i in range(len(listCheck[0])):
            if(int(listCheck[0][i]) is not int(listCheck[1][i]) or int(listCheck[1][i]) is not int(listCheck[2][i]) or int(listCheck[2][i]) is not int(listCheck[3][i]) or int(listCheck[3][i]) is not int(listCheck[4][i]) or int(listCheck[4][i]) is not int(listCheck[5][i])):
                inside = False

        if(len(listCheck[0]) is len(listCheck[5]) and inside is True): found = True
        check +=1

    answer = check

    return answer

def calculateChain() -> int:

    largestChainLength = 0
    for i in range(1000000):
        currentChain = len(generateChain(i+1))
        if(currentChain > largestChainLength):
            answer = i+1
            largestChainLength = currentChain

    return answer

def generateChain(input: int) -> list:
    foundChain = []
    foundChain.append(input)
    while input is not 1:
        if(input % 2 is 0):
            input = int(input / 2)
            foundChain.append(input)
        else:
            input = int(input *3 +1)
            foundChain.append(input)

    return foundChain



# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################
if __name__ == "__main__":
    print(caclulateChain())
    #Write anything here to test your code .