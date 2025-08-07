age = 20

# if age >= 18:
#     print("Eligible to vote.")

age = 19
if age > 18: print("Eligible to Vote.")



# if-else statment ....-->

age = 10

if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")


'''
elif Statement
elif statement in Python stands for "else if." It allows us to check multiple conditions , providing a way to execute different blocks of code based on which condition is true. Using elif statements makes our code more readable and efficient by eliminating the need for multiple nested if statements.

If-elif-else-Statement-3.webp
'''


age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")


'''
Nested if..else Conditional Statements in Python
Nested if..else means an if-else statement inside another if statement. We can use nested if statements to check conditions within conditions.
'''

age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")