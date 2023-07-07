       #Continue using While Loop in Python
"""
The continue statement instructs a loop to continue to the next iteration.
The continue statement is used to skip the remaining statements of the current loop and go to the next iteration.
"""
#Print Odd Numbers using While Loop in Python

#>>>> Continue Statement
i = 1
while i <= 20:
  if i % 2 == 0:
    i = i + 1
    continue;
  print(i)
  i += 1