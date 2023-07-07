#elif Statement in Python
"""
The elif condition is used to multiple conditional expressions after the if condition or between the if and else conditions.
The elif block is executed if the specified condition evaluates to True.

  Syntax :
        if ( condition 1 ) :
               // body of the statements will execute if the condition1 is true
        elif ( condition 2 ) :
               // body of the statements will execute if the condition2 is true
        .
        .
        else :
               // body of the statements will execute if the condition1 is false condition2 is False
"""

# elif Statement in Python
"""
0       Not Fine
1-5     1
5-10    5
10-30   10
>30     Membership is Cancel
"""
days = int(input("Enter The Days : "))
if days == 0:
    print("Good No Fine")
elif days >= 1 and days <= 5:
    print("Fine Amount : ", days * 1)
elif days > 5 and days <= 10:
    print("Fine Amount : ", days * 5)
elif days > 10 and days <= 30:
    print("Fine Amount : ", days * 10)
else:
    print("Membership is Cancel")