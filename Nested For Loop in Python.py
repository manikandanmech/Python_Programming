#Nested For Loop in Python
"""
The nested loop refers to a loop within a loop, an inner loop within the body of an outer one.
Nested loops are useful when for each pass through the outer loop, you need to repeat some action on the elements in the outer loop.
The nested loop is a one iteration of the outer loop is first executed, after which the inner loop is executed.
The execution of the inner loop continues till the condition described in the inner loop is satisfied.


Syntax:
   // outer for loop
   for variable_name in sequence :
             // inner for loop
              for variable_name in sequence :
                    // body of loop

"""
# Nested For Loop
"""
*
**
***
****
*****

*****
****
***
**
*

ABCDE
ABCDE
ABCDE
ABCDE
ABCDE

A-Z => 65-90
a-z=> 97-122

"""

for i in range(6):
    for j in range(i):
        print("*",end="")
    print("")
print("--------------------------------")

for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print("")
print("---------------------------------")

for i in range(65,70,1):
    for j in range(65,70,1):
        print(chr(j),end="")
    print("")
print("--------------------------------")