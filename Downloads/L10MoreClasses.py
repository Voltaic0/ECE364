#! /usr/local/bin/python3.7

##############################
#### Lecture 8: More OOP
##############################
"""
References:

* Python Docs:
    - Classes                       https://docs.python.org/3.7/tutorial/classes.html
    - Data Model                    https://docs.python.org/3.7/reference/datamodel.html
    - Modules: * functools          https://docs.python.org/3.7/library/functools.html  
               * Functional         https://docs.python.org/3.7/howto/functional.html?highlight=lambda
               * Introspection      https://docs.python.org/3.7/library/inspect.html

    * Websites:
    - Real Python                   https://realpython.com/python3-object-oriented-programming/
    - The Python Guru               https://thepythonguru.com/python-operator-overloading/
"""

from pprint import pprint as pp
from functools import total_ordering


# Class variables vs. Instance variables.
#######################################################
class Numbers:

    # Class Variables: They exist across all instances.
    # They should be immutable!
    one = 0
    two = "Hello"

    # Should NOT be here, or you will incur problems.
    three = [1, 2, 3]

    def __init__(self):

        # All mutable variables should be here.
        self.four = [4, 5, 6]

    def addToValue(self, i):
        self.one += i

x = Numbers()
y = Numbers()
pp(x.three)

x.three.insert(0, 0)
pp(y.three)

pp(x.four)
x.four.insert(0, 9)
pp(y.four)


# Dynamic Classes
#######################################################
class Empty:
    pass


x1 = Empty()
x2 = Empty()


x1.firstName = "Mary"
x1.lastName = "Smith"

x2.SSN = "123-45-6789"
x2.State = "IN"

# Dynamic Access of attributes.
if hasattr(x2, "firstName"):
    firstName1 = getattr(x1, "firstName", "Not Here!")
    print(firstName1)
else:
    print("Attribute NOT found!")

firstName2 = getattr(x2, "firstName", "Not Here!")
print(firstName2)

setattr(x1, "SSN", "098-34-1234")


# Aliases & Function variables
#######################################################
class EmptyAlias:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0


x1 = EmptyAlias()
print(x1.x, x1.y)

DifferentAlias = EmptyAlias
x2 = DifferentAlias()
print(x2.x, x2.y)


# Stateful Functions.
class NumberChange:

    def __init__(self, initial):
        self.store = initial
        self.tally = [initial]

    def __call__(self, value):
        self.tally.append(value)
        self.store += value


aggregate = NumberChange(100)
aggregate(10)
aggregate(20)
aggregate(40)

print(aggregate.tally)
print(aggregate.store)

# Rich Comparison
###########################################################
@total_ordering
class Comparator:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value


x = Comparator(3)
y = Comparator(12)
print(x == y)
print(x != y)
print(x < y)
print(x >= y)
print(x > y)
print(x <= y)


# Introspection
########################################################
import inspect
import L7Classes as TestModule

classes = inspect.getmembers(TestModule, inspect.isclass)



