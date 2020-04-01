#! /usr/local/bin/python3.7

##############################
## Lecture 03: Exceptions
##############################

"""
References:

* Python Tutorials: Section 8
    https://docs.python.org/3.7/tutorial/errors.html
* Python Library Reference: Built-in Exceptions
    https://docs.python.org/3.7/library/exceptions.html
* Python Reference Book:
    Chapter 8
"""

x = 3

# Unplanned.
sentence = "Hello " + x

# Example 1: Simple
try:
    sentence2 = "Hello " + x
    print("It is Thursday!")
except:
    print("Example 1: Something is off.")


# Example 2: Except and else.

try:
    z = 1 / 0
except ArithmeticError as ex:
    print(f"Example 2: unexpected error: {ex}.")
else:
    print("Example 2: Operation ran without issues.")


# Example 3: Except, else & Finally

try:
    # fileName = "ScoobyDoo.py"
    fileName = "L3Samples.py"
    with open(fileName, "r") as pFile:
        lines = pFile.read()

except OSError as ex:
    print(f"Example 3: unexpected error: {ex}.")
else:
    print("Example 3: Operation ran without issues.")
finally:
    print("Operation complete!")


# Example 4
mapEx = {1: "Hello"}  # Key = 1

try:
    # # Possible Arithmetic Error.
    # z = 1 / 0

    # Possible Key Error.
    print(mapEx[33])
    # print(mapEx[1])

    # Possible Type Error.
    # print(mapEx[1] + 3)

except ZeroDivisionError as ze:
    print("Caught the error: " + ze.args[0])
except KeyError as ke:
    print(f"Caught a Key Error, with key: {ke}")
# except (ZeroDivisionError, KeyError) as x:
#     print("Caught a ZeroDivisionError or a KeyError: ".format(x.args[0]))
# except Exception as e:
#     print("Caught an Error. Exception: {0}, Message: {1}".format(type(e), e.args[0]))
else:
    print("In the 'else' clause.")
finally:
    print("Final Cleanup")

print("After Exception blocks.")


# Example 5:
def combine(x, y):
    if x < 0:
        raise ValueError("The value of x should be above 0.")

    return x + y
