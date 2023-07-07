# String Functions in Python
"""
Python has several built-in functions associated with the string data type.
These functions let us easily modify and manipulate strings.
Creating Strings is the simplest and easy to use in Python.
To create a string in Python, we simply enclose a text in single as well as double-quotes.
----------------------------------------------------------------------------------------------
type() => The returns the type of the object.
upper() => All the characters in a given string are uppers case.
lower() => All the characters in a given string are lower case.
capitalize() => The first character is the upper case
The title() => The first character in every word of the string is an upper case.
count() => Finds the number of times a specified value in the given string.
find() => Finds the first occurrence of the specified value.
replace() => Replaces a specified phrase with another specified phrase.
isalnum() => Checks whether all the characters in a given string is alphanumeric or not
isalpha() => returns True if all the characters in the string are alphabets
islower() => Checks if all characters in the string are lowercase
isupper() => Checks if all characters in the string are uppercase
strip() => The used to trim whitespaces from the string object
---------------------------------------------------------------------------------------------------
"""

# String And String Function
s = "welcome to maatram foundation"
print(s)
print(type(s))
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print("-------------------------------------------")
print(s.count("t"))
print(s.endswith("on"))
print(s.find("a"))
print(s.find("a",18))
print(s.replace("o", '0'))
print("-------------------------------------------")
a = "mani1234"
print("Is Upper : ", a.isupper())
print("Is Lower : ", a.islower())
print("Is Alpha Numeric : ", a.isalnum())
print("Is Alpha : ", a.isalpha())
print("-------------------------------------------")
s = "sujith sir\nis\nfounder"
print(s)
print(s.splitlines())
print(s.splitlines(True))
print("-------------------------------------------")
a = "sindhu mam was inspires me"
print(a.split(" "))
a = "sindhu,mam,was,inspires,me"
print(a.split(","))
print("-------------------------------------------")
s="    Joes     "
print(len(s))
print(len(s.strip()))
print(len(s.lstrip())) #left intex
print(len(s.rstrip())) #right intex
print("-------------------------------------------")
s='11-02-2003'
print(s.partition('-'))
print("-------------------------------------------")