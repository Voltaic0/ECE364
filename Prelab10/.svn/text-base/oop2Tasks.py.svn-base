# ######################################################
# Author : Mark Dunn
# email : dunn60@purdue.edu
# ID : ee364a12
# Date : 11/03/19
# ######################################################
from itertools import zip_longest
import copy
from functools import total_ordering
from collections import UserList
from enum import Enum
# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################
@total_ordering
class Datum:
    def __init__(self, *args):
        for val in args:
            if type(val) is not float and type(val) is not int: raise TypeError(f"Inputs must be floats! {val} is not acceptable.\n")
        self._storage = tuple(args)

    def __str__(self):
        temp = tuple()
        for val in self._storage:
            temp += (round(val, 2),)
        return f"{temp}\n"

    def __repr__(self):
        temp = tuple()
        for val in self._storage:
            temp += (round(val, 2),)
        return f"{temp}\n"

    def __hash__(self):
        return hash(self._storage)

    def __iter__(self):
        return iter(self._storage)

    def __contains__(self, item):
        if type(item) is not float and type(item) is not int: raise TypeError(f"{item} is not a float.")
        if item in self._storage: return True
        else: return False

    def __len__(self):
        return len(self._storage)

    def __neg__(self):
        self._storage = tuple(-val for val in self._storage)
        negated = self.clone()
        self._storage = tuple(-val for val in self._storage)
        return negated

    def __getitem__(self, item):
        return list(self._storage)[item]

    def __add__(self, other):
        if type(other) is not Datum and type(other) is not float and type(other) is not int: raise TypeError(f"{other} is not Datum or Float type!")
        elif type(other) is Datum:
            tmp = self._storage
            lis = []
            for each in zip_longest(self, other, fillvalue=0):
                lis.append(each[0]+each[1])
            self._storage = tuple(lis)
            new = self.clone()
            self._storage = tmp
            return new
        else:
            self._storage = tuple(map(lambda x: x + other, self._storage))
            return self

    def __sub__(self, other):
        if type(other) is not Datum and type(other) is not float and type(other) is not int:
            raise TypeError(f"{other} is not Datum or Float type!")
        elif type(other) is Datum:
            tmp = self._storage
            lis = []
            for each in zip_longest(self, other, fillvalue=0):
                lis.append(each[0] - each[1])
            self._storage = tuple(lis)
            new = self.clone()
            self._storage = tmp
            return new
        else:
            tmp = self._storage
            self._storage = tuple(map(lambda x: x - other, self._storage))
            new = self.clone()
            self._storage = tmp
            return new

    def __radd__(self, other):
        if type(other) is not float and type(other) is not int: raise TypeError(f"{other} is not Float type!")
        else:
            tmp = self._storage
            self._storage = tuple(map(lambda x: x + other, self._storage))
            new = self.clone()
            self._storage = tmp
            return new

    def __mul__(self, other):
        if type(other) is not float and type(other) is not int: raise TypeError(f"{other} is not Float type!")
        else:
            tmp = self._storage
            self._storage = tuple(map(lambda x: x * other, self._storage))
            new = self.clone()
            self._storage = tmp
            return new

    def __rmul__(self, other):
        if type(other) is not float and type(other) is not int: raise TypeError(f"{other} is not Float type!")
        else:
            tmp = self._storage
            self._storage = tuple(map(lambda x: x * other, self._storage))
            new = self.clone()
            self._storage = tmp
            return new

    def __truediv__(self, other):
        if type(other) is not float and type(other) is not int: raise TypeError(f"{other} is not Float type!")
        else:
            tmp = self._storage
            self._storage = tuple(map(lambda x: x / other, self._storage))
            new = self.clone()
            self._storage = tmp
            return new

    def __eq__(self, other):
        if type(other) is not Datum: raise TypeError(f"{other} is not of type Datum!")
        else:
            return self.distanceToOrigin() == other.distanceToOrigin()

    def __lt__(self, other):
        if type(other) is not Datum: raise TypeError(f"{other} is not of type Datum!")
        else:
            return self.distanceToOrigin() < other.distanceToOrigin()

    def distanceFrom(self, other):
        if type(other) is not Datum: raise TypeError("Input must have Datum Type.\n")
        sum = 0
        for each in zip_longest(self, other, fillvalue=0):
            sum += (each[0] - each[1])**2
        return sum**(1/2)

    def clone(self):
        return copy.deepcopy(self)

    def distanceToOrigin(self):
        return sum(list(map(lambda x: x*x, self._storage)))**(1/2)

    def compareTimeMax(self, other):
        long = []
        tmp = self._storage
        for each in zip_longest(self, other, fillvalue=0):
            if each[0] >= each[1]: long.append(each[0])
            else: long.append(each[1])
        self._storage = tuple(long)
        new = self.clone()
        self._storage = tmp
        return new

    def compareTimeMin(self, other):
        long = []
        tmp = self._storage
        for each in zip_longest(self, other, fillvalue=0):
            if each[0] <= each[1]: long.append(each[0])
            else: long.append(each[1])
        self._storage = tuple(long)
        new = self.clone()
        self._storage = tmp
        return new

    def compareSun(self, other):
        long = []
        tmp = self._storage
        for each in zip_longest(self, other, fillvalue=0):
            long.append(each[0]+each[1])
        self._storage = tuple(long)
        new = self.clone()
        self._storage = tmp
        return new

class Data(UserList):
    def __init__(self, initial=None):
        if initial is None: super().__init__([])
        else:
            for value in initial:
                if type(value) is not Datum: raise TypeError("Data only stores Datum types!")
            super().__init__(initial)

    def computeBounds(self):
        big = None;
        small = None;
        for datu in self.data:
            if big is None: big = copy.deepcopy(datu)
            if small is None: small = copy.deepcopy(datu)
            big = datu.compareTimeMax(big)
            small = datu.compareTimeMin(small)
        return small, big

    def computeMean(self):
        avg = Datum(0);
        for datu in self.data:
            avg = datu.compareSun(avg)
        return avg / len(self.data)

    def append(self, other):
        if type(other) is Datum:
            super().append(other)
        else: raise TypeError(f"{other} is not a Datum type!")

    def count(self, other):
        if type(other) is Datum:
            super().count(other)
        else: raise TypeError(f"{other} is not a Datum type!")

    def index(self, other, start, stop):
        if type(other) is Datum:
            super().index(other, start, stop)
        else: raise TypeError(f"{other} is not a Datum type!")

    def insert(self, index, other):
        if type(other) is Datum:
            super().insert(index, other)
        else: raise TypeError(f"{other} is not a Datum type!")

    def remove(self, other):
        if type(other) is Datum:
            super().remove(other)
        else: raise TypeError(f"{other} is not a Datum type!")

    def __setitem__(self, key, other):
        if type(other) is Datum:
            super().__setitem__(key, other)
        else: raise TypeError(f"{other} is not a Datum type!")

    def extend(self, other):
        if type(other) is Data:
            super().extend(other)
        else: raise TypeError(f"{other} is not a Data type!")


class DataClass(Enum):
    Class1 = "Class1"
    Class2 = "Class2"


class DataClassifier:
    def __init__(self, group1, group2):
        if type(group1) is not Data: raise TypeError(f"{group1} is not Data type!")
        if type(group2) is not Data: raise TypeError(f"{group2} is not Data type!")
        if len(group1) == 0: raise ValueError(f"Group1 input is empty!")
        if len(group2) == 0: raise ValueError(f"Group2 input is empty!")
        self._class1 = group1
        self._class2 = group2

    def classify(self, other):
        if other in self._class1: return DataClass.Class1
        else: return DataClass.Class2


if __name__ == "__main__":
    test = Datum(6.123, 5.21)
    test2 = Datum(1, 65.12354, 58.15, 90)
    print(test)
    print(test2)
    print(-test2)
    print(test[0])
    print(test.distanceFrom(test2))
    print(test+test2)
    print(test - test2)
    print(test + 15)
    print(15 + test)
    print(test - 15)
    print(test * 15)
    print(5 * test)
    print(test / 15)
    print(test2)
    print(test == test2)
    print(test != test2)
    print(test <= test2)
    print(test >= test2)
    los = [test, test2]
    newly = Data(los)
    print(test)
    print(test2)
    print(newly.computeBounds())
    print(newly.computeMean())
