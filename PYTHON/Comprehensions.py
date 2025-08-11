"""
Comprehensions in Python

Comprehensions in Python provide a concise and efficient way to create new sequences from existing ones. 
They enhance code readability and reduce the need for lengthy loops.

Why do we need Comprehensions
--> Encourages Modular Thinking: Promotes writing logic in smaller, reusable expressions.
--> Widely Used in Real-World Code: Found in data science, web development and automation scripts.
--> Easier Debugging & Testing: Fewer lines reduce the surface area for bugs.
--> Seamless with Other Python Features: Integrates well with functions like zip(), enumerate() and lambda.


Types of Comprehensions in Python
Python offers different types of comprehensions to simplify creation of data structures in a clean, readable way. 
Let’s explore each type with simple examples.

"""

'''
1. List Comprehensions
List comprehensions allow for the creation of lists in a single line, improving efficiency and readability. 
They follow a specific pattern to transform or filter data from an existing iterable.

Syntax:

[expression for item in iterable if condition]

Where:

==> expression: Operation applied to each item.
==> item: Variable representing the element from the iterable.
==> iterable: The source collection.
==> condition (optional): A filter to include only specific items.

'''

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = [num for num in a if num%2 != 0] #This creates a list of even numbers by filtering elements from a that are divisible by 2.
print(res)

res = [num**2 for num in range(1, 6)]  #This generates a list of squares for numbers from 1 to 5.
print(res)



"""
2. Dictionary comprehension
Dictionary Comprehensions are used to construct dictionaries in a compact form, 
making it easy to generate key-value pairs dynamically based on an iterable.

Syntax:

{key_expression: value_expression for item in iterable if condition}

Where:

--> key_expression: Determines the dictionary key.
--> value_expression: Computes the value.
--> iterable: The source collection.
--> condition (optional): Filters elements before adding them.

"""

res = {i: i**2 for i in range(1,21)} #This creates a dictionary where keys are numbers from 1 to 5 and values are their squares
print(res)

a = ["Texas", "California", "Florida"] # states
b = ["Austin", "Sacramento", "Tallahassee"] # capital

res={state: cap for state,cap in zip(a,b)} # zip() function pairs each state with its corresponding capital, creating a dictionary.
print(res)


"""
3. Set comprehensions
Set Comprehensions are similar to list comprehensions but result in sets, automatically eliminating duplicate values while maintaining a concise syntax.

Syntax:

{expression for item in iterable if condition}

Where:

--> expression: The operation applied to each item.
--> iterable: The source collection.
--> condition (optional): Filters elements before adding them.

"""

a = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

res = {num for num in a if num % 2 == 0} #This creates a set of even numbers from a, automatically removing duplicates.
print(res)

res = {num**2 for num in range(1, 6)} # This generates a set of squares, ensuring each value appears only once.
print(res)


"""
3. Generator comprehensions
Generator Comprehensions create iterators that generate values lazily, making them memory-efficient as elements are computed only when accessed.

Syntax:

(expression for item in iterable if condition)

Where:

expression: Operation applied to each item.
iterable: The source collection.
condition (optional): Filters elements before including them.

"""

res = (num for num in range(10) if num % 2 == 0) #  This generator produces even numbers from 0 to 9, but values are only computed when accessed.
print(list(res))


res = (num**2 for num in range(1, 6))
print(tuple(res))