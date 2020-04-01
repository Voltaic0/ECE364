##############################
# Lecture 7: OOP
##############################
import os


class MyClass:

    # Special methods.
    # ####################################
    def __init__(self, someVar):

        # Attributes -- Member Variables -- fields -- properties
        self._backingStore = 0
        self.userCount = 0
        self.someVar = someVar

    def __str__(self):
        # Must return a string.
        pass

    # operator Overloads.
    # ####################################
    def __add__(self, other):
        pass

    def __eq__(self, **kwargs):
        pass

    # Methods, or Member functions. Public & Private.
    # ####################################
    def _processUser(self, userName):       # Private function, by convention.
        pass

    def addUser(self, userName):
        pass
        

class AnotherClass(MyClass):

    def __init__(self, newVar):

        self.newVar = newVar

        # You "should" invoke the parent initializer!
        super().__init__(newVar)
        # OR
        # MyClass.__init__(self, newVar)

        pass

    # If the function already exists in the parent, and you add
    # it in the child, you are "overriding" that function.
    def addUser(self, userName):
        pass
