                    #Set in Python
"""
Set are used to store multiple items in a single variable. To separate two items, you use a comma ( , ) . A set is like a list except that it uses parentheses { } 
Set are unordered
A set doesn’t allow duplicate elements
Set cannot be changed

The new element is added to the set using the "add" method.
The elements are added to the names set using the "update" method.
The "remove" and "discard" methods are used to remove elements from the set.
The "pop" method is used to remove an arbitrary element from the set.
The "clear" method is used to remove all elements from the set and "del" is used to delete the entire set.

>> set operations such as union, intersection, symmetric difference and set comparison methods such as isdisjoint, issubset, and issuperset.

The "union" method is used to combine the elements of two sets and the "update" method updates the set with the elements from another set.
The "intersection" method returns the common elements in both sets and the "intersection_update" method updates the set with the common elements.
The "symmetric_difference" method returns the elements that are unique to each set and the "symmetric_difference_update" method updates the set with the unique elements.
The "isdisjoint" method returns True if two sets have no common elements and False otherwise. The "issubset" method returns True if a set is a subset of another set and False otherwise.
The "issuperset" method returns True if a set is a superset of another set and False otherwise.

"""

names={'Mani','Raj','Geetha'}
print(names)
print(type(names))
print("-----------------------------------------------------------------------")

# Access Values Using For loop
for name in names:
    print(name)
print("-----------------------------------------------------------------------")

# Adding New Element
names.add('Sneka')
print(names)
# Update Another Set of Data
a={'Sindhu',',Monika','Arul'}
names.update(a)
print(names)
names.remove('Mani')
print(names)
names.discard('Suresh')
print(names)
names.pop()
print(names)
names.clear()
print(names)
del names
print("-----------------------------------------------------------------------")
names={'Raj', ',Monika', 'Geetha', 'Arul', 'Sindhu'}
print(names)

print("-----------------------------------------------------------------------")

a = {1, 2, 3, 4}
b = {'a', 'b', 'c', 'd'}
c=a.union(b)
print(c)
a.update(b)
print(a)

print("-----------------------------------------------------------------------")
a = {1, 2, 3, 4, 5}
b = {5, 6, 7, 8, 9}
c=a.intersection(b)
print(c)
a.intersection_update(b)
print(a)
c=a.symmetric_difference(b)
print(c)
a.symmetric_difference_update(b)
print(a)

print("-----------------------------------------------------------------------")

a = {5,6,7}
b = {5, 6, 7}
c=a.isdisjoint(b)
print(c)
c=a.issubset(b)
print(c)
c=a.issuperset(b)
print(c)

print("-----------------------------------------------------------------------")
