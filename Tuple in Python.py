                          #Tuple in Python
"""
 Tuple are used to store multiple items in a single variable.To separate two items, you use a comma ( , ).
 A tuple is like a list except that it uses parentheses ( ) . 
 Once you define a tuple, you can access an individual element by its index.
 A tuple is a collection of objects which ordered and immutable, you cannot change its elements.
 Tuples are sequences, just like lists.


"""
# Tuple in Python
# Immutable
# Surrounded by Round Brackets (1,1,5)
a = (2, 8.5, True, "mani")
print(a)
print(type(a))
print(a[1])
print(a[-1])
print(a[0:2])
b = list(a)
print(b)
b.append("raj")
print(b)
print(type(b))
a = tuple(b)
print(a)
print(type(a))

print("-----------------------------------------")

for i in a:
    print(i)

print("-----------------------------------------")

if "Raj" in a:
    print("Raj is Found")
else:
    print("Not Found")
print(len(a))

print("-----------------------------------------")
a = (1,)
print(type(a))
del a
a = (1, 2, 7, 4)
b = (5, 6, 7, 8)
c = a + b
print(c)
print(c.count(7))
print("-----------------------------------------")
a = (1, 2, 7, 4)
b = (5, 6, 7, 8)
c = (a, b)
print(c)
print(c[0])
print(c[1])
print(c[0][1])
print("-----------------------------------------")

x = ('santhi',) * 8
print(x)

print("-----------------------------------------")

a = (1, 2, 7, 4)
b = (5, 6, 7, 8)
print(min(a))
print(max(a))

print("-----------------------------------------")