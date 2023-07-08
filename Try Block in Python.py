                       #Try Block in Python
"""
The try block in Python is used to enclose code that might raise an exception. If an exception is raised within the try block, it is caught by the associated except block, which can then handle the exception as desired. The basic structure of a try-except block in Python is as follows:

Syntax:
   try:
              # code that might raise an exception
   except ExceptionType1:
              # code to handle ExceptionType1
   except ExceptionType2:
              # code to handle ExceptionType2
   except:
              # code to handle any other exception
   else:
              # code to run if no exception was raised
   finally:
              # code that will always be executed, regardless of whether an exception was raised or not
The else block is optional, and is only executed if no exceptions were raised within the try block. The finally block is also optional, but is always executed after the try block, regardless of whether an exception was raised or not.

"""

# try block in Python
try:
    a = 10 / 0
except Exception as e:
    print(e)
print("----------------------------------------------------------")

# Try Else
try:
    a = 10 / 25
except Exception as e:
    print(e)
else:
    print("A Value : ",a)
print("----------------------------------------------------------")
# Try else finally
try:
    a = 10 / 0
except Exception as e:
    print(e)
else:
    print("A Value : ",a)

finally:
    print("Thank You")


# Type of Exceptions in Python
print(dir(locals()['__builtins__']))
print(len(dir(locals()['__builtins__'])))

# Type of Exceptions in Python =>> 153
"""
 ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError',
 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',etc..]
"""

# Nameerror Exception

try:
    print(a)
except NameError as e:
    print("A is not Defined")

print("----------------------------------------------------------")
try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("denominator cant be zero")
print("----------------------------------------------------------")
try:
    a = int("Joes")
except ValueError as e:
    print("Please Enter Numbers only")
print("----------------------------------------------------------")
try:
    a = [10, 20, 30, 40]
    print(a[10])
except IndexError as e:
    print("Invalid Index")
print("----------------------------------------------------------")

try:
    f = open("test.txt") #create test text file ,than run it.
except FileNotFoundError:
    print("File Not Found")
else:
    print(f.read())
print("----------------------------------------------------------")

try:
    a=10/20
    print(a)
    b=[10,20,30,40]
    print(b[0])
    a=open('manic.txt')
except ZeroDivisionError:
    print("denominator cant be zero")
except IndexError:
    print("Invalid Index")
except Exception as e:
    print(e)

