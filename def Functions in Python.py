                              #Functions in Python
"""
Python allows us to divide a large program into the basic building blocks known as a function.
function is a group of related statements that performs a specific task.
A function is a reusable block of code which only runs when it is called. 
A function can return data as a result.

>>Two Types of Function :
        1. User-defined Function: We can create our own function based on our requirements.
        2. Standard Library Function: These are built-in function in python that are available to use.
        
Syntax:
   def function_name ( Parameter list ) :
        // function block

Return Syntax:
     return expression

Function Types :
No Return Type With Argument Function
No Return Type Without Argument Function
Return Type Without Argument Function
Return Type With Argument Function       
"""
def welcome():
    print("Welcome To Maatram Foundation")

welcome()
print("-------------------------------------------------------")

# No Return Type Without Argument Function in Python

def add():
    a=int(input("Enter The Value of A : "))
    b=int(input("Enter The Value of B : "))
    c=a+b
    print("Total ",c)

add()

print("-------------------------------------------------------")

# No Return Type With Argument Function in Python

def sub(a, b):
    c = a - b
    print("Difference : ", c)

sub(20, 2)
print("-------------------------------------------------------")


# Return Type Without Argument Function in Python

def mul():
    a = int(input("Enter The Value of A : "))
    b = int(input("Enter The Value of B : "))
    c = a * b
    return c

x=mul()
print("Mul ",x)
print("-------------------------------------------------------")

# Return Type With Argument Function in Python
def div(a, b):
    c = a / b
    return c

x = div(25, 2)
print("Division ", x)
print("-------------------------------------------------------")

# Arbitrary Arguments Function in Python (*)
def class_10(*students):
    print(students)
    for user in students:
        print(user)

class_10("Mani", "Vasu", "Chinna", "Susi")
print("-------------------------------------------------------")

# Keyword Arguments Function in Python
def message(name, age):
    print(name, " age is ", age)

message(age=25, name="Mani")

print("-------------------------------------------------------")

# Arbitrary Keyword Arguments in Python(**)
def bioData(**data):
    print(data)

bioData(name="Ram Kumar", age=25, gender="Male")

print("-------------------------------------------------------")

# Default Parameter Function in Python
def user(name, city="Salem"):
    print(name, " is from ", city)

user("Ram", "Namakkal")
user("Sam")

print("-------------------------------------------------------")

# Passing a List as an Argument in Function Python
def total(marks):
    return sum(marks)

print("Total : ",total([55, 75, 80, 95, 47]))

print("-------------------------------------------------------")
#>> recursive function

# 1 * 2 * 3 * 4 * 5=120
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))

print("Factorial : ", factorial(5))

"""
factorial(5)
5*factorial(4)
5*4*factorial(3)
5*4*3*factorial(2)
5*4*3*2*factorial(1)
5*4*3*2*1
120
"""
print("---------------lambda---------------------------")
c = lambda a: a + 50
print(c(5))

c = lambda a, b: a * b
print(c(10, 25))