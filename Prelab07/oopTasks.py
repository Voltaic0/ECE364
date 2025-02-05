# # Author : Mark Dunn
# email : dunn60@purdue.edu
# ID : ee364a12
# Date : 10/02/19
# import os # List of module import statements
import sys  # Each one on a line
from enum import Enum

# # No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !

class Level(Enum):
    Freshman = "Freshman"
    Sophomore = "Sophomore"
    Junior = "Junior"
    Senior = "Senior"

class ComponentType(Enum):
    Resistor = "Resistor"
    Capacitor = "Capacitor"
    Inductor = "Inductor"
    Transistor = "Transistor"

class Student:
    def __init__(self, ID, first, last, level):
        self.ID = ID
        self.firstName = first
        self.LastName = last
        if type(level) is Level: self.level = level
        else: raise TypeError("The 4th argument must be an instance of the 'Level' Enum.")

    def __str__(self):
        return f"{self.ID}, {self.firstName} {self.LastName}, {self.level.value}"

class Component:
    def __init__(self, ID, ctype, price):
        self.ID = ID
        self.price = price

        if type(ctype) is ComponentType: self.ctype = ctype
        else: raise TypeError("Second argument must have type 'ComponentType' Enum")

    def __str__(self):
        return f"{self.ctype.value}, {self.ID}, ${round(self.price, 2)}"
    def __repr__(self):
        return(f"{self.ID}")

    def __hash__(self):
        return hash(self.ID)

class Circuit:
    def __init__(self, ID, components, cost):
        self.ID = ID
        self.cost = cost
        for value in components:
            if type(value) is not Component: raise TypeError("Components in set are not all of type 'Component'.")
        self.components = components

    def __str__(self):
        resistorCount = 0; capacitorCount = 0; inductorCount = 0; transistorCount = 0

        for value in self.components:
            if value.ctype is ComponentType.Resistor: resistorCount += 1
            elif value.ctype is ComponentType.Capacitor: capacitorCount += 1
            elif value.ctype is ComponentType.Inductor: inductorCount += 1
            elif value.ctype is ComponentType.Transistor: transistorCount += 1
        return (f"{self.ID}: (R = {resistorCount:02d}, C = {capacitorCount:02d}, I = {inductorCount:02d},"
                f" T = {transistorCount:02d}), Cost = ${round(self.cost, 2)}")

    def getByType(self, compType) -> set:
        if type(compType) is not ComponentType: raise ValueError("Expected input with a ComponentType Enum value.")
        parts = set()
        for value in self.components:
            if value.ctype is compType: parts.add(value)
        return parts

    def __contains__(self, component):
        if type(component) is not Component: raise TypeError("The component to check is not of type 'Component'.")
        for value in self.components:
            if(component.ctype is value.ctype) and (component.ID == value.ID) and (component.price == value.price):
                return True
        return False
    def __sub__(self, comp):
        if type(comp) is not Component: raise TypeError("The component to check is not of type 'Component'.")
        if comp not in self: return self
        for value in self.components:
            if (comp.ctype is value.ctype) and (comp.ID == value.ID) and (comp.price == value.price):
                self.components.remove(value)
                self.cost -= value.price
                break
        return self
    def __add__(self, comp):
        if type(comp) is not Component: raise TypeError("The component to check is not of type 'Component'.")
        if comp in self: return self
        self.components.add(comp)
        self.cost += comp.price
        return self
    def __eq__(self, circuit2):
        if type(circuit2) is not Circuit: raise TypeError("Both objects must be of type 'Circuit' when comparing.")
        return self.cost == circuit2.cost
    def __lt__(self, circuit2):
        if type(circuit2) is not Circuit: raise TypeError("Both objects must be of type 'Circuit' when comparing.")
        return self.cost < circuit2.cost
    def __gt__(self, circuit2):
        if type(circuit2) is not Circuit: raise TypeError("Both objects must be of type 'Circuit' when comparing.")
        return self.cost > circuit2.cost

class Project:
    def __init__(self, ID, participants, circuits):
        self.ID = ID
        for value in participants:
            if type(value) is not Student: raise ValueError("Not all participants are Students.")
        self.participants = participants
        for value in circuits:
            if type(value) is not Circuit: raise ValueError("Not all circuits are  actual Circuits.")
        self.circuits = circuits
        self.cost = round(sum([value.cost for value in self.circuits]), 2)
    def __str__(self):
        return (f"{self.ID}: ({len(self.circuits):02d} Circuits, {len(self.participants):02d} Participants),"
                f" Cost = ${self.cost}")
    def __contains__(self, comp):
        if type(comp) is not Component and type(comp) is not Circuit and type(comp) is not Student:
            raise TypeError("Object must have type 'Component', 'Circuit', or 'Student' to check if in Project.")
        if type(comp) is Component:
            for value in self.circuits:
                if comp in value: return True
            return False
        elif type(comp) is Circuit:
            for value in self.circuits:
                if comp.ID is value.ID: return True
            return False
        else:
            for value in self.participants:
                if comp.ID is value.ID: return True
            return False
    def __add__(self, circ):
        if type(circ) is not Circuit: raise TypeError("Addition operand must have the type 'Circuit'.")
        for value in self.circuits:
            if value.ID == circ.ID: return self
        self.circuits.append(circ)
        self.cost = round(self.cost+circ.cost, 2)
        return self
    def __sub__(self, circ):
        if type(circ) is not Circuit: raise TypeError("Addition operand must have the type 'Circuit'.")
        for value in self.circuits:
            if value.ID == circ.ID: return self
        self.circuits.remove(circ)
        self.cost = round(self.cost-circ.cost, 2)
        return self
    def __getitem__(self, id):
        for value in self.circuits:
            if value.ID == id: return value
        raise KeyError(f"Circuit ID:{id} does not exist within this project.")

class Capstone(Project):
    def __init__(self, **kwargs):
        if "project" in kwargs.keys():
            v = kwargs["project"]
            for stud in v.participants:
                if stud.level is not Level.Senior:
                    raise ValueError("All students participating in Capstone Project must be Seniors.")
            super().__init__(v.ID, v.participants, v.circuits)
        else:
            for stud in kwargs["participants"]:
                if stud.level is not Level.Senior:
                    raise ValueError("All students participating in Capstone Project must be Seniors.")
            super().__init__(kwargs["ID"], kwargs["participants"], kwargs["circuits"])



# This block is optional and can be used for testing .
# We will NOT look into its content .
# 

if __name__ == "__main__":
    test = Student("15487-79431", "John", "Smith", Level.Senior)
    print(test)
    test2 = Component("REW-321", ComponentType.Resistor, 1.40)
    print(test2)
    setting = set()
    for i in range(10): setting.add(test2);  test2 = Component(f"{i}", ComponentType.Transistor, 1.40)
    circuit3 = Circuit("Special", setting, 150.00)
    print(circuit3)
    print(test2 in circuit3)
    print(circuit3.getByType(ComponentType.Resistor))
    test2 = Component(f"8", ComponentType.Transistor, 1.40)
    circuit3 -= test2
    circuit4 = Circuit("Special", setting, 150.00)
    print(circuit3.cost, circuit4.cost)
    print(circuit4 < circuit3)

    project = Project("Proj", [test], [circuit3, circuit4])
    print(project)
    test2 = Component(f"5", ComponentType.Transistor, 1.40)
    print(test2 in project)
    test = Student("15487-79401", "John", "Smith", Level.Sophomore)
    circuit4 = Circuit("Special", setting, 150.00)
    #project.participants.append(test)
    project += circuit4
    print(project["Special"])
    cap = Capstone(ID=project.ID, participants=project.participants, circuits=project.circuits)
    print(cap)
    # Write anything here to test your code .