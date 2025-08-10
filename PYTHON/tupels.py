
"""
A tuple in Python is an immutable ordered collection of elements.

--> Tuples are similar to lists, but unlike lists, they cannot be changed after their creation (i.e., they are immutable).
--> Tuples can hold elements of different data types.
--> The main characteristics of tuples are being ordered , heterogeneous and immutable.

"""

"""
Creating a Tuple
A tuple is created by placing all the items inside parentheses (), separated by commas. 
A tuple can have any number of items and they can be of different data types.

"""
tup = ()
print(tup)

# Using String
tup = ('Geeks', 'For')
print(tup)

# Using List
li = [1, 2, 4, 5, 6]
print(tuple(li))

# Using Built-in Function
tup = tuple('Geeks')
print(tup)

'''
Creating a Tuple with Mixed Datatypes.
Tuples can contain elements of various data types, including other tuples, lists, dictionaries and even functions.
'''

tup = (5, 'Welcome', 7, 'Geeks')
print(tup)

# Creating a Tuple with nested tuples
tup1 = (0, 1, 2, 3)
tup2 = ('python', 'geek')
tup3 = (tup1, tup2)
print(tup3)

# Creating a Tuple with repetition
tup1 = ('Geeks',) * 3
print(tup1)

# Creating a Tuple with the use of loop
tup = ('Geeks')
n = 5
for i in range(int(n)):
    tup = (tup,)
    print(tup)

'''
Python Tuple Basic Operations
Below are the Python tuple operations.

--> Accessing of Python Tuples
--> Concatenation of Tuples
--> Slicing of Tuple
--> Deleting a Tuple
Accessing of Tuples
We can access the elements of a tuple by using indexing and slicing, similar to how we access elements in a list. 
Indexing starts at 0 for the first element and goes up to n-1, where n is the number of elements in the tuple. 
Negative indexing starts from -1 for the last element and goes backward.

'''
# Accessing Tuple with Indexing
tup = tuple("Geeks")
print(tup[0])

# Accessing a range of elements using slicing
print(tup[1:4])  
print(tup[:3])

# Tuple unpacking
tup = ("Geeks", "For", "Geeks")

# This line unpack values of Tuple1
a, b, c = tup
print(a)
print(b)
print(c)

'''
Concatenation of Tuples
Tuples can be concatenated using the + operator. This operation combines two or more tuples to create a new tuple.

'''
tup1 = (0, 1, 2, 3)
tup2 = ('Geeks', 'For', 'Geeks')

tup3 = tup1 + tup2
print(tup3)

'''
Slicing of Tuple
Slicing a tuple means creating a new tuple from a subset of elements of the original tuple.
 The slicing syntax is tuple[start:stop:step].

'''

tup = tuple('GEEKSFORGEEKS')

# Removing First element
print(tup[1:])

# Reversing the Tuple
print(tup[::-1])

# Printing elements of a Range
print(tup[4:9])


'''
Deleting a Tuple
Since tuples are immutable, we cannot delete individual elements of a tuple. However, we can delete an entire tuple using del statement.

'''

# tup = (0, 1, 2, 3, 4)
# del tup

# print(tup)

'''
Tuple Unpacking with Asterisk (*)
In Python, the " * " operator can be used in tuple unpacking to grab multiple items into a list. 
This is useful when you want to extract just a few specific elements and collect the rest together

'''

tup = (1, 2, 3, 4, 5)

a, *b, c = tup

print(a) 
print(b) 
print(c)

'''
a gets the first item.
c gets the last item.
*b collects everything in between into a list.

'''