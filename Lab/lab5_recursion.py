'''
DEBUGGING TIPS:

1) Don't write too much code at once.
2) Don't take for granted what you think the value of your variables are.
    ---> Print statements are your friends.
3) Change one thing at a time (like a good controlled experiment).
4) Use the shell to examine small expressions (especially ones you're not 100%
    familiar with).
5) Design from the top down, CODE from the bottom-up.
    ---> Make sure your auxiliary functions (helper functions) are 100% correct.
6) You can't just "think really hard and then get it". DO SOMETHING.
    ---> It's amazing how fast new evidence will present itself.
'''



# Function to find palindrome words
# Palindrome - word that reads the same backward as forward

def is_pal(s):
    '''
    (str) -> boolean

    Returns true if s is a palindrome,
        false otherwise.

    Example:
    >>> is_pal('noon')
    True
    >>> is_pal('hello')
    False
    '''

    while len(s)>0:
        if s[0] != s[-1]:
            return False
        s = s[1:-1]

    return True



# Equivalence classes

'''
Types of equivalence classes:
    - long
    - short
    - single character
    - empty
    - True
    - False
'''



'''
RECURSION:

DEF - Method of solving problems in which the solution to your problem can
    be expressed int terms of solutions to SMALLER INSTANCES OF THE SAMMMMME
    PROBLEM.

A recursive solution in computing requires two things:
    1) BASE CASE!!! <--- Trivial, terminating case
    2) Recursive relationship
        ---> Involving a recursive call to some function
'''

# Recursive algorithm for stars

def stars(n):
    '''

    '''

    if n == 1:
        print('*', end = '')
    else:
        stars(n-1)
        print(n * '*', end = '')
        stars(n-1)

    return None




# FACTORIAL FUNCTION

def fact(x):
    '''
    (int) -> int

    Returns a factorial integer.

    Example:
    >>> fact(3)
    6
    >>> fact(0)
    1
    '''
    
    if x == 0:
        return 1

    return x * fact(x-1)



def is_palr(s):
    '''

    '''

    if len(s) == 0 or len(s) == 1:
        return True

    return is_palr(s[1:-1]) and (S[0] == S[-1])






# Lab 5 Recursion Examples

def is_palindrome(string):
    ''' (str) -> str
    Returns True if (string) is a palindrome, False otherwise.
    Examples:
    >>> palindrome("racecar")
    True
    >>> palindrome("whatever")
    False
    >>> palidrome("")
    True
    '''

    if (len(string) <= 1):
        return True

    return (string[0] == string[-1]) and is_palindrome(string[1:-1])


print("Is 'racecar' a palindrome?   ", is_palindrome("racecar"))
print("Is 'whatever' a palindrome?  ", is_palindrome("whatever"))
print("What about the empty string?   ", is_palindrome(""))

#=======================================================

def factorial(x):
    ''' (int) -> int
    Calculates and returns the factorial of x (x!).
    Examples:
    >>> factorial(0)
    1
    >>> factorial(4)
    24
    '''

    if x == 0:
        return 1

    return x * factorial(x - 1)


print("Factorial 0 = ", factorial(0))
print("Factorial 1 = ", factorial(1))
print("Factorial 4 = ", factorial(4))
print("Factorial 10 = ", factorial(10))

#=======================================================

def exp(x, n):
    '''(num, int) -> num
    Calculates and returns x raised to the nth power.
    Examples:
    >>> exp(2, 5)
    32
    >>> exp(100, 0)
    1
    >>> exp(10, 2)
    100
    '''
    
    if (n == 0):
        return 1
    return x * exp(x, n - 1)

print("2^5 = ", exp(2, 5))
print("100^0 = ", exp(100, 0))

