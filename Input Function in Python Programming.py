#Input Function in Python Programming
"""
The input ( ) function helps to enter data at run time by the user and returns it as a string.
 This function prompts the user for an input from the keyboard.

The output function print ( ) is used to display the result of the program on the screen after execution.

>> Use the int ( ) Function to Check if the Input Is an Integer in Python.
The int ( ) function can convert a given string integer value to an integer type.
>> Use the float ( ) Function to Check if the Input Is an decimal number in Python.
The float ( ) function can convert a given string decimal number value to an float type.
--------------------------------------------------------------------------------------------------------------
"""
#Getting input in Python

#Getting String input Statement
name=input("Enter Name : ")
print(type(name))
print(name)

#Getting Integer input Statement
a=int(input("Enter The Value of A : "))
b=int(input("Enter The Value of B : "))
c=a+b
print(c)
print(type(a))

#Getting Float input Statement
a=float(input("Enter The Value of A : "))
b=float(input("Enter The Value of B : "))
c=a+b
print(c)
print(type(a))
#-----------------------------------------------------------------------------------------------------------------------

#Multiple Values in Single Line
name1,name2,name3=input("Enter 3 Names : ").split()
print("Name 1 : ",name1)
print("Name 2 : ",name2)
print("Name 3 : ",name3)

name1,name2,name3=input("Enter 3 Names : ").split(',')
print("Name 1 : ",name1)
print("Name 2 : ",name2)
print("Name 3 : ",name3)

"""
The input() function is used to take the input, and the split() function is used to separate the names by a space,comma and store them in the respective variables"""
#-----------------------------------------------------------------------------------------------------------------------

#Multiple Line String Input in Python
a="""
What could be better? 
You cannot help bring change outside if you cannot change your own vicinity.
-Sujith Kumar
"""
print(type(a))
print(a)

#-----------------------------------------------------------------------------------------------------------------------
para=[]
print("Enter a Para : ")
while True:
  line=input()
  if line:
    para.append(line)
  else:
    break
print(para)
output='\n'.join(para)
print(output)