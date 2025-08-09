'''
Python String


A string is a sequence of characters. Python treats anything inside quotes as a string.
This includes letters, numbers, and symbols. Python has no character data type so single character is a string of length 1.

'''
s = "GfG"

print(s[1]) # access 2nd char
s1 = s + s[0] # update
print(s1) # print

"""
Creating a String
Strings can be created using either single (') or double (") quotes.

"""
s1 = 'GfG'
s2 = "GfG"
print(s1)
print(s2)

# Multi-line Strings
s = """I am Learning
Python String on GeeksforGeeks"""
print(s)

s = '''I'm a 
Geek'''
print(s)


'''
Accessing characters in Python String
Strings in Python are sequences of characters, so we can access individual characters using indexing. 
Strings are indexed starting from 0 and -1 from end. This allows us to retrieve specific characters from the string.

'''
s = "GeeksforGeeks"

# Accesses first character: 'G'
print(s[0])  

# Accesses 5th character: 's'
print(s[4])

# Access string with Negative Indexing
s = "GeeksforGeeks"

# Accesses 3rd character: 'k'
print(s[-10])  

# Accesses 5th character from end: 'G'
print(s[-5])


'''String Slicing
Slicing is a way to extract portion of a string by specifying the start and end indexes. 
The syntax for slicing is string[start:end], where start starting index and end is stopping index (excluded).
'''
# Retrieves characters from index 1 to 3: 'eek'
print(s[1:4])  

# Retrieves characters from beginning to index 2: 'Gee'
print(s[:3])   

# Retrieves characters from index 3 to the end: 'ksforGeeks'
print(s[3:])   

# Reverse a string
print(s[::-1])


'''
String Immutability
Strings in Python are immutable. This means that they cannot be changed after they are created. 
If we need to manipulate strings then we can use methods like concatenation, slicing, or formatting to create new strings based on the original.
'''

s = "geeksforGeeks"

# Trying to change the first character raises an error
# s[0] = 'I'  # Uncommenting this line will cause a TypeError

# Instead, create a new string
s = "G" + s[1:]
print(s)


'''Deleting a String
In Python, it is not possible to delete individual characters from a string since strings are immutable. 
However, we can delete an entire string variable using the del keyword.
'''
s = "GfG"

# Deletes entire string
del s


# Common String Methods

# --> len(): The len() function returns the total number of characters in a string.
s = "GeeksforGeeks"
print(len(s))

# output: 13

# --> upper() and lower(): upper() method converts all characters to uppercase. lower() method converts all characters to lowercase.

s = "Hello World"

print(s.upper())   # output: HELLO WORLD

print(s.lower())   # output: hello world

# strip() and replace(): strip() removes leading and trailing whitespace from the string and replace(old, new) replaces all occurrences of a specified substring with another.

s = "   Gfg   "

# Removes spaces from both ends
print(s.strip())    

s = "Python is fun"

# Replaces 'fun' with 'awesome'
print(s.replace("fun", "awesome"))


'''Concatenating and Repeating Strings
We can concatenate strings using + operator and repeat them using * operator.

Strings can be combined by using + operator.

'''
s1 = "Hello"
s2 = "World"
s3 = s1 + " " + s2
print(s3)



