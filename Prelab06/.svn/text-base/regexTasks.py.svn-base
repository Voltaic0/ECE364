# ######################################################
# Author : Mark Dunn
# email : dunn60@purdue.edu
# ID : ee364a12
# Date : 09/26/19
# ######################################################
import os # List of module import statements
import sys # Each one on a line
import re
from uuid import UUID
from collections import Counter
# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################

def getUrlParts(url: str) -> tuple:
    """Retrieves the various parts of inputed url"""
    match = re.search(r"http://(?P<baseAddress>[\w.-]+)/(?P<controller>[\w.-]+)/(?P<action>[\w.-]+)\?", url)
    return match[1], match[2], match[3]

def getQueryParameters(url: str) -> tuple:
    """Gets all the Query parts of a url and returns them as a list of tuples"""
    values = re.findall(r"[?&](.+?)=", url)
    numbers = re.findall(r"=(.+?)(&|$)", url)
    numbers = [value[0] for value in numbers]

    finalVals = [(answer, equals) for answer, equals in zip(values, numbers)]

    return finalVals

def getSpecial(sentence: str, let: str) ->list:
    """Takes in a letter and sentence and then returns a list of strings that either begin or end with that letter
    but not both"""
    pattern = r'\b({letter}\w*[^{letter}\W]|[^{letter}\W]\w*{letter})\b'.format(letter=let)
    values = re.findall(pattern, sentence, re.IGNORECASE)
    return values

def getRealMAC(sentence: str) -> str:
    """Takes in a sentence as a string and returns a MAC address as a string if it exists and None otherwise"""
    address = re.search(r"([a-f\d]{2}[:\-]){5}[a-e\d]{2}", sentence, re.IGNORECASE)

    return address[0] if address else None

def getRejectedEntries() -> list:
    """Returns a sorted list of names who have no information besides their name"""
    employeesInfo = employeeReader()
    rejected = []
    for employee in employeesInfo:
        name, workID, phone, state = decipherInfo(employee)
        if workID is None and phone is None and state is None: rejected.append(name)
    rejected.sort()
    return rejected

def getEmployeesWithIDs() -> {str: str}:
    """Returns a dicitonary of employee names who have ids with the ids as keys"""
    employeeInfo = employeeReader()
    employeeDict = {}
    for employee in employeeInfo:
        name, workID, _, _ = decipherInfo(employee)

        if workID: employeeDict[name] = workID
    return employeeDict

def getEmployeesWithoutIDs() -> list:
    """Returns a sorted list of all employees without IDs"""
    employeeInfo = employeeReader()
    idLess = []
    for employee in employeeInfo:
        name, workID, _, _ = decipherInfo(employee)
        if workID is None: idLess.append(name)
    idLess.sort()
    return idLess

def getEmployeesWithPhones()-> {str: str}:
    """Returns a dicitonary of employee names who have phone numbers with the numbers as keys"""
    employeeInfo = employeeReader()
    employeePhoneDict = {}
    for employee in employeeInfo:
        name, _, phone, _ = decipherInfo(employee)

        if phone: employeePhoneDict[name] = phone
    return employeePhoneDict

def getEmployeesWithStates()-> {str: str}:
    """Returns a dicitonary of employee names who have states with the states as keys"""
    employeeInfo = employeeReader()
    employeeStateDict = {}
    for employee in employeeInfo:
        name, _, _, state = decipherInfo(employee)

        if state: employeeStateDict[name] = state
    return employeeStateDict

def getCompleteEntries()-> {str: (str, str, str)}:
    """Returns of dicitonary of names who contain a phone number, id, and state with that information in a
    tuple as keys"""
    employeeInfo = employeeReader()
    completeDict = {}
    for employee in employeeInfo:
        name, workID, phone, state = decipherInfo(employee)
        if workID and phone and state: completeDict[name] = (workID, phone, state)
    return completeDict


def decipherInfo(info: str) -> tuple:
    """Takes in a string of employee info unparsed and returns all relevant information in tuple of
    form(Full Name, ID, Phone#, State"""
    name = re.search(r"((?P<first>[\w]+) (?P<last>[\w]+)+),|((?P<last2>[\w]+)+, (?P<first2>[\w]+)+),", info)
    fullName = (name["first"]+" "+name["last"]) if name["first"] else (name["first2"]+" "+name["last2"])

    idPattern = r"([,{](([a-f\d]{8})-([a-f\d]{4})-([a-f\d]{4})-([a-f\d]{4})-([a-f\d]{12}))[,}]|([a-f\d]{32}))"
    findID = re.search(idPattern, info, re.IGNORECASE)
    if findID is not None: empID = findID[8] if findID[8] else findID[3]+findID[4]+findID[5]+findID[6]+findID[7]
    else: empID = None
    if empID: empID = str(UUID("{"+empID+"}"))

    findPhone = re.search(r"(\([\d]{3}\) [\d]{3}-[\d]{4});|([\d]{3})-([\d]{3}-[\d]{4});|([\d]{3})([\d]{3})([\d]{4});", info)
    if findPhone:
        curNumber = "("+findPhone[4]+") "+findPhone[5]+"-"+findPhone[6] if findPhone[6] else None
        phoneNum = curNumber if findPhone[6] else ("("+findPhone[2]+") "+findPhone[3]) if findPhone[3] else findPhone[1]
    else: phoneNum = None

    findState = re.search(r",,([\w ]+)\s", info)
    if findState:
        stateHood = findState[1]
    else: stateHood = None

    return fullName, empID, phoneNum, stateHood
def employeeReader()-> list:
    """"Helper Function that opens the Employee file and returns a list of strings that contain employee info"""
    with open("Employees.dat") as file:
        data = file.readlines()
    return data
# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################
if __name__ == "__main__":
    print(getUrlParts("http://www.purdue.edu/Home/Calendar?Year=2016&Month=September&Semester=Fall"))
    print(getQueryParameters("http://www.purdue.edu/Home/Calendar?Year=2016&Month=September&Semester=Fall"))
    s = "The TART program runs on Tuesdays and Thursdays, but it does not start until next week that."
    print(getSpecial(s, "p"))
    s = "The TART program runs on Tuesdays and Thursdays, but it does not 58:1C:0A:6E:39:4C start until next week that."
    print(getRealMAC(s))
    print(getRejectedEntries())
    print(getEmployeesWithIDs())
    print(getEmployeesWithoutIDs())
    print(getEmployeesWithPhones())
    print(getEmployeesWithStates())
    print(getCompleteEntries())
# Write anything here to test your code .
