
from __future__ import print_function

'''
Loops in Python - For, While and Nested Loops
Loops in Python are used to repeat actions efficiently. The main types are For loops (counting through items) and While loops (based on conditions). In this article, we will look at Python loops and understand their working with the help of examples.
'''
"""
For Loop in Python
For loops is used to iterate over a sequence such as a list, tuple, string or range. It allow to execute a block of code repeatedly, once for each item in the sequence.
Syntax:
for iterator_var in sequence:
    statements(s)
"""
n=10
for i in range(0,10):
    print(i)


li = ["geeks", "for", "geeks"]
for i in li:
    print(i)

li = ["geeks", "for", "geeks"]
for i in range (0,len(li)):
    print(li[i])
    
tup = ("geeks", "for", "geeks")
for i in tup:
    print(i)
    
s = "Geeks"
for i in s:
    print(i)
    
d = dict({'x':123, 'y':354})
for i in d:
    print("%s  %d" % (i, d[i]))
    
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i),


'''

While Loop in Python
In Python, a while loop is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the line immediately after the loop in the program is executed.

Syntax:
while expression:
    statement(s)

'''

cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hello Geek")


'''
Nested Loops in Python
Python programming language allows to use one loop inside another loop which is called nested loop. Following section shows few examples to illustrate the concept. 

Syntax:
for iterator_var in sequence:
   for iterator_var in sequence:
       statements(s)
   statements(s)

while expression:
   while expression: 
       statement(s)
   statement(s)

'''


for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()