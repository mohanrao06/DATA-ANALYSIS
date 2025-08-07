""" Python Operators

    In Python programming, Operators in general are used to perform operations on values and variables. These are standard symbols used for logical and arithmetic operations. In this article, we will look into different types of Python operators. 

    OPERATORS: These are the special symbols. Eg- + , * , /, etc.
    OPERAND: It is the value on which the operator is applied.

"""

# Variables
a = 15
b = 4

# Addition
print("Addition:", a + b)  

# Subtraction
print("Subtraction:", a - b) 

# Multiplication
print("Multiplication:", a * b)  

# Division
print("Division:", a / b) 

# Floor Division
print("Floor Division:", a // b)  

# Modulus
print("Modulus:", a % b) 

# Exponentiation
print("Exponentiation:", a ** b)


# Comparison of Python Operators

a = 13
b = 33

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)


""" 
Logical Operators in Python
Python Logical operators perform Logical AND, Logical OR and Logical NOT operations. It is used to combine conditional statements.

"""

a = True
b = False
print(a and b)
print(a or b)
print(not a)


''' 
Bitwise Operators in Python
Python Bitwise operators act on bits and perform bit-by-bit operations. These are used to operate on binary numbers.

Bitwise Operators in Python are as follows:

Bitwise NOT
Bitwise Shift
Bitwise AND
Bitwise XOR
Bitwise OR

'''

a = 10
b = 4

print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)


'''  Assignment Operators in Python
Python Assignment operators are used to assign values to the variables. This operator is used to assign the value of the right side of the expression to the left side operand.
'''

a = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)


'''
Identity Operators in Python
In Python, is and is not are the identity operators both are used to check if two values are located on the same part of the memory. Two variables that are equal do not imply that they are identical. 

is  :-        True if the operands are identical 
is not  :-    True if the operands are not identical 

'''
a = 10
b = 20
c = a

print(a is not b)
print(a is c)

'''
Membership Operators in Python
In Python, in and not in are the membership operators that are used to test whether a value or variable is in a sequence.

in   :-         True if value is found in the sequence
not in  :-      True if value is not found in the sequence

'''

x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")



'''ernary Operator in Python
in Python, Ternary operators also known as conditional expressions are operators that evaluate something based on a condition being true or false. It was added to Python in version 2.5. 

It simply allows testing a condition in a single line replacing the multiline if-else making the code compact.

Syntax :  [on_true] if [expression] else [on_false] '''


a, b = 10, 20
min = a if a < b else b

print(min)