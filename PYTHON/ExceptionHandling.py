'''
Python Exception Handling handles errors that occur during the execution of a program. 
Exception handling allows to respond to the error, instead of crashing the running program. 
It enables you to catch and manage errors, making your code more robust and user-friendly. Let's look at an example:

'''

# Exception handling helps in preventing crashes due to errors. 
# Here’s a basic example demonstrating how to catch an exception and handle it gracefully:
# Simple Exception Handling Example
n = 10
try:
    res = n / 0  # This will raise a ZeroDivisionError
    
except ZeroDivisionError:
    print("Can't be divided by zero!")

'''
In this example, dividing number by 0 raises a ZeroDivisionError. 
The try block contains the code that might cause an exception and the except block handles the exception, 
printing an error message instead of stopping the program.
'''


"""
Difference Between Exception and Error
--> Error: Errors are serious issues that a program should not try to handle. 
    They are usually problems in the code's logic or configuration and need to be fixed by the programmer. 
    Examples include syntax errors and memory errors.
--> Exception: Exceptions are less severe than errors and can be handled by the program. 
    They occur due to situations like invalid input, missing files or network issues.

"""
# # Syntax Error (Error)
# print("Hello world"  # Missing closing parenthesis

# # ZeroDivisionError (Exception)
# n = 10
# res = n / 0

"""
Syntax and Usage
Exception handling in Python is done using the try, except, else and finally blocks.

try:
      # Code that might raise an exception
except SomeException:
      # Code to handle the exception
else:
     # Code to run if no exception occurs
finally:
    # Code to run regardless of whether an exception occurs

"""

"""
try, except, else and finally Blocks
--> try Block: try block lets us test a block of code for errors. 
    Python will "try" to execute the code in this block. 
    If an exception occurs, execution will immediately jump to the except block.
--> except Block: except block enables us to handle the error or exception. 
    If the code inside the try block throws an error, Python jumps to the except block and executes it. 
    We can handle specific exceptions or use a general except to catch all exceptions.
--> else Block: else block is optional and if included, must follow all except blocks. 
    The else block runs only if no exceptions are raised in the try block. 
    This is useful for code that should execute if the try block succeeds.
--> finally Block: finally block always runs, regardless of whether an exception occurred or not. 
    It is typically used for cleanup operations (closing files, releasing resources).

"""

try:
    n = 0
    res = 100 / n
    
except ZeroDivisionError:
    print("You can't divide by zero!")
    
except ValueError:
    print("Enter a valid number!")
    
else:
    print("Result is", res)
    
finally:
    print("Execution complete.")


'''
Explanation:

--> try block asks for user input and tries to divide 100 by the input number.
--> except blocks handle ZeroDivisionError and ValueError.
--> else block runs if no exception occurs, displaying the result.
--> finally block runs regardless of the outcome, indicating the completion of execution.

'''

"""
Python Catching Exceptions
When working with exceptions in Python, we can handle errors more efficiently by specifying the types of exceptions we expect. 
This can make code both safer and easier to debug.

Catching Specific Exceptions
Catching specific exceptions makes code to respond to different exception types differently.

"""

try:
    x = int("str")  # This will cause ValueError
    
    #inverse
    inv = 1 / x
    
except ValueError:
    print("Not Valid!")
    
except ZeroDivisionError:
    print("Zero has no inverse!")

# The ValueError is caught because the string "str" cannot be converted to an integer.
# If x were 0 and conversion successful, the ZeroDivisionError would be caught when attempting to calculate its inverse.


'''
Catching Multiple Exceptions
We can catch multiple exceptions in a single block if we need to handle them in the same way or we can 
separate them if different types of exceptions require different handling.

'''
a = ["10", "twenty", 30]  # Mixed list of integers and strings
try:
    total = int(a[2]) + int(a[1])  # 'twenty' cannot be converted to int
    
except (ValueError, TypeError) as e:
    print("Error", e)
    
except IndexError:
    print("Index out of range.")
    
# The ValueError is caught when trying to convert "twenty" to an integer.
# TypeError might occur if the operation was incorrectly applied to non-integer types, but it's not triggered in this specific setup.
# IndexError would be caught if an index outside the range of the list was accessed, but in this scenario, it's under control.

'''
Raise an Exception
We raise an exception in Python using the raise keyword followed by an instance of the exception class that we want to trigger. 
We can choose from built-in exceptions or define our own custom exceptions by inheriting from Python's built-in Exception class.

Basic Syntax:

raise ExceptionType("Error message")

'''
def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set(10)
except ValueError as e:
    print(e)

# The function set checks if the age is negative. If so, it raises a ValueError with a message explaining the issue.
# This ensures that the age attribute cannot be set to an invalid state, thus maintaining the integrity of the data.


"""
Advantages of Exception Handling:
--> Improved program reliability: By handling exceptions properly, you can prevent your 
    program from crashing or producing incorrect results due to unexpected errors or input.
--> Simplified error handling: Exception handling allows you to separate error handling code from the main program logic, 
    making it easier to read and maintain your code.
--> Cleaner code: With exception handling, you can avoid using complex conditional statements to check for errors, 
    leading to cleaner and more readable code.
--> Easier debugging: When an exception is raised, the Python interpreter prints a traceback that shows the exact location 
    where the exception occurred, making it easier to debug your code.
    
Disadvantages of Exception Handling:
--> Performance overhead: Exception handling can be slower than using conditional statements to check for errors, 
    as the interpreter has to perform additional work to catch and handle the exception.
--> Increased code complexity: Exception handling can make your code more complex, 
    especially if you have to handle multiple types of exceptions or implement complex error handling logic.
--> Possible security risks: Improperly handled exceptions can potentially reveal sensitive 
    information or create security vulnerabilities in your code, so it's important to handle exceptions carefully and avoid exposing too much information about your program.
"""