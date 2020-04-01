#! /usr/local/bin/python3.7

#####################################
#### Lecture 6: Regular Expressions
#####################################

"""
References:

* Python Library Reference:
    - Python HOWTOs:                https://docs.python.org/3.7/howto/regex.html
    - Regular Expressions Ref:      https://docs.python.org/3.7/library/re.html

* Python Reference Book:
    - Chapter 10.
* RegEx Game:                       https://regexcrossword.com/
"""

import re
from pprint import pprint as pp

# Exact Match. Already in str methods.
# For the RegEx Prelab + Lab, DO NOT USE STRING METHODS!!
#########################################
s = "Today is Monday. Tomorrow is Tuesday"
pp(s.find("Tuesday"))

# Motivation.   NOTE: All patterns are recommended to be RAW. Special characters can be escaped.
#########################################
s = "Mary is scheduled for Feb 1st, John for the 2nd, and Lisa for the 3rd."
pattern = r"(\dst|\dnd|\drd)"
multiple = re.findall(pattern, s)
pp(multiple)

# Disjunction: OR-ing Options.      Symbol:     '|'
#########################################
s = "In order to capture the vertical bar |, you must escape!"
single = re.search(r"(\||!)", s)
pp(single[1])
multiple = re.findall(r"(\||!)", s)
pp(multiple)

s = "Today is Monday. Tomorrow is Tuesday"
pattern = r"(Friday|Sunday|Monday|Tuesday)"

# Regex find ONLY the first match.
single = re.search(pattern, s)
pp(single.group(1))  # This is the same as single[1], since 3.6.
pp(single[0])
pp(single[1])
pp(single)

# But it can find all matches.
multiple = re.findall(pattern, s)
pp(multiple)

# Grouping.     Symbol:     '()'
#########################################
s = "The 'side' fell off during the 'ride'. Let's 'hide'!!"
m = re.search(r"'((r|h|s)ide)'", s)
pp(m[0])
pp(m[1])
pp(m[2])
pp(m.groups())          # You can access all groups.
pp(m.groupdict())       # Why is this an empty dictionary? [See named-groups below]

# This is a character set, equivalent to the group above. [See Sets below]
single = re.search(r"(([srh])ide)", s)
pp(single[1])

multiple = re.findall(r"([hrs]ide)", s)
pp(multiple)

# Quantifiers.  Symbols: '+', '*', '?', '{}', '{,}'
#########################################
s = "4 / 3 = 1.33333333333"
single = re.search(r"(1\.3?)", s)       # Zero or one
pp(single[1])

s = "4 / 3 = 1.33333333333"  #   "4 / 3 = 1."
single = re.search(r"(1\.3*)", s)       # Zero or more (As many as possible!)
pp(single[1])

s = "4 / 3 = 1.33333333333"  #  "4 / 3 = 1."
single = re.search(r"(1\.3+)", s)       # One or more (As many as possible!)
# pp(single[1])   # CAREFUL! Can cause an error.
result = single[1] if single else "Nothing found! :-("
pp(result)

s = "4 / 3 = 1.33333333333"
single = re.search(r"(1\.3{5})", s)     # Exactly 5
pp(single[1])

s = "4 / 3 = 1.31.31.31.31.31.3"  #  "4 / 3 = 1."
single = re.search(r"((1\.3)+)", s)     # Sequence
pp(single[1])


# Sets.         Symbols:    '[]'
#########################################
# VERY IMPORTANT: characters inside the set are unordered.

s = "The students taking the exam are ee364a33, ee364b50 and ee364h07."
multiple = re.findall(r"(ee364([abc][0-9]{2}))", s)
pp(multiple)      # Note the group behavior in find all.

s = "The students taking the exam are ee364h33, ee364b50 and ee364a07."
multiple = re.findall(r"(ee364([a-h][0-9]{2}))", s)
pp(multiple)      # Note the group behavior in find all.

s = "It is 55.9 and not 31.222."
single = re.search(r"([0-9]{2}\.[0-9]{2,})", s)
pp(single[1])

# Negation in sets.                     Symbol '[^]'
s = "It is 31.222 and not 55.9."
single = re.search(r"([^0-3]{2}\.[0-9]+)", s)
pp(single[1])


# The Dot: Any single character.        Symbol '.'
# (Except \n), but can be overridden.
#########################################
s = "It is 55.9 and not 31.222."
single = re.search(r"(\d{2}\.\d{2,})", s)
pp(single)
pp(single[1])

s = "It is 55.19 and not AC.222."
single = re.search(r"(.{2}\.\d{3,})", s)
pp(single[1])

multiple = re.findall(r"(.{2}\.\d{3,})", s)
pp(multiple)

# String bounds.        Symbols:    '^', '$'
#########################################
s = "ee364j01 was a student in class and so was ee364f44"
single = re.search(r"(^.{8})", s)
pp(single)

single = re.search(r"(.{8}$)", s)
pp(single)

# NOTE: Match is simply searching from the beginning.
single = re.match(r"(.{8})", s)
pp(single[1])

# Complete string match.
s = "ee364j01 was a student in class and so was ee364f44"
single = re.search(r"(^.{8}$)", s)
pp(single[1] if single else "Nothing found!")

s = "ee364j77"
single = re.search(r"(^.{8}$)", s)
pp(single[1])

# Shorthand.
#   \d: digit      \w: letter + numbers + underscore    \b: word-boundary
#   \s: Whitespace character: space + \n + \t + \r
#   \D, \W, \S, \B: Negate their lowercase counterpart.
#########################################
s = "The students taking the exam are ee364a33, ee364b50 and ee364h07."
multiple = re.findall(r"(\w{2}\d{3}(\w\d{2}))", s)
pp(multiple)      # Note the group behavior in find all.

# Named groups.
#########################################
s = 'The support email is tech.support@purdue.edu'
match = re.search(r'(?P<user>[\w.-]+)@(?P<domain>[\w.-]+)', s)

pp(match[0])
pp(match[1])
pp(match[2])
pp(match["user"])
pp(match["domain"])
pp(match.groups())
pp(match.groupdict())   # Now the dictionary works!

# Nested groups: CAREFUL with that. It can get confusing.
s = 'The support email is tech.support@purdue.edu'
match = re.search(r'(?P<email>(?P<user>[\w.-]+)@(?P<domain>[\w.-]+))', s)
pp(match["email"])
pp(match["user"])
pp(match["domain"])
pp(match.groupdict())

# Greedy Quantifiers vs. non-greedy quantifiers
# For non-greedy, add '?' to all quantifiers.
#########################################
s = '<html><head><title>ECE364</title></head></html>'
single = re.search(r"<(.+)>", s)    # As many as possible.
pp(single[1])

single = re.search(r"<(.+?)>", s)   # As little as possible.
pp(single[1])

s = "4 / 3 = 1.33333333333"
single = re.search(r"(1\.3*)", s)       # Zero or more (As many as possible!)
pp(single[1])
single = re.search(r"(1\.3*?)", s)       # Zero or more (As little as possible!)
pp(single[1])

s = "4 / 3 = 1.33333333333"
single = re.search(r"(1\.3+)", s)       # One or more (As many as possible!)
pp(single[1])
single = re.search(r"(1\.3+?)", s)       # One or more (As little as possible!)
pp(single[1])


# Flags: Override behavior.
#########################################

s = "Second Name: Alfred\nFourth Name: Shaggy"
# print(s)

multiple = re.findall(r"(^.{6})", s)
pp(multiple)
multiple = re.findall(r"(.{6}$)", s)
pp(multiple)

# Multiline flag.
s = "Second Name: Alfred\nFourth Name: Shaggy"
multiple = re.findall(r"(^.{6})", s, re.MULTILINE)
pp(multiple)
multiple = re.findall(r"(.{6}$)", s, re.MULTILINE)
pp(multiple)

# Ignore case.
s = "EE364X03 and ee364x01 are students."
single = re.search(r"ee364x\d\d", s)
pp(single)
single = re.search(r"EE364X\d\d", s, re.IGNORECASE)
pp(single)

multiple = re.findall(r"ee364x\d\d", s)
pp(multiple)
multiple = re.findall(r"EE364X\d\d", s, re.IGNORECASE)
pp(multiple)

# DOTALL
s = "Alfred:\nIt cannot be!"
# print(s)

single = re.search(r"(.{13})", s)
pp(single)

single = re.search(r"(.{13})", s, re.DOTALL)
pp(single)

