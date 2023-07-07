          #Bitwise Operators in Python
"""
In Python, bitwise operators are used to perform bitwise calculations on integers. The integers are first converted into binary and then operations are performed on bit by bit, hence the name bitwise operators. Then the result is returned in decimal format. Bitwise AND operator: Returns 1 if both the bits are 1 else 0

-------------------------------
Operator	 |     Description
-------------------------------
&         	     Bitwise AND
|	             Bitwise OR
^	             Bitwise XOR
~	             Bitwise NOT
<<	             Left shift
>>	             Right shift   
-------------------------------  """

# Bitwise Operators
"""
& 	AND
|	OR
^	XOR
~ 	NOT
<<	Zero fill left shift
>>	Signed right shift
"""
a = 20
b = 40
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 2)
print(a >> 2)