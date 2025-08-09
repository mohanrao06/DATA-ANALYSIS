"""
In Python, a list is a built-in dynamic sized array (automatically grows and shrinks). We can store all types of items (including another list) in a list. A list may contain mixed type of items, this is possible because a list mainly stores references at contiguous locations and actual items maybe stored at different locations.

--> List can contain duplicate items.
--> List in Python are Mutable. Hence, we can modify, replace or delete the items.
--> List are ordered. It maintain the order of elements based on how they are added.
---> Accessing items in List can be done directly using their position (index), starting from 0.

"""
# Creating a Python list with different data types
a = [10, 20, "GfG", 40, True]
print(a)

# Accessing elements using indexing
print(a[0])  # 10
print(a[1])  # 20
print(a[2])  # "GfG"
print(a[3])  # 40
print(a[4])  # True

# Checking types of elements
print(type(a[2]))  # str
print(type(a[4]))  # bool


# Creating a List
# --> Using Square Brackets
# List of integers
a = [1, 2, 3, 4, 5]

# List of strings
b = ['apple', 'banana', 'cherry']

# Mixed data types
c = [1, 'hello', 3.14, True]

print(a)
print(b)
print(c)

# --> Using list() Constructor
# From a tuple
a = list((1, 2, 3, 'apple', 4.5))  
print(a)

'''
Accessing List Elements
Elements in a list can be accessed using indexing. Python indexes start at 0, so a[0] will access the first element, while negative indexing allows us to access elements from the end of the list. Like index -1 represents the last elements of list.

'''
a = [10, 20, 30, 40, 50]

# Access first element
print(a[0])    

# Access last element
print(a[-1])


'''
Adding Elements into List
We can add elements to a list using the following methods:

--> append(): Adds an element at the end of the list.
--> extend(): Adds multiple elements to the end of the list.
--> insert(): Adds an element at a specific position.

'''
# Initialize an empty list
a = []

# Adding 10 to end of list
a.append(10)  
print("After append(10):", a)  

# Inserting 5 at index 0
a.insert(0, 5)
print("After insert(0, 5):", a) 

# Adding multiple elements  [15, 20, 25] at the end
a.extend([15, 20, 25])  
print("After extend([15, 20, 25]):", a)


# We can change the value of an element by accessing it using its index.
a = [10, 20, 30, 40, 50]

# Change the second element
a[1] = 25 
print(a)


'''
Removing Elements from List
We can remove elements from a list using:

--> remove(): Removes the first occurrence of an element.
--> pop(): Removes the element at a specific index or the last element if no index is specified.
--> del statement: Deletes an element at a specified index.

'''
a = [10, 20, 30, 40, 50]

# Removes the first occurrence of 30
a.remove(30)  
print("After remove(30):", a)

# Removes the element at index 1 (20)
popped_val = a.pop(1)  
print("Popped element:", popped_val)
print("After pop(1):", a) 

# Deletes the first element (10)
del a[0]  
print("After del a[0]:", a)


'''
List Comprehension in Python
List comprehension is a concise way to create lists using a single line of code. 
It is useful for applying an operation or filter to items in an iterable, such as a list or range.


'''
# Create a list of squares from 1 to 5
squares = [x**2 for x in range(1, 6)]
print(squares)