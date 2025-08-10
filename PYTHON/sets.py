'''
A Set in Python is used to store a collection of items with the following properties.

No duplicate elements. If try to insert the same item again, it overwrites previous one.
An unordered collection. When we access all items, they are accessed without any specific order and we cannot access items using indexes as we do in lists.
Internally use hashing that makes set efficient for search, insert and delete operations. It gives a major advantage over a list for problems with these operations.
Mutable, meaning we can add or remove elements after their creation, the individual elements within the set cannot be changed directly.
Example of Python Sets

'''

s = {10, 50, 20}
print(s)
print(type(s))


'''
Type Casting with Python Set method
The Python set() method is used for type casting.
'''
# typecasting list to set
s = set(["a", "b", "c"])
print(s)

# Adding element to the set
s.add("d")
print(s)


'''
Check unique and  Immutable with Python Set
Python sets cannot have duplicate values. 
While you cannot modify the individual elements directly, you can still add or remove elements from the set.
'''

# Python program to demonstrate that
# a set cannot have duplicate values 
# and we cannot change its items

# a set cannot have duplicate values
s = {"Geeks", "for", "Geeks"}
print(s)

# values of a set cannot be changed
# s[1] = "Hello"
# print(s)


'''
Heterogeneous Element with Python Set
Python sets can store heterogeneous elements in it, i.e., 
a set can store a mixture of string, integer, boolean, etc datatypes.

'''
# Python example demonstrate that a set
# can store heterogeneous elements
s = {"Geeks", "for", 10, 52.7, True}
print(s)


'''
Python Frozen Sets
Frozen sets in Python are immutable objects that only support methods and operators that produce a result without affecting the frozen set or sets to which they are applied. It can be done with frozenset() method in Python.

While elements of a set can be modified at any time, elements of the frozen set remain the same after creation. 

If no parameters are passed, it returns an empty frozenset.

'''

# Python program to demonstrate differences
# between normal and frozen set

# Same as {"a", "b","c"}
s = set(["a", "b","c"])

print("Normal Set")
print(s)

# A frozen set
fs = frozenset(["e", "f", "g"])

print("\nFrozen Set")
print(fs)

# Uncommenting below line would cause error as
# we are trying to add element to a frozen set
# 

# fs.add("h")

'''
internal working of Set
This is based on a data structure known as a hash table.  
If Multiple values are present at the same index position, then the value is appended to that index position, to form a Linked List.

In, Python Sets are implemented using a dictionary with dummy variables, where key beings the members set with greater optimizations to the time complexity.

'''
'''
Methods for Sets
Adding elements to Python Sets
Insertion in the set is done through the set.add() function, where an appropriate record value is created to store in the hash table. 
Same as checking for an item, i.e., O(1) on average. However, in worst case it can become O(n).
'''
# A Python program to
# demonstrate adding elements
# in a set

# Creating a Set
people = {"Jay", "Idrish", "Archi"}

print("People:", end = " ")
print(people)

# This will add Daxit
# in the set
people.add("Daxit")

# Adding elements to the
# set using iterator
for i in range(1, 6):
    people.add(i)

print("\nSet after adding element:", end = " ")
print(people)


'''
Union operation on Python Sets
Two sets can be merged using union() function or | operator. Both Hash Table values are accessed and traversed with merge operation perform on them to combine the elements, at the same time duplicates are removed. The Time Complexity of this is O(len(s1) + len(s2)) where s1 and s2 are two sets whose union needs to be done.
'''

# Python Program to
# demonstrate union of
# two sets

people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
dracula = {"Deepanshu", "Raju"}

# Union using union()
# function
population = people.union(vampires)

print("Union using union() function")
print(population)

# Union using "|"
# operator
population = people|dracula

print("\nUnion using '|' operator")
print(population)


'''
Intersection operation on Python Sets
This can be done through intersection() or & operator. Common Elements are selected. 
They are similar to iteration over the Hash lists and combining the same values on both the Table. Time Complexity of this is O(min(len(s1), len(s2)) where s1 and s2 are two sets whose union needs to be done.

'''

# Python program to
# demonstrate intersection
# of two sets

set1 = set()
set2 = set()

for i in range(5):
    set1.add(i)

for i in range(3,9):
    set2.add(i)

# Intersection using
# intersection() function
set3 = set1.intersection(set2)

print("Intersection using intersection() function")
print(set3)

# Intersection using
# "&" operator
set3 = set1 & set2

print("\nIntersection using '&' operator")
print(set3)

'''
Finding Differences of Sets in Python
To find differences between sets. Similar to finding differences in the linked list. 
This is done through difference() or – operator. Time complexity of finding difference s1 – s2 is O(len(s1))

'''

# Python program to
# demonstrate difference
# of two sets

set1 = set()
set2 = set()

for i in range(5):
    set1.add(i)

for i in range(3,9):
    set2.add(i)

# Difference of two sets
# using difference() function
set3 = set1.difference(set2)

print(" Difference of two sets using difference() function")
print(set3)

# Difference of two sets
# using '-' operator
set3 = set1 - set2

print("\nDifference of two sets using '-' operator")
print(set3)


'''
Clearing Python Sets
Set Clear() method empties the whole set inplace.

'''

# Python program to
# demonstrate clearing
# of set

set1 = {1,2,3,4,5,6}

print("Initial set")
print(set1)

# This method will remove
# all the elements of the set
set1.clear()

print("\nSet after using clear() function")
print(set1)