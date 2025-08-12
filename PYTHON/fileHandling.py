'''
File Handling in Python


File handling refers to the process of performing operations on a file, such as creating, opening, reading, writing and closing it through a programming interface. 
It involves managing the data flow between the program and the file system on the storage device, ensuring that data is handled safely and efficiently.


Why do we need File Handling
--> To store data permanently, even after the program ends.
--> To access external files like .txt, .csv, .json, etc.
--> To process large files efficiently without using much memory.
--> To automate tasks like reading configs or saving outputs.
--> To handle input/output in real-world applications and tools.


'''

"""
Opening a File in Python
To open a file, we can use open() function, which requires file-path and mode as arguments:

Syntax:

file = open('filename.txt', 'mode')

--> filename.txt: name (or path) of the file to be opened.
--> mode: mode in which you want to open the file (read, write, append, etc.).
--> Note: If you don’t specify the mode, Python uses 'r' (read mode) by default.


"""
import os
os.chdir(os.path.dirname(__file__))


f = open("demo.txt", "r")
print(f.read())
f.close()


# This code opens the file demo.txt in read mode. 
# If the file exists, it connects successfully, otherwise, it throws an error.

'''
Closing a File
It's important to close the file after you're done 
using it. file.close() method closes the file and releases the system resources ensuring that changes are saved properly (in case of writing)

'''

file = open("demo.txt", "r")
# Perform file operations
file.close()

# Once the file is open, we can check some of its properties:

f = open("demo.txt", "r")

print("Filename:", f.name)
print("Mode:", f.mode)
print("Is Closed?", f.closed)

f.close()
print("Is Closed?", f.closed)


'''
Explanation:

--> f.name: Returns the name of the file that was opened (in this case, "demo.txt").
--> f.mode: Tells us the mode in which the file was opened. Here, it’s 'r' which means read mode.
--> f.closed: Returns a boolean value- Fasle when file is currently open otherwise True.
    

'''

"""
Reading a File
Reading a file can be achieved by file.read() which reads the entire content of the file. 
After reading the file we can close the file using file.close() which closes the file after reading it, which is necessary to free up system resources.

"""

file = open("demo.txt", "r")
content = file.read()
print(content)
file.close()

'''
Using with Statement
Instead of manually opening and closing the file, you can use the with statement, which automatically handles closing. 
This reduces the risk of file corruption and resource leakage.

'''
with open("demo.txt", "r") as file:
    content = file.read()
    print(content)

'''
Handling Exceptions When Closing a File
It's important to handle exceptions to ensure that files are closed properly, 
even if an error occurs during file operations.

'''
try:
    file = open("demo.txt", "r")
    content = file.read()
    print(content)
finally:
    file.close()