# DOCTEST EXAMPLE

import math
import doctest #<-- check it out!

def mysqrt(num, k):
    '''(int, int) -> float

    Generates and returns an approximate square root of num,
    a positive integer, via an iterative process
    that runs k times. 

    >>> mysqrt(25, 5)
    5.000023178253949
    >>> mysqrt(25, 10)
    5.0
    >>> mysqrt(100, 10)
    10.0
    >>> mysqrt(625, 10)
    25.0
    >>> mysqrt(10000, 8)
    101.20218365353946
    >>> mysqrt(10000, 10)
    100.00000025490743
    >>> mysqrt(10000, 11)
    00.0
 
    '''
    # iterative process calculates
    # approximate square root
    
    x = 1
    for i in range(k):
        x = .5 * (x + num/x)

    return x

def doctest_print_example(some_string):
i   '''
     function just prints some_string, with an EXTRA newline character

    >>> doctest_print_example("Hello world!")
    Hello world!


    '''
    print(some_string + '\n') # <-- THERE IT IS!
    return None


doctest.testmod()


'''
things to NOTICE!!!!

the syntax for an example in the docstring is:
>>> functioncall(params)
expected output

Note that this includes a SPACE after the >>>

testmod() RETURNS its value, it doesn't print anything..
 so WE need to print it if we want to see the results

Also, doctest is considered "brittle", meaning it's very sensitive to syntax and output format.
For example, it will notice if we are missing a newline character in an output.
(check out the doctest_print_example() function in this module.)
'''




# ASSERT STATEMENTS

# Assert statement examples

'''
assert statements in Python:

WHAT are they? 
- "assert" is a Python key word, (like if, else, for, while, or, and, not, return, etc.)
- Assert statements are a way of checking whether or not a condition is true.


What's the syntax?
- see example below
it's essentially "assert (BOOLEAN EXPRESSION)"

If the EXPRESSION == True, nothing happens.
If the EXPRESSION == False, Python raises an AssertionError


WHEN/WHY to use it?
Note that "assert condition" is functionally equivalent to the following:
if not condition:
    raise AssertionError()

assert IS:
	Assert is a convenient debugging aid.
	It allows you to quickly test whether a condition that you think / hope is true
	is indeed true at that moment in your code.
	*can be universally disabled when no longer needed, without having to remove all the statements (Beyond the scope of this class..)


assert is NOT:
	A replacement for proper error handling and program flow redirection.
	(If the condition is false, your program simply exits with an error...
		Sometimes this is NOT what you want your program to do!!! )
	A good way to output useful information to your user.
	A failsafe debugging tool.
'''

def false_assert():
    ''' Raises an assertion error '''
    condition = False
    assert condition
    print("Inside false_assert()... condition = %s" % condition)
    return None


def btod(bin_str):
    '''
     Hey pay attention, this is how you do the extra credit.
    '''
    assert type(bin_str) == str
    print("Your string is " + bin_str)
    return None

#false_assert()
btod("1100101")

