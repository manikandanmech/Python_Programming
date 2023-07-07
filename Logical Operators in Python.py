#Logical Operators in Python
"""
   Logical operators are used to combine multiple conditions in a single expression in Python.
The three logical operators in Python are and, or, and not.

and:
   This operator returns True if both the conditions on either side of the operator are True, otherwise it returns False.
or:
  This operator returns True if either of the conditions on either side of the operator is True, otherwise it returns False.
not:
  This operator inverts the truth value of a single condition.
  If a condition is True, the not operator will make it False and vice versa.    """

# Logical Operators in Python
"""
and
or
not

"""
a = 25
print(a >= 10 and a <= 20)
print(a >= 10 or a <= 20)
print(not(a >=  10 and a <= 20))