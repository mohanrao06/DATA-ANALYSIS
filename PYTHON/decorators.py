'''
vIn Python, decorators are a powerful and flexible way to modify or extend the behavior of functions or methods, 
without changing their actual code.

A decorator is essentially a function that takes another function as an argument and returns a new function with enhanced functionality.
Decorators are often used in scenarios such as logging, 
authentication and memorization, allowing us to add additional functionality to existing functions or methods in a clean, reusable way.

'''

# A simple decorator function
def decorator(func):
  
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

# Applying the decorator to a function
@decorator

def greet():
    print("Hello, World!")

greet()

# decorator takes the greet function as an argument.
# It returns a new function (wrapper) that first prints a message, calls greet() and then prints another message.
# The @decorator syntax is a shorthand for greet = decorator(greet).

"""
Higher-Order Functions
In Python, higher-order functions are functions that take one or more functions as arguments, 
return a function as a result or do both. Essentially, a higher-order function is a function that operates on other functions. This is a powerful concept in functional programming and is a key component in understanding how decorators work.

Key Properties of Higher-Order Functions:
--> Taking functions as arguments: A higher-order function can accept other functions as parameters.
--> Returning functions: A higher-order function can return a new function that can be called later.

"""
# A higher-order function that takes another function as an argument
def fun(f, x):
    return f(x)

# A simple function to pass
def square(x):
    return x * x

# Using apply_function to apply the square function
res = fun(square, 5)
print(res)


'''
Role in Decorators:
Decorators in Python are a type of higher-order function because they take a function as input, modify it, and return a new function that extends or changes its behavior. 
Understanding higher-order functions is essential for working with decorators since decorators are essentially functions that return other functions.

'''

"""
Functions as First-Class Objects
In Python, functions are first-class objects, meaning that they can be treated like any other object, such as integers, strings, or lists. This gives functions a unique level of flexibility and allows them to be passed around and manipulated in ways that are not possible in many other programming languages.

What Does It Mean for Functions to Be First-Class Objects?
--> Can be assigned to variables: Functions can be assigned to variables and used just like any other value.
--> Can be passed as arguments: Functions can be passed as arguments to other functions.
--> Can be returned from other functions: Functions can return other functions, which is a key concept in decorators.
--> Can be stored in data structures: Functions can be stored in lists, dictionaries, or other data structures.

"""

# Assigning a function to a variable
def greet(n):
    return f"Hello, {n}!"

say_hi = greet  # Assign the greet function to say_hi
print(say_hi("Alice"))  # Output: Hello, Alice!

# Passing a function as an argument
def apply(f, v):
    return f(v)

res = apply(say_hi, "Bob")
print(res)  # Output: Hello, Bob!

# Returning a function from another function
def make_mult(f):
    def mult(x):
        return x * f
    return mult

dbl = make_mult(2)
print(dbl(5))  # Output: 10

'''
Explanation:

--> The code defines a greet function that returns a greeting message.
--> The greet function is assigned to the say_hi variable, which is used to print a greeting for "Alice".
--> Another function, apply, takes a function and a value as arguments, applies the function to the value, and returns the result.
--> apply is demonstrated by passing say_hi and "Bob", printing a greeting for "Bob".
--> The make_mult function creates a multiplier function based on a given factor.

'''

"""
Role of First-Class Functions in Decorators
--> Decorators receive the function to be decorated as an argument. This allows the decorator to modify or enhance the function's behavior.
--> Decorators return a new function that wraps the original function. This new function adds additional behavior before or after the original function is called.
--> When a function is decorated, it is assigned to the variable name of the original function. This means the original function is replaced by the decorated (wrapped) function.

"""

'''
Types of Decorators
1. Function Decorators:
The most common type of decorator, which takes a function as input and returns a new function. The example above demonstrates this type.

'''

def simple_decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@simple_decorator
def greet():
    print("Hello, World!")

greet()


'''
2. Method Decorators:
Used to decorate methods within a class. 
They often handle special cases, such as the self argument for instance methods.

'''

def method_decorator(func):
    def wrapper(self, *args, **kwargs):
        print("Before method execution")
        res = func(self, *args, **kwargs)
        print("After method execution")
        return res
    return wrapper

class MyClass:
    @method_decorator
    def say_hello(self):
        print("Hello!")

obj = MyClass()
obj.say_hello()


'''
3. Class Decorators
Class decorators are used to modify or enhance the behavior of a class. Like function decorators, 
class decorators are applied to the class definition. They work by taking the class as an argument and returning a modified version of the class.

'''

def fun(cls):
    cls.class_name = cls.__name__
    return cls

@fun
class Person:
    pass

print(Person.class_name)


"""
Common Built-in Decorators in Python
Python provides several built-in decorators that are commonly used in class definitions. These decorators modify the behavior of methods and attributes in a class,
 making it easier to manage and use them effectively. The most frequently used built-in decorators are @staticmethod, @classmethod, and @property.

@staticmethod
The @staticmethod decorator is used to define a method that doesn't operate on an instance of the class (i.e., it doesn't use self). 
Static methods are called on the class itself, not on an instance of the class.

"""
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

# Using the static method
res = MathOperations.add(5, 3)
print(res)


"""
@classmethod
The @classmethod decorator is used to define a method that operates on the class itself (i.e., it uses cls). 
Class methods can access and modify class state that applies across all instances of the class.

"""

class Employee:
    raise_amount = 1.05

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

# Using the class method
Employee.set_raise_amount(1.10)
print(Employee.raise_amount)

"""
@property
The @property decorator is used to define a method as a property, which allows you to access it like an attribute. 
This is useful for encapsulating the implementation of a method while still providing a simple interface.

"""

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius cannot be negative")

    @property
    def area(self):
        return 3.14159 * (self._radius ** 2)

# Using the property
c = Circle(5)
print(c.radius) 
print(c.area)    
c.radius = 10
print(c.area)