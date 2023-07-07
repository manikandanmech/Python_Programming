#if-else Statement in Python
"""
The if-else statement is used to execute both the true part and the false part of a given condition.
If the condition is true, the if block code is executed and if the condition is false, the else block code is executed.

  Syntax :
        if ( condition ) :
               // body of the statements will execute if the condition is true
        else :
               // body of the statements will execute if the condition is false
"""
# if-else Statement in Python
name = input("Enter Your Name : ")
age = int(input("Enter Your Age : "))
if age >= 18:
    print(name, " age is ", age, " Eligible for Vote.")
else:
    print(name, " age is ", age, " Not Eligible for Vote.")