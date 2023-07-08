                                                    #Dictionary in Python
"""
A Python dictionary is a collection of key-value pairs where each key is associated with a value.
dictionary are used to store multiple items in a single variable.To separate two items, you use a comma ( , ).
A dictionary is like a list except that it uses parentheses { key : value } .

They are Immutable
A set doesn’t allow duplicate elements
The key cannot be changed

The keys() method returns the keys of the dictionary, and the values() method returns the values of the dictionary.
The items() method returns a view of the dictionary's key-value pairs.
For loops are used to iterate over the keys, values and items of the dictionary .
The dictionary values can be updated using the update() method and the [] operator.
The pop() method is used to remove the key-value pair with the given key.
The clear() method is used to remove all key-value pairs from the dictionary.
"""
user = {
    "name": "Mani",
    "age": 20,
    "isMarried":False
}

print(user)
print(type(user))
print(user["name"])
print(user.get('age'))
print(user.keys())
print(user.values())
print(user.items())

print("----------------------------------------------------------")

for x in user:
    print(x," ",user[x])

print("------------------valuse--------------------------------")
for x in user.values():
    print(x)

print("------------------Keys------------------------------------")

for x in user.keys():
    print(x)

print("------------------items---------------------------------")

for x,y in user.items():
    print(x,y)

print("----------------------------------------------------------")
if "age" in user:
    print("Present")

if "gender" in user:
    print("Not Present")
#else:
    #//

print("--------------------Changing Values--------------------------------------")

user.update({"gender":"male"})
print(user)
user["age"]=35
print(user)
user.pop("age")
print(user)
user.clear()
print(user)

print("-------------------Nested Dictionary--------------------------------------")
users={
    "user1": {
        "name": "Ram",
        "age": 25,
        "isMarried": True
    },
"user2": {
        "name": "SAm",
        "age": 35,
        "isMarried": False
    }
}
print(users)

for user in users:
    print(user["name"])