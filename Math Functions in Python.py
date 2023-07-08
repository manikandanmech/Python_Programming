                   #Math Functions in Python
"""
The Python Math Library provides us access to some common math functions and constants in Python.
The math module is used to access mathematical functions in the Python.
Some of the most popular mathematical functions are defined in the math module.
All methods of this functions are used for integer or real type objects, not for complex numbers.

sqrt ( ) => The square root of the argument
ceil ( ) => Rounds float value up to an integer value
floor ( ) => Rounds float value down to an integer value
fabs ( ) => Value is return to the absolute ( positive ) value
pow ( ) => Returns the value of the first parameter raised to the second parameter
factorial ( ) => Returns the factorial of a number
"""
import math
print(math.sqrt(4))
print(math.ceil(2.55555))
print(math.floor(2.55555))
print(math.factorial(5))  # 5! => 1*2*3*4*5=120
print(math.fabs(-5))
print(math.pow(2, 3))  # 2^3
print(math.log2(2))
print(math.log10(2))
print(math.pi)
print(math.e)