# # Author : Mark Dunn
# email : dunn60@purdue.edu
# ID : ee364a12
# Date : 11/05/19
import os # List of module import statements
import sys  # Each one on a line
from functools import total_ordering

# # No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
@total_ordering
class TimeSpan:
    def __init__(self, **kwargs):
        if kwargs["weeks"] < 0 or kwargs["days"] < 0 or kwargs["hours"] < 0: raise ValueError("The arguments cannot be negative!")

        self.weeks = kwargs["weeks"]
        self.days = kwargs["days"]
        self.hours = kwargs["hours"]
        if self.hours > 23:
            self. days += int(self.hours / 24)
            self.hours = self.hours % 24
        if self.days > 6:
            self.weeks += int(self.days / 7)
            self.days = self.days % 7

    def __str__(self):
        if self.weeks < 10:
            return f"{self.weeks:02d}W {self.days:01d}D {self.hours:02d}H"
        else:
            return f"{self.weeks}W {self.days:01d}D {self.hours:02d}H"

    def __repr__(self):
        if self.weeks < 10:
            return f"{self.weeks:02d}W {self.days:01d}D {self.hours:02d}H"
        else:
            return f"{self.weeks}W {self.days:01d}D {self.hours:02d}H"

    def getTotalHours(self):
        total = int(self.weeks*7*24 + self.hours + self.days *24)
        return total

    def __add__(self, other):
        if type(other) is not TimeSpan: raise TypeError("Addition must be between two TimeSpan types.\n")
        nweeks = self.weeks + other.weeks
        ndays = self.days + other.days
        nhours = self.hours + other.hours

        return TimeSpan(weeks=nweeks, days=ndays, hours=nhours)

    def __mul__(self, other):
        if type(other) is not int: raise TypeError("Expected integer multiplication.")
        if other <= 0: raise ValueError("Must multiply by number greater than 0.")
        nweeks = self.weeks * other
        ndays = self.days * other
        nhours = self.hours * other

        return TimeSpan(weeks=nweeks, days=ndays, hours=nhours)

    def __rmul__(self, other):
        if type(other) is not int: raise TypeError("Expected integer multiplication.")
        if other <= 0: raise ValueError("Must multiply by number greater than 0.")
        nweeks = self.weeks * other
        ndays = self.days * other
        nhours = self.hours * other

        return TimeSpan(weeks=nweeks, days=ndays, hours=nhours)

    def __eq__(self, other):
        return self.days == other.days and self.hours == other.hours and self.weeks == other.weeks

    def __lt__(self, other):
        total = self.weeks*7*24 + self.hours + self.days *24
        total2 = other.weeks*7*24 + other.hours + other.days *24
        return total < total2


# This block is optional and can be used for testing .
# We will NOT look into its content .
# 

if __name__ == "__main__":
    ts = TimeSpan(weeks=100, days=15, hours=49)
    ts2 = TimeSpan(weeks=0, days=5, hours=10)
    ts3 = TimeSpan(weeks=102, days=3, hours=1)
    print(ts)
    print(ts.getTotalHours())
    print(ts2.getTotalHours())
    print(ts < ts2)
    print(ts > ts2)
    print(ts < ts3)
    print(ts == ts3)
# Write anything here to test your code .