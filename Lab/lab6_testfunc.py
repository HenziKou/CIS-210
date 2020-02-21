# Demo of passing functions as arguments.
# This weeks project looks something like this!

def examine_function(f):
    '''
    (function) -> None

    Prints out some information about given function, including an example
    call.

    Example:
    >>> examine_function(myFunction)
    ...
    '''

    # assigns 'f.__name__' to be 'examine_function'
    print('\nName of func = ', f.__name__)
    print('Type of func = ', type(f))
    print('Memory location: ', id(f))
    print('Docstring of func: \n', f.__doc__)
    print('Result of call: ')
    print('return value: ', f())
    print()

    return None


def a():
    '''
    a's docstring
    '''

    print("We're in a!")

    return None


def b():
    '''
    b's docstring
    '''

    print("I'm in b!")

    return None


def c():
    '''
    c's docstring
    '''

    print("You get the idea...")

    return None


examine_function(a)
examine_function(b)
examine_function(c)





# Lab 6 Function demos:
# string formatting methods
# importing our own modules
# if __name__ == __main__:
# passing functions as arguments


def moneyformat(x):
    '''
    (num) -> string

    Returns the value x as a string formatted as USD.

    Example:
    >>> moneyformat(5)
    $5.00
    >>> moneyformat(1420.8823423)
    $1,420.88
    '''

    return "$" + "{:,.2f}".format(x)


def dtob(x):
    '''
    (int) -> str

    Returns int x formatted as binary string.
    If x is a floating point number, rounds to the nearest int before
    converting.

    Example:
    >>> dtob(13)
    1101
    '''

    if(isinstance(x, float)):
        x = int(x)

    return "{:b}".format(x)


def centerindashes(x):
    '''
    (num) -> string

    Returns a string formatted x, centered in 20 dashes.

    Example:
    >>> centerindashes(2984)
    --------2984--------
    '''

    return '{:-^20}'.format(x)


def test_formats(listoffunctions):
    '''
    () -> None

    Prints labeled output for all functions in this file for a variety
    of test cases.
    '''

    test_cases = (0, 1, -20, 0.0234, 39, 23.943, 9999999999)

    for function in listoffunctions:
        for case in test_cases:
            labelstring = function.__name__ + "(" + str(case) + ") = "
            labelstring = '{:<30}'.format(labelstring)
            print(labelstring, function(case), sep = '')

    return None


if __name__ == '__main__':
    functions_to_test = [moneyformat, dtob, centerindashes]
    test_formats(functions_to_test)

    
