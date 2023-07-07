#Nested If Statement in Python

"""
Nested If Statement means to place one If inside another If Statement. Nested ifs are very common in programming.
when you nest ifs, the main thing to remember is that an else statement always refers to the nearest if statement,
that is within the same block as the else and that is not already associated with an else.

  Syntax:
    if ( Expression 1 ) :
        // Executes when the Expression 1 is true
           if ( Expression 2 ) :
             // Executes when the Expression 2 is true
"""

# Nested If Statement in Python
"""
3 Marks as Input
Total
Average
Result
If Pass Grade
    90-100 A
    80-89 B
    70-79 C
    else D
"""
m1 = int(input("Enter Mark-1  : "))
m2 = int(input("Enter Mark-2  : "))
m3 = int(input("Enter Mark-3  : "))
total = m1 + m2 + m3
average = total / 3
print("Total  : ", total)
print("Average  : ", average)
if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("Result  : Pass")
    if average >= 90 and average <= 100:
        print("Grade : A")
    elif average >= 80 and average <= 89:
        print("Grade : B")
    elif average >= 70 and average <= 79:
        print("Grade : C")
    else:
        print("Grade : D")
else:
    print("Result  : Fail")
    print("Grade   : No Grade")