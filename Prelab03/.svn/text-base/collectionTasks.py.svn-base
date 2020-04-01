# ######################################################
# Author : Mark Dunn
# email : dunn60@purdue.edu
# ID : ee364a12
# Date : 09/05/19
# ######################################################
import os # List of module import statements
import sys # Each one on a line
import glob
# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################
def getComponentCountByProject(projectID: str, componentSymbol: str) -> int:
    compUsed = 0
    projectdic = projectsDic(1)

    if projectID not in projectdic.keys():
        raise ValueError(f"Project ID: {projectID} does not Exist")

    componentsDic = compDic(componentSymbol)
    circuitList = projectdic[projectID]

    allComponents = []
    for value in circuitList:
        allComponents = allComponents + circuitInfo(value, True)[1]

    for element in allComponents:
        if element in componentsDic.keys(): compUsed += 1

    return compUsed

def getComponentCountByStudent(student: str, componenetSymbol: str) -> int:
    compCount = 0
    circuitList = glob.glob("circuits/*.dat")
    compTypeDic = compDic(componenetSymbol)
    students = studentDic()

    if student not in students.keys():
        raise ValueError(f"Student: {student} is not Enrolled.")
    student = students[student]
    componentsUsed = []

    for element in circuitList:
        circInf = circuitInfo(element, False)
        if student in circInf[0]: componentsUsed += circInf[1]
    if len(componentsUsed) == 0: return 0

    for element in componentsUsed:
        if element in compTypeDic.keys(): compCount +=1
    return compCount

def getParticipationByStudent(studentName: str) -> set:
    projects = set([])

    studentId = studentDic()[studentName]


    if studentName not in studentDic().keys():
        raise ValueError(f"Student: {studentName} is not Enrolled.")

    circuitDic = projectsDic(0)
    circuitList = glob.glob("circuits/*.dat")

    for value in circuitList:
        circInf = circuitInfo(value, False)
        if studentId in circInf[0]:projects.add(circuitDic[value.strip("circuits/circuit_.dat")])

    return projects

def getParticipationByProject(projectID : str) -> set:
    students = set([])
    if projectID not in projectsDic().keys():
        raise ValueError(f"The Project with ID:{projectID} does not exist.")


    circList = projectsDic(1)[projectID]

    studentDicionary = studentDic()

    reverseStudent = {v : k for k, v in studentDicionary.items()}
    studentIDs = []
    for element in circList:
        studentIDs += circuitInfo(element, True)[0]

    for ID in studentIDs: students.add(reverseStudent[ID])

    return students

def getCostOfProjects() -> dict:
    projCosts = {}
    projectDictionary = projectsDic(1)
    projIDs = projectDictionary.keys()

    componentDictionary = compDic("I")
    componentDictionary.update(compDic("T"))
    componentDictionary.update(compDic("C"))
    componentDictionary.update(compDic("R"))

    curCompList = []
    curCost = 0

    for ID in projIDs:
        for circuit in projectDictionary[ID]:
            curCompList += circuitInfo(circuit, True)[1]

        for component in curCompList: curCost += componentDictionary[component]
        projCosts[ID] = round(curCost, 2)
        curCompList = []
        curCost = 0

    return projCosts

def getProjectByComponent(componentIDs: set) -> set:
    projUsed = set([])

    projectDictionary = projectsDic(1)

    for ID in projectDictionary:
        for circuit in projectDictionary[ID]:
            for component in circuitInfo(circuit, True)[1]:
                if component in componentIDs: projUsed.add(ID)
    return projUsed

def getCommonByProject(projectID1: str, projectID2: str) -> list:

    projTwoCircuits = projectsDic(1)[projectID2]
    compOne =[]
    compTwo =[]
    sharedComp = []
    for circuit in projectsDic(1)[projectID1]:
        compOne += circuitInfo(circuit, True)[1]
    for circuit in projectsDic(1)[projectID2]:
        compTwo += circuitInfo(circuit, True)[1]

    for component in compOne:
        if component in compTwo and component not in sharedComp: sharedComp.append(component)
    sharedComp.sort()
    return sharedComp

def getComponentReport(componentIDs: set) -> dict:
    timesUsed = {}
    for comp in componentIDs: timesUsed[comp] = 0

    circuitList = glob.glob("circuits/*.dat")

    for circuit in circuitList:
        compList = circuitInfo(circuit, False)[1]
        for component in componentIDs:
            if component in compList: timesUsed[component] += 1

    return timesUsed

def getCircuitByStudent(studentNames: set) -> set:

    circuitSet = set([])
    circuitList = glob.glob("circuits/*.dat")
    studentIDs = set([])
    studenDictionary = studentDic()

    for name in studentNames: studentIDs.add(studenDictionary[name])
    for circuit in circuitList:
        if studentIDs.isdisjoint(set(circuitInfo(circuit, False)[0])) is False:
            circuitSet.add((circuit.strip("circuits/circuit_.dat")))
    return circuitSet

def getCircuitByComponent(componentIDs: set) -> set:

    circuitIDs = set([])
    circuitList = glob.glob("circuits/*.dat")
    for circuit in circuitList:
        if componentIDs.isdisjoint(set(circuitInfo(circuit, False)[1])) is False:
            circuitIDs.add((circuit.strip("circuits/circuit_.dat")))
    return circuitIDs
# HELPER FUNCTIONS
###############################################################
def circuitInfo(number: str, path: bool) -> list:

    if path is True: filename = "circuits/circuit_" + number + ".dat"
    else: filename = number
    with open(filename) as file:
        data = file.read()

    data = data.split("Components:\n")
    data[0] = data[0].split()
    data[1] = data[1].split()
    del data[0][0]
    del data[0][0]
    del data[1][0]
# data[0] is a list of student IDs in circuit ; data[1] is a list of the components in the circuit#
    return data

#Returns a dictionary of {componenetID: cost}
def compDic(compName: str) -> dict:
    if compName == "I": filename = "maps/inductors.dat"
    elif compName == "R": filename = "maps/resistors.dat"
    elif compName == "C": filename = "maps/capacitors.dat"
    else: filename = "maps/transistors.dat"

    with open(filename) as file:
        data = file.readlines()
    del data[0]
    del data[0]
    del data[0]
    comps = {}
    for i in range(len(data)):
        data[i] = data[i].strip().split("$")
        comps[data[i][0].strip()] = float(data[i][1])
    return comps

#Returns a dictionary of {StudentName: studentID}
def studentDic() -> dict:
    students = {}
    with open("maps/students.dat") as file:
        data = file.readlines()
    del data[0]
    del data[0]
    for i in range(len(data)):
        data[i] = data[i].rstrip().split("|")
        students[data[i][0].strip()] = data[i][1].strip()
    return students
# Returns a dictionary of projectId as keys with a list of circuits
def projectsDic(order:int) -> dict:
    with open("maps/projects.dat") as file:
        data = file.readlines()
    del data[0]
    del data[0]
    proj = {}

    if order == 1:
        for i in range(len(data)):
            data[i] = (data[i].rstrip())
            data[i] = data[i].split()
            if data[i][1] in proj.keys(): proj[data[i][1]].append(data[i][0])
            else: proj[data[i][1]] = [data[i][0]]
    else:
        for i in range(len(data)):
            data[i] = (data[i].rstrip())
            data[i] = data[i].split()
            proj[data[i][0]] = data[i][1]
    return proj
# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################


if __name__ == "__main__":
    # Write anything here to test your code .
    y = getComponentCountByProject("90BE0D09-1438-414A-A38B-8309A49C02EF", "T")
    z = getParticipationByStudent("Alexander, Carlos")
    testset = set([])
    testset.add("CRV-843")
    testset.add("UTH-014")
    testset.add("YDR-391")
    x = getComponentReport(testset)
    w = getCircuitByComponent(testset)
    print(w)


