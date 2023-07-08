                     #List in Python
"""
Lists are used to store multiple items in a single variable.
To separate two items, you use a comma ( , ) . 
List uses the square brackets [ ].
 #Lists are one of 4 built-in data types in Python used to store collections of data, 
the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Sequence Type
Element of the list can access by index
They are mutable

>>various built-in functions and methods that can be used with lists in Python.

 clear() method to remove all elements from a list, the copy() method to create a copy of a list.
 count() method to count the number of occurrences of an element in a list.
 index() method to find the index of an element in a listlen() function to find the length of a list.
 max() and min() functions to find the maximum and minimum element in a list.
 pop() method to remove an element from a list using an index.
 remove() method to remove an element from a list using its value.
 append() method to add elements to a list.
 extend() method to add elements from another list.
 insert() method to insert an element at a specific index in a list.
 range() function to create a list of numbers.
 list() function to convert a string to a list.
 sort() method to sort the elements of a list in ascending or descending order.
 
"""
# List in Python
a = [1, 2, 3, 4, 5]
print(a)
print(type(a))
a[0] = 50
print(a)
print("-----------------------------------------------------")
print("Slicing")
print(a[1])
print(a[-1])
print(a[0:3])
print(a[2:])
print(a[:3])
print("-----------------------------------------------------")
a = [1, True, 'mani', 2.5, [1, 2, 3, 4]]
print(a)
print(type(a))
print(a[0], " type is ", type(a[0]))
print(a[1], " type is ", type(a[1]))
print(a[2], " type is ", type(a[2]))
print(a[3], " type is ", type(a[3]))
print(a[4], " type is ", type(a[4]))
print(a[4][1])
print("-------------------------------------------------")
a = [5,15, 25, 35, 45]
print(a)
a.clear()
print(a)
a = [5,15, 25, 35, 45]
b = a.copy()
print(b)
a = [10, 25, 35, 45, 25, 4, 25]
print(a.count(25))
print(a.index(25))
print(len(a))
print(max(a))
print(min(a))
print(a)
a.pop(0)  # remove Element using index
print(a)
a = [10, 25, 35, 45, 25, 4, 25]
a.remove(25)  # Values
print(a)
print("---------------------------------------------------")
names = ["Mani"]
print(names)
names.append("Sugu")
names.append("Dinesh")
names.append("SanjayKumar")
print(names)
name2 = ["Srikanth", "Hari"]
names.extend(name2)
print(names)
names.insert(0,"Bala") #(index ,value)
print(names)
print("----------------------------------------------------------------")
print(list(range(5)))
print(list("MaatramFoundation"))
a=[10,50,100,25,85]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a=["Orange","Apple","Zebra"]
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a=["Orange","Apple","Zebra"]
a.sort(key=len)
print(a)
