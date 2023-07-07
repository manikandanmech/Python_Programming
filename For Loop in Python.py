#For Loop in Python
"""
The for loop is used to repeat a specific block of code which you want to repeat a fixed number of times. The for loop is a control flow statement that is used to repeatedly execute a group of statements as long as the condition is satisfied.

Syntax:
   for variable_name in sequence :
              body of loop
"""

# For Loop in Python
for i in range(0, 21, 2):
    print(i)

for i in range(5):
    a=int(input("Enter a No : "))
    b=int(input("Enter a No : "))
    print(a+b)