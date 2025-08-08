'''
Python Functions is a block of statements that does a specific task. The idea is to put some commonly or repeatedly done task together and make a function so that instead of writing the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again.

Benefits of Using Functions :-
--> Code Reuse
--> Reduced code length
--> Increased redability of code

Types of Functions in Python
Below are the different types of functions in Python:

--> Built-in library function: These are Standard functions in Python that are available to use.
==> User-defined function: We can create our own functions based on our requirements.

'''

"""
Creating a Function in Python
We can define a function in Python, using the def keyword. We can add any type of functionalities and properties to it as we require.

What is def ?
The def keyword stands for define. It is used to create a user-defined function. It marks the beginning of a function block and allows you to group a set of statements so they can be reused when the function is called.

Syntax:

def function_name(parameters):

    # function body

    
"""
"""
Explanation:

--> def: Starts the function definition.
---> function_name: Name of the function.
---> parameters: Inputs passed to the function (inside ()), optional.
---> : : Indicates the start of the function body.
---> Indented code: The function body that runs when called.

"""
def fun():
    print("Welcome to venkey")

"""
Calling a Function in Python
After creating a function in Python we can call it by using the name of the functions Python followed by parenthesis containing parameters of that particular function. Below is the example for calling def function Python.

"""
fun()

"""
Python Function Arguments
Arguments are the values passed inside the parenthesis of the function. A function can have any number of arguments separated by a comma.

Syntax for functions with arguments:

 def function_name(parameter: data_type) -> return_type:
    
    # body of the function
    return expression

data_type and return_type are optional in function declaration, meaning the same function can also be written as:

 def function_name(parameter) :
    
    # body of the function
    return expression
"""

def even_odd(x):
    if(x%2==0):
        return "even"
    else:
        return "odd"
    
print(even_odd(10))

"""
Types of Python Function Arguments
Python supports various types of arguments that can be passed at the time of the function call. In Python, we have the following function argument types in Python:

--> Default argument
---> Keyword arguments (named arguments)
---> Positional arguments
---> Arbitrary arguments (variable-length arguments *args and **kwargs)
Let's discuss each type in detail. ......

"""


'''
Default Arguments
A default argument is a parameter that assumes a default value if a value is not provided in the function call for that argument. The following example illustrates Default arguments to write functions in Python.
'''
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)


myFun(10)


'''
Keyword Arguments
The idea is to allow the caller to specify the argument name with values so that the caller does not need to remember the order of parameters.

'''

def student(fname, lname):
    print(fname, lname)

student(fname='Geeks', lname='Practice')
student(lname='Practice', fname='Geeks')


'''
Positional Arguments
We used the Position argument during the function call so that the first argument (or value) is assigned to name and the second argument (or value) is assigned to age. By changing the position, or if you forget the order of the positions, the values can be used in the wrong places, as shown in the Case-2 example below, where 27 is assigned to the name and Suraj is assigned to the age.

'''
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)


print("Case-1:")
nameAge("Suraj", 27)

print("\nCase-2:")
nameAge(27, "Suraj")

'''
Arbitrary Keyword  Arguments
In Python Arbitrary Keyword Arguments, *args, and **kwargs can pass a variable number of arguments to a function using special symbols. There are two special symbols:

*args in Python (Non-Keyword Arguments)
**kwargs in Python (Keyword Arguments)

'''

def myFun(*argv):
    for arg in argv:
        print(arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


myFun(first='Geeks', mid='for', last='Geeks')



'''
Docstring
The first string after the function is called the Document string or Docstring in short. This is used to describe the functionality of the function. The use of docstring in functions is optional but it is considered a good practice.

The below syntax can be used to print out the docstring of a function.

Syntax: print(function_name.__doc__)

'''

def evenOdd(x):
    """Function to check if the number is even or odd"""
    
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")


print(evenOdd.__doc__)


'''
Anonymous Functions in Python
In Python, an anonymous function means that a function is without a name. As we already know the def keyword is used to define the normal functions and the lambda keyword is used to create anonymous functions.

'''

def cube(x): return x*x*x   # without lambda

cube_l = lambda x : x*x*x  # with lambda

print(cube(7))
print(cube_l(7))


'''
Pass by Reference and Pass by Value
One important thing to note is, in Python every variable name is a reference. When we pass a variable to a function Python, a new reference to the object is created. Parameter passing in Python is the same as reference passing in Java.

'''

# Here x is a new reference to same list lst
def myFun(x):
    x[0] = 20

# Driver Code (Note that lst is modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)

def myFun(x):
    x = [20, 30, 40]


lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)