''''
In any programming language, usage of resources like file operations or database connections is very common, but limited. 
Therefore, main problem lies in making sure to release these resources after usage. 
If they are not released then it will lead to resource leakage and may cause system to either slow down or crash.
Python’s context managers provide a neat way to automatically set up and clean up resources, ensuring they’re properly managed even if errors occur.


Why Do We Need Context Managers?

--> Automatic cleanup: Frees resources like files or connections without manual effort.
--> Avoid resource leaks: Ensures proper release, even if errors occur.
--> Cleaner code: Replaces verbose try-finally blocks with with.
--> Exception-safe: Always performs cleanup, even on exceptions.
--> Custom control: Lets you manage any resource using __enter__ and __exit__.


Risks of Not Closing Resources
Failing to close resources like files can lead to serious issues, such as exhausting available system file descriptors. 
This can cause your program or even the entire system to slow down or crash.

'''

'''
This code repeatedly opens a file without closing it, leading to resource exhaustion and a potential system error.


'''

# file_descriptors = []
# for x in range(100000):
#     file_descriptors.append(open('test.txt', 'w'))

# This happens because too many files are left open without being closed, something context managers help avoid.

'''
Built-in Context Manager for File Handling
File operations are a common case in Python where proper resource management is crucial. 
The with statement provides a built-in context manager that ensures file is automatically closed once you're done with it, even if an error occurs.

'''
with open("test.txt") as f:
    data = f.read()

# __enter__(): sets up the resource and returns it.
# __exit__(): cleans up the resource (e.g., closes a file).

class ContextManager:
    def __init__(self):
        print('init method called')
        
    def __enter__(self):
        print('enter method called')
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called')

with ContextManager() as manager:
    print('with statement block')