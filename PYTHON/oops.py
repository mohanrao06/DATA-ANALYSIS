'''
Python OOP Basics

comments
Object Oriented Programming is a fundamental concept in Python, empowering developers to build modular, maintainable, and scalable applications. By understanding the core OOP principles (classes, objects, inheritance, encapsulation, polymorphism, and abstraction), programmers can leverage the full potential of Python OOP capabilities to design elegant and efficient solutions to complex problems.

OOPs is a way of organizing code that uses objects and classes to represent real-world entities and their behavior. In OOPs, object has attributes thing that has specific data and can perform certain actions using methods.

OOPs Concepts in Python
---> Class in Python
---> Objects in Python
---> Polymorphism in Python
---> Encapsulation in Python
---> Inheritance in Python
---> Data Abstraction in Python

'''

'''
Python Class
A class is a collection of objects. Classes are blueprints for creating objects. A class defines a set of attributes and methods that the created objects (instances) can have.

Some points on Python class:  

--> Classes are created by keyword class.
--> Attributes are the variables that belong to a class.
--> Attributes are always public and can be accessed using the dot (.) operator. Example: Myclass.Myattribute

'''

class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

'''
Explanation:

--> class Dog: Defines a class named Dog.
--> species: A class attribute shared by all instances of the class.
---> __init__ method: Initializes the name and age attributes when a new object is created.

'''

'''
Python Objects
An Object is an instance of a Class. It represents a specific implementation of the class and holds its own data.

An object consists of:

State: It is represented by the attributes and reflects the properties of an object.
Behavior: It is represented by the methods of an object and reflects the response of an object to other objects.
Identity: It gives a unique name to an object and enables one object to interact with other objects.

'''

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)

print(dog1.name) 
print(dog1.species)
print(dog1.age)

'''
__init__ Method:- 
__init__ method is the constructor in Python, automatically called when a new object is created. It initializes the attributes of the class.
'''


'''
Class and Instance Variables
In Python, variables defined in a class can be either class variables or instance variables, and understanding the distinction between them is crucial for object-oriented programming.

Class Variables

These are the variables that are shared across all instances of a class. It is defined at the class level, outside any methods.
 All objects of the class share the same value for a class variable unless explicitly overridden in an object.

Instance Variables

Variables that are unique to each instance (object) of a class. 
These are defined within the __init__ method or other instance methods. Each object maintains its own copy of instance variables, independent of other objects.


'''

class Dog:
    # Class variable
    species = "Canine"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

# Create objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

# Access class and instance variables
print(dog1.species)  # (Class variable)
print(dog1.name)     # (Instance variable)
print(dog2.name)     # (Instance variable)

# Modify instance variables
dog1.name = "Max"
print(dog1.name)     # (Updated instance variable)

# Modify class variable
Dog.species = "Feline"
print(dog1.species)  # (Updated class variable)
print(dog2.species)