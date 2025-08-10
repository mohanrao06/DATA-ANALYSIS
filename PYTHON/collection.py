from collections import Counter 
  


'''
Python Collections Module


The collections module in Python provides specialized containers (different from general purpose built-in containers like dict, list, tuple and set). 
These specialized containers are designed to address specific programming needs efficiently and offer additional functionalities.

'''

"""
Why do we need Collections Module?
1. Provides specialized container data types beyond built-in types like list, dict and tuple.
2. Includes efficient alternatives such as deque, Counter, OrderedDict, defaultdict and namedtuple.
3. Simplifies complex data structure handling with cleaner and faster implementations.
3. Helps in frequency counting, queue operations and structured records with minimal code.
4. Ideal for improving performance and code readability in data-heavy applications.

"""

'''
Counters
A counter is a sub-class of the dictionary. 
It is used to keep the count of the elements in an iterable in the form of an unordered dictionary where the key represents element in the iterable and value represents the count of that element in the iterable.

Note: It is equivalent to bag or multiset of other languages.

Syntax:

class collections.Counter([iterable-or-mapping])

'''

'''
Initializing Counter Objects
The counter object can be initialized using counter() function and this function can be called in one of the following ways:

--> With a sequence of items
--> With a dictionary containing keys and counts
--> With keyword arguments mapping string names to counts

'''
 
  
# Creating Counter from a list (sequence of items)  
print(Counter(['B','B','A','B','C','A','B','B','A','C']))
  
# Creating Counter from a dictionary
print(Counter({'A':3, 'B':5, 'C':2}))
  
# Creating Counter using keyword arguments
print(Counter(A=3, B=5, C=2))


'''
OrderedDict
An OrderedDict is a dictionary that preserves the order in which keys are inserted. 
While regular dictionaries do this from Python 3.7+, OrderedDict also offers extra features like moving re-inserted keys to the end making it useful for order-sensitive operations.

Syntax: 
        class collections.OrderDict()

'''
from collections import OrderedDict 
print("This is a Dict:\n") 
d = {} 
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
  
for key, value in d.items(): 
    print(key, value) 
  
print("\nThis is an Ordered Dict:\n") 
od = OrderedDict() 
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
  
for key, value in od.items(): 
    print(key, value)



from collections import OrderedDict 
od = OrderedDict() 
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
  
print('Before Deleting')
for key, value in od.items(): 
    print(key, value) 
    
# deleting element
od.pop('a')

# Re-inserting the same
od['a'] = 1

print('\nAfter re-inserting')
for key, value in od.items(): 
    print(key, value)

'''
DefaultDict
A DefaultDict is also a sub-class to dictionary. 
It is used to provide some default values for the key that does not exist and never raises a KeyError.

Syntax:

class collections.defaultdict(default_factory)

default_factory is a function that provides the default value for the dictionary created. 
If this parameter is absent then the KeyError is raised.

Initializing DefaultDict Objects
DefaultDict objects can be initialized using DefaultDict() method by passing the data type as an argument.

'''

from collections import defaultdict 

# Creating a defaultdict with default value of 0 (int)
d = defaultdict(int) 
L = [1, 2, 3, 4, 2, 4, 1, 2] 

# Counting occurrences of each element in the list
for i in L: 
    d[i] += 1  # No need to check key existence; default is 0

print(d)



  
# Defining a dict 
d = defaultdict(list) 
  
for i in range(5): 
    d[i].append(i) 
      
print("Dictionary with values as list:") 
print(d)



'''
ChainMap
A ChainMap encapsulates many dictionaries into a single unit and returns a list of dictionaries.

Syntax:

class collections.ChainMap(dict1, dict2)

'''

from collections import ChainMap 
   
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

# Defining the chainmap 
c = ChainMap(d1, d2, d3) 
print(c)


'''
Accessing Keys and Values from ChainMap
Values from ChainMap can be accessed using the key name. They can also be accessed by using the keys() and values() method.

'''


   
# Accessing Values using key name
print(c['a'])

# Accessing values using values()
print(c.values())

# Accessing keys using keys()
print(c.keys())


'''
Adding new dictionary
A new dictionary can be added by using the new_child() method. The newly added dictionary is added at the beginning of the ChainMap.

'''

import collections 
  
# initializing dictionaries 
dic1 = { 'a' : 1, 'b' : 2 } 
dic2 = { 'b' : 3, 'c' : 4 } 
dic3 = { 'f' : 5 } 
  
# initializing ChainMap 
chain = collections.ChainMap(dic1, dic2) 
  
# printing chainMap 
print ("All the ChainMap contents are: ") 
print (chain) 
  
# using new_child() to add new dictionary 
chain1 = chain.new_child(dic3) 
  
# printing chainMap
print ("Displaying new ChainMap : ") 
print (chain1)


"""
NamedTuple
A NamedTuple is like a regular tuple but with named fields, making data more readable and accessible. 
Instead of using indexes, you can access elements by name (e.g., student.fname), which improves code clarity and ease of use.

Syntax:

class collections.namedtuple(typename, field_names)

"""

from collections import namedtuple
  
# Declaring namedtuple() 
Student = namedtuple('Student',['name','age','DOB']) 
  
# Adding values 
S = Student('Nandini','19','2541997') 
  
# Access using index 
print ("The Student age using index is : ",end ="") 
print (S[1]) 
  
# Access using name  
print ("The Student name using keyname is : ",end ="") 
print (S.name)


"""
Conversion Operations 
1. _make(): This function is used to return a namedtuple() from the iterable passed as argument.

2. _asdict(): This function returns the OrdereDict() as constructed from the mapped values of namedtuple().


"""
Student = namedtuple('Student',['name','age','DOB']) 
  
# Adding values 
S = Student('Nandini','19','2541997') 
  
# initializing iterable  
li = ['Manjeet', '19', '411997' ] 
  
# initializing dict 
di = { 'name' : "Nikhil", 'age' : 19 , 'DOB' : '1391997' } 
  
# using _make() to return namedtuple() 
print ("The namedtuple instance using iterable is  : ") 
print (Student._make(li)) 

# using _asdict() to return an OrderedDict() 
print ("The OrderedDict instance using namedtuple is  : ") 
print (S._asdict())


"""
Deque
Deque (Doubly Ended Queue) is the optimized list for quicker append and pop operations from both sides of the container. 
It provides O(1) time complexity for append and pop operations as compared to list with O(n) time complexity.

Syntax:

class collections.deque(list)

This function takes the list as an argument.

"""

from collections import deque
  
# Declaring deque
queue = deque(['name','age','DOB']) 
print(queue)


"""
Inserting Elements
Elements in deque can be inserted from both ends. 
To insert the elements from right append() method is used and to insert the elements from the left appendleft() method is used.

"""

de = deque([1, 2, 3]) 
  
# Append 4 to the right end of deque
de.append(4) 
  
# Print deque after appending to the right
print("The deque after appending at right is :") 
print(de) 
  
# Append 6 to the left end of deque
de.appendleft(6) 
  
# Print deque after appending to the left
print("The deque after appending at left is :") 
print(de)


"""
Removing Elements
Elements can also be removed from the deque from both the ends. 
To remove elements from right use pop() method and to remove elements from the left use popleft() method.
"""
de.pop()

# Print deque after deletion from the right
print("The deque after deleting from right is :") 
print(de)

# Delete element from the left end (removes 6)
de.popleft()

# Print deque after deletion from the left
print("The deque after deleting from left is :") 
print(de)

"""
UserDict
UserDict is a dictionary-like container that acts as a wrapper around the dictionary objects. This container is used when someone wants to create their own dictionary with some modified or new functionality. 

Syntax:

class collections.UserDict([initialdata])

"""
from collections import UserList 

# Creating a list where deletion is not allowed
class MyList(UserList): 
      
    # Prevents using remove() on list
    def remove(self, s=None): 
        raise RuntimeError("Deletion not allowed") 
          
    # Prevents using pop() on list
    def pop(self, s=None): 
        raise RuntimeError("Deletion not allowed") 
      
# Create an instance of MyList
L = MyList([1, 2, 3, 4]) 
print("Original List") 

# Append 5 to the list
L.append(5) 
print("After Insertion") 
print(L) 
# Attempt to remove an item (will raise error)
L.remove()