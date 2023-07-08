          #Identity Operators in Python
"""
*Identity operators are used to compare the objects, not if they are equal,
but if they are actually the same object, with the same memory location. 

*Two identity operators is and is not.

*The is operators test If two operands have the same identity, it returns True. Otherwise, it returns False.
"""

"""
is
is not
"""
a = [1, 2]
b = [1, 2]
c = a
print(id(a))
print(id(c))
print(id(b))
print(a is c)
print(a is b)
print(a==b)
print(a is not c)
print(a is not b)
print(a!=b)
