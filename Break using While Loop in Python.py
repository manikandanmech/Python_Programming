           #Break using While Loop in Python
"""The break statements are your way of asking the loop to stop and execute the next statement. 
When a break statement is encountered inside a loop, the loop is immediately terminated and the program control resumes at the next statement following the loop"""

# Break Statement
i = 1
while i <= 20:
  if i==11:
    break
  print(i)
  i += 1