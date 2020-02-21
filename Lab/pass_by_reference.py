# CIS 210 Lab 8 - Try / Except / Finally Examples

'''
Here's the documentation if you want to read about it:
https://docs.python.org/3/tutorial/errors.html

try:
    Code in this block is connected to the following except (and finally) statement(s).
    If any errors occur here, the except statement is examined to see if they
    are supposed to be handled.
    The first exception raised causes the try block to terminate.
except [optional specification of specific exceptions]:
    This body is also optional.
    If any of the *specified* exceptions are caught, it executes.
    An empty body just means the exception is caught, but nothing happens.
finally:
    This code will be executed no matter what, just before the try block completes.
    OR, after the except block completes, IF IT WAS ENTERED.
    It's a way of saying, "no matter what happens, tell my mom I love her"
    ** generally used to release external resources, like files **

What are some common reasons to use Try/Except?
-> Typically, you want to be specific about the errors you are catching!
-> Therefore, it is usually bad style to except EVERYTHING (with the unadorned "except:" statement)
    -> this is because you should only except the errors that you have a reason to expect
    -> if "everything" is in that category....? then you're basically saying "My code is broken and fragile"
-> Handle bad user input.
-> Trying to import a module that might not exist.
-> Trying to open a file that might not exist.
'''
#==========================================================
"""
# Can you catch syntax errors?
def handle_syntaxError():
    try:
        while True print("<-- While loop is missing a colon!!!")
    except SyntaxError:
        print("Caught the syntax error, keepin' on...")
    return None

handle_syntaxError()
# NO! apparently not...
"""

#==========================================================
# Example: Catch ANY exception
def catch_them_all():
    try:
        x = 1/0 # <--- obvious division by 0 error
    except:
        print("Caught an exception")

catch_them_all()

#==========================================================
# Example: Catch ONE specific exception
def catch_divZero():
    try:
        x = 1/0
    except ZeroDivisionError:
        print("Caught a ZeroDivisionError")
        
catch_divZero()   
#==========================================================
# Example: Catch SEVERAL exceptions

def catch_multiple():
    datalist = [42, 56, 52332, 48596, 995, 1215, 3, -321, 4, 32]
    try:
        num = int(input("Enter an integer!")) # <-- might get a ValueError
        result = 1000 // num                  # <-- might get a ZeroDivisionError
        target = datalist[result]             # <-- might get an IndexError
    except (ZeroDivisionError, IndexError) as e:
        print("Caught exception: ", e)
    except ValueError:
        num = int(input("I said integer: "))

#==========================================================
catch_multiple()

