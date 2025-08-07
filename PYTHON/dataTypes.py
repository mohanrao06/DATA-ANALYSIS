# data types...
#  int, float, string, list and set


x = 50
x = 60.5
x = "Hello World"
x = ["geeks", "for", "geeks"]
x = ("geeks", "for", "geeks")




# 1. Numeric Data Types in Python
# Numeric data types are immutable data types that store numeric values.
# Numeric data types include int, float, and complex numbers.

a= 10  # int
print(type(a))
b= 20.5  # float
print(type(b))
c= 3 + 4j  # complex
print(type(c))


# 2.sequence Data Types in Python
# Sequence data types are ordered collections of items.
# Sequence data types include strings, lists, and tuples.


s = "Hello World"  # string
print(type(s))
print(s[0])
print(s[-1])
print(s[0:5])


# Empty list
a = []

# list with int values
a = [1, 2, 3]
print(a)

# list with mixed int and string
b = ["Geeks", "For", "Geeks", 4, 5]
print(b)

a = ["Geeks", "For", "Geeks"]
print("Accessing element from the list")
print(a[0])
print(a[2])

print("Accessing element using negative indexing")
print(a[-1])
print(a[-3])

# initiate empty tuple
tup1 = ()

tup2 = ('Geeks', 'For')
print("\nTuple with the use of String: ", tup2)

tup1 = tuple([1, 2, 3, 4, 5])

# access tuple items
print(tup1[0])
print(tup1[-1])
print(tup1[-3])


# 3. Boolean Data Type in Python
print(type(True))
print(type(False))
# print(type(true))   #this will give you  error--->


# initializing empty set
s1 = set()

s1 = set("GeeksForGeeks")
print("Set with the use of String: ", s1)

s2 = set(["Geeks", "For", "Geeks"])
print("Set with the use of List: ", s2)



set1 = set(["Geeks", "For", "Geeks"])
print(set1)

# loop through set
for i in set1:
    print(i, end=" ")
    
# check if item exist in set    
print("\n")
print("Geeks" in set1)



# initialize empty dictionary
d = {}


d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d)

# creating dictionary using dict() constructor
d1 = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print(d1)

d = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

# Accessing an element using key
print(d['name'])

# Accessing a element using get
print(d.get(3))



# Python Operators