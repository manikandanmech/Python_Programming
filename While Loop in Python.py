                     #While Loop in Python
""" The while loop is repeats a statement or block while its controlling expression is true.
The condition can be any Boolean expression.

When condition becomes false, control passes to the next line of code immediately following the loop.

If the condition to true, the code inside the while loop is executed.
The condition is evaluated again.
This process continues until the condition is false.
When the condition to false, the loop stops.

  Syntax:
      while ( Condition ) :
          // body of statement
 
 """
# While Loop
i = 1
while i <= 10:
    print(i)
    i += 1
print("--------------------")
print("Even No : ")
n = 20
i = 2
while i <= 20:
    print(i)
    i += 2