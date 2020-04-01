# # Author : Mark Dunn
# email : dunn60@purdue.edu
# ID : ee364a12
# Date : 10/29/19
# import os # List of module import statements
import sys  # Each one on a line
import re


# # No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# 
# This block is optional and can be used for testing .
# We will NOT look into its content .
# 

def getNumberPattern() -> str:
    pattern =r"[-+]*[0-9]\.[0-9]+?[Ee][-+]*[0-9]+|[-+]*\d+?\.\d+|[-+]*\d+"
    return pattern
def getLinkPattern() -> str:

    pattern = r'<a href="(?P<url>(https://|ftp://|http://|ftps://)[\S]+?)">(?P<text>[\w ]+?)</a>'
    return pattern

def getDataPattern():
    return r'"([a-zA-Z0-9]+?)"[ ]*?:[ ]*?"(.+?)"[ ]*?'

class Action:

    def __init__(self, act, amo):
        if act != "W" and act != "D": raise ValueError("Not a proper action")
        self.actionType = act
        self.amount = amo

class Client:

    def __init__(self, first, last):
        self.firstName = first
        self.lastName = last
    def __str__(self):
        return f"{self.firstName} {self.lastName}"

class Account:

    def __init__(self, acc, cli, amo, mini):
        self.accountNumber = acc
        self.client = cli
        self.amount = amo
        self.minThreshold = mini
    def __str__(self):
        if self.amount < 0:
            amountnow = -self.amount
            return f"{self.accountNumber}, {self.client}, Balance = (${round(amountnow, 2)})"
        else:
            return f"{self.accountNumber}, {self.client}, Balance = ${round(self.amount, 2)}"
    def performAction(self,actionc):
        if actionc.actionType == "D":
            self.amount = round(self.amount +actionc.amount, 2)
        else:
            if(self.amount - actionc.amount) >= 0:
                self.amount = round(self.amount - actionc.amount, 2)
                if self.amount < self.minThreshold: self.amount -= 10
            else:
                raise ValueError("Account will go below 0 dollars invalid")

class Institute:
    def __init__(self):
        self.accounts = {}
    def createNew(self, fir, las, ac):
        if ac not in self.accounts.keys():
            client1 = Client(fir, las)
            test = Account(ac, client1, 500, 1000)
            self.accounts[ac] = test







if __name__ == "__main__":
    test = getNumberPattern()
    s = "With the electron's charge being -1.6022e-19, some choices you have are -110, -32.0 and +55. Assume that pi equals" \
        "3.145, 'e' equals 2.7 and Na is 6.0221E+023."
    m = re.findall(test, s)
    s = 'You can download the file from <a href="ftps://local.files.io">The Repository</a> or you can search for it <a href' \
        '="https://www.google.com">here.</a>'
    test = getLinkPattern()
    m = re.search(test, s)
    print(m["url"])
    print(m["text"])
    s= '{"firstName" : "George", "lastName" : "Smith", "state" : "New York", "zip" : "20146-4099"}'
    m = re.findall(getDataPattern(), s)
    print(m)
    a = Action("W", 100)
    c = Client("Mark", "Dunn")
    print(c)
    i = Institute()
    i.createNew("123456", "Mark", "Dunn")
    print(i)

# Write anything here to test your code .