#Type Casting in Python
"""
   In Python, type casting is the process of converting one data type to another.
Python is a dynamically-typed language, which means that the data type of a variable can change based on the value assigned to it.
However, sometimes you may need to convert a variable from one data type to another.

There are several built-in functions in Python that can be used for type casting:
int(): Converts a value to an integer.
float(): Converts a value to a floating-point number.
str(): Converts a value to a string.
bool(): Converts a value to a Boolean (True or False).

"""

a = 40.0
print(a)
print(type(a))
b = int(a)
print(b)
print(type(b))

#int()
#float()
#str()

a = int(input("Enter The Value of A : "))
b = int(input("Enter The Value of B : "))
c = a + b
print("Total : " + str(c))