#! /usr/local/bin/python3.7

##############################
#### Lecture 4: More Collections
##############################

"""
References:

* Python Library Reference:
    - collections:          https://docs.python.org/3.7/library/collections.html
    - Copy module:          https://docs.python.org/3.7/library/copy.html
    - Built-in Functions:   https://docs.python.org/3.7/library/functions.html
    - itertools module:     https://docs.python.org/3.7/library/itertools.html
"""

##############################
#### Shallow vs Deep Copy
##############################
import copy
from pprint import pprint as pp

# Some List.
l1 = [4, 5, 6]

# Direct reference.
l2 = l1

# Copies of the list.
l3 = copy.copy(l1)
l4 = copy.deepcopy(l1)

# A dictionary with reference to lists.
myMap = {"Original": l1, "RefCopy": l2, "Copy": l3, "DeepCopy": l4}

print("Initial Assignment:")
pp(myMap)
print()

# Mutate the original list.
l1.insert(0, 10)

print("After Modification:")
pp(myMap)
print()
# ----------------------------------

l5 = [9, 8, 7, 6, 5, 4]

map1 = {"IN": l5}
map2 = map1
map3 = copy.copy(map1)
map4 = copy.deepcopy(map1)

print("Initial Assignment:")
print("Original: {0}".format(map1["IN"]))
print("RefCopy:  {0}".format(map2["IN"]))
print("KeyCopy:  {0}".format(map3["IN"]))
print("DeepCopy: {0}".format(map4["IN"]))
print()

# Mutate the original list.
l5.insert(0, 10)

print("After Modification:")
print("Original: {0}".format(map1["IN"]))
print("RefCopy:  {0}".format(map2["IN"]))
print("KeyCopy:  {0}".format(map3["IN"]))
print("DeepCopy: {0}".format(map4["IN"]))
print()

##############################
#### ChainMap and Counter
##############################

from collections import ChainMap, Counter
from pprint import pprint as pp

d1 = {121: "John the 3rd",
      295: "Todd Son of Aragorn",
      330: "Christine of England",
      559: "Queen Mary of Someplace",
      670: "Elisabeth Trudy Jr."}

d2 = {100: "John",
      200: "Todd",
      300: "Christine",
      500: "Mary",
      670: "Elisabeth"}

chained = ChainMap(d1, d2)
pp(chained)
print("Key = {}, Value = {}".format(121, chained[121]))
print("Key = {}, Value = {}".format(670, chained[670]))

# Get the internal maps as a list (Mutable! So you can shuffle after the fact.)
pp(chained.maps, width=50)

# Create a "reference" to a new ChainMap, prepended with a new map
d3 = {121: "John Smith"}
chained2 = chained.new_child(d3)

print("Original ChainMap:")
pp(chained)
print("Another ChainMap:")
pp(chained2)
print("Key = {}, Value = {}".format(121, chained[121]))
print("Key = {}, Value = {}".format(121, chained2[121]))

# This will cascade into the original objects.
d2[200] = "Michael"
print("Original ChainMap:")
pp(chained)
print("Another ChainMap:")
pp(chained2)

# Example:
phoneMap = {"Alex": "(765) 494-4000", "Mark": "(765) 449-1000", "Lisa": "(765) 137-3000"}
reverseMap = {v: k for k, v in phoneMap.items()}

phoneBook = ChainMap(phoneMap, reverseMap)

entry = "Lisa"; output1 = phoneBook[entry]
print(f"Looking for {entry}. Found {output1}")

entry = "(765) 494-4000"; output2 = phoneBook[entry]
print(f"Looking for {entry}. Found {output2}")

# Counter
IDs = ["8420", "9251", "7591", "5283", "6523", "5116", "6406", "5029",
       "2887", "7591", "5116", "7254", "6523", "8228", "4340", "4340",
       "5116", "5283", "7254", "9251", "4097", "7805", "5029", "5283",
       "7254", "7591", "6523", "9251", "4340", "4097", "5339", "7805",
       "8228", "5116", "9285", "7591", "4097", "8420", "5283", "7796",
       "5028", "3451", "5430", "5339", "7591", "5283", "6406", "7591",
       "5116", "4340", "6523", "7796", "5116", "8420", "5029", "8228",
       "2887", "7796", "8420", "7805", "6523", "8420", "7254", "5283",
       "2887", "9285", "2887", "6406", "8420", "5283", "5029", "9251"]

aggregator = Counter(IDs)
pp(aggregator)

ids1 = ['5028', '3451', '5430']
aggregator.subtract(ids1)
pp(aggregator)
most = aggregator.most_common(1)

element, frequency = most[0]
print(f"Element '{element}' has the highest Frequency = {frequency}")

ids2 = {'5028': 10, '3451': 10, '5430': 10}
aggregator.subtract(ids2)
pp(aggregator)

ids3 = ['1000', '1000', '1000', '2000', '2000', '3000']
aggregator.update(ids3)
pp(aggregator)

ids4 = {'1000': 2, '2000': -3, '3000': 7}
aggregator.update(ids4)
pp(aggregator)

others = [12, 13, 12, 12, 10, 11, 14, 15]
aggregator2 = Counter(others)
pp(aggregator2, width=50)

for element in aggregator2.elements():
    print(element)


aggregator2.subtract([14, 15])
pp(aggregator2, width=50)
for element in aggregator2.elements():
    print(element)

##############################
#### Special functions.
##############################

# enumerate.
values = [28, 12, 71, 64, 26, 97, 1, 7, 100, 68, 57, 92, 29, 53, 8, 13, 84, 58, 69, 90]

for index, value in enumerate(values):
    if index % 2 == 0 and value <= 100:
        print(f"Value = {value:03d}, @ {index}")

# Packing with zip()
from math import sqrt
x = [2, 3, 6]
y = [0, 4, 7]

squaredDifference = []
for first, second in zip(x, y):
    diff = (first - second) ** 2
    squaredDifference.append(diff)

dist = sqrt(sum(squaredDifference))
print(f"Distance = {dist:4.2f}")

# Unpack
rep_list = [('Juan', 68), ('Rodney', 36), ('Edward', 57), ('Christine', 98)]
names, grades = zip(*rep_list)
print("Names = {}\nGrades={}".format(names, grades))

# Unpacking with zip(): Remember args!
def addAll(*args):

    total = 0.
    for value in args: total += value
    return total

print("Summation = {}".format(addAll(1, 2, 3, 4)))


# Unpack into variable inside a function.
def addTwoValues(x, y):
    return x + y

l = [3, 5]
t = 3, 5

w = addTwoValues(*l)
q = addTwoValues(*t)

print(f"The Result of Passing List Elements {l} is: {w}")
print(f"The Result of Passing Tuple Elements {t} is: {q}")


# map with one variable
def scaleBy5(v):
    return 5 * v

vec = [3, 2, 1, 4]
scaledVec = map(scaleBy5, vec) # This is a map object.
print("vector Type is {0}, map Type = {1}".format(type(vec), type(scaledVec)))
print("Original = {0}\n Scaled = {1}".format(vec, list(scaledVec)))


# map with two variables
def getProduct(x, y):
    return x * y

lstX = [2, 3, 6]
lstY = [2, 4, 1]
pProd = map(getProduct, lstX, lstY)
print("X = {0}\nY = {1}\nP = {2}".format(lstX, lstY, list(pProd)))


# filter example.
def isEven(n):
    return n % 2 == 0

values = [28, 12, 71, 64, 26, 97, 1, 7, 100, 68, 57, 92, 29, 53, 8, 13, 84, 58, 69, 90]
evenValues = filter(isEven, values)
print("Values = {0}\nEven =   {1}".format(values, list(evenValues)))

##############################
#### itertools
##############################

import itertools as it

# infinite counter from N. MUST HAVE A STOPPING CONDITION.
for index, number in enumerate(it.count(3, 3)):
    if index > 10: break
    print(f"index = {index}, value = {number}")


# infinite cycler. MUST HAVE A STOPPING CONDITION.
names = ["John", "Mary", "Suzan"]
for index, name in enumerate(it.cycle(names)):
    if index > 10: break
    print(f"index = {index}, value = {name}")