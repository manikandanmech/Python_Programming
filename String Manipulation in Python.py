#String Manipulation in Python
"""
String manipulation is a process of manipulating the string, such as slicing, parsing, analyzing, etc.
String slicing in python programming is all about fetching a substring from a given string by slicing it from a start to end index.

 Syntax :
   s [ start : end ]
   s [ start : ]
   s [ : end ]
   s [ :: ]
"""
# String Manipulation
'''
 S  a  m  p  l  e
 0  1  2  3  4  5
-6 -5 -4 -3 -2 -1
'''

s = "Technology"
print(s)
print(s[0:2])
print(s[:5])
print(s[1:])
print(s[-1])
print(s[-2:-1])
print(s[:-1])
print(s[::-1]) #reverse