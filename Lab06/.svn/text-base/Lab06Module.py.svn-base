# # Author : Mark Dunn
# email : dunn60@purdue.edu
# ID : ee364a12
# Date : 10/01/19
# import os # List of module import statements
import sys  # Each one on a line
import glob
import re

# # No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
def getGenres()-> list:

    bookInfo = readBooks()

    genres = set(re.findall(r"<genre>([\w]+?)</genre>", bookInfo))
    genres = list(genres)
    genres.sort()
    return genres
def getAuthorOf(bookName: str) -> str:

    booksInfo = readBooks()
    p = r"<author>(.+?)</author><title>{book}</title>|<author>(.+?)</author>\n.+?<title>{book}</title>".format(book=bookName)
    author = re.search(p, booksInfo)
    if author: name = author[1] if author[1] else author[2]
    else: name=None
    return name

def getBookInfo(bookID: str)-> (str, str):

    booksCatalog = readBooks()
    p = r'<book id="{ident}">\n.+?<author>(.+?)</author><title>(.+?)</title>|<book id="{ident}">\n.+?<author>(.+?)</author>\n.+?<title>(.+?)</title>'.format(ident=bookID)
    bookInfo = re.search(p, booksCatalog)

    if bookInfo:
        name = bookInfo[1] if bookInfo[1] else bookInfo[3]
        title = bookInfo[2] if bookInfo[2] else bookInfo[4]
    else: return None

    return title, name

def getBooksBy(authorName: str) -> list:

    booksCat = readBooks()
    p = r"<author>{name}</author>[\n]*.*?<title>(.+?)</title>".format(name=authorName)
    bookBy = re.findall(p,booksCat)
    bookBy.sort()
    return bookBy

def getBooksBelow(bookPrice: float) -> list:
    bookCat = readBooks()

    bPrices = re.findall(r"<title>(.+?)</title>[\n]*.+?[\n]*.*?<price>(.+?)</price>", bookCat)

    booksBelow = [name for name, price in bPrices if float(price) < bookPrice]
    booksBelow.sort()
    return booksBelow

def searchForWord(word:str) -> list:
    bookCat = readBooks()

    bDesc = re.findall(r"<title>(.+?)</title>[\n]*.+?[\n]*.*?\n*?.*?\n*?<description>(.+?)</description>", bookCat)

    booksWithWord = [title for title, desc in bDesc if (word in title or word in desc)]
    booksWithWord.sort()
    return booksWithWord
#Helpers
def readBooks()-> str:
    with open("books.xml") as file:
        data = file.read()
    return data
# This block is optional and can be used for testing .
# We will NOT look into its content .
# 

if __name__ == "__main__":
    print(getGenres())
    print(getAuthorOf("MSXML3: A Comprehensive Guide"))
    print(getAuthorOf("Visual Studio 7: A Comprehensive Guide"))
    print(getBookInfo("bk109"))
    print(getBooksBy("Corets, Eva"))
    print(getBooksBy("O'Brien, Tim"))
    print(getBooksBelow(40.00))
    print(searchforWord("the"))
# Write anything here to test your code .
