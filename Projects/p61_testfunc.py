'''
Project 6.1: Testing Functions
    "Automated Testing"

CIS 210

Author: Henzi Kou
Credits: N/A

Function that tests other string reverse functions.
    Practice with:
        - Software development (i.e. testing)
        - Functions as parameters
'''


import p52_stringreverse as p5


def test_reverse(f):
    '''
    (function) -> None

    Prints labeled output for all functions in this file for a variety
    of test cases.

    Example:
    >>>
    ...
    '''

    test_cases = (('', ''), ('a', 'a'), ('xyz', 'zyx'),
                    ('testing123', '321gnitset'),
                    ('hello, world', 'dlrow ,olleh'))
    
    for function in f:
        for case in test_cases:
            labelstring = 'Checking' + '(' + str(case[0]) + ') ... '
            labelstring = '{:<30}'.format(labelstring)
            result = "'" + function(str(case[0])) + "',"
            expect = "'" + str(case[1]) + "'."

            if function(str(case[0])) == str(case[1]):
                print(labelstring, 'its value', result, 'is correct!')
            else:
                print(labelstring, 'Error: has wrong value', result,
                      'expected ', expect)
        return None
                
    return None




def main():
    '''
    Calls string reverse test function 2x.
        - 'test_reverse(function 1)'
        - 'test_reverse(function 2)'
    '''

    functions_to_test = [p5.strReverseR, p5.strReverseI]
    test_reverse(functions_to_test)

    return None



if __name__ == '__main__':
    main()



# EXTRA CREDIT

def isMember(alist, target):
    '''
    (list, int) -> boolean

    Determines whether a target value is in a sequence that may contain
    nested sequences using a recursive method.

    Example:
    >>> isMember([1, [2, [3], 4], [5, 6]], 3)
    True
    '''

    isinstance(alist, str)
    isinstance(target, int)

    if len(alist) == 0:
        return False
    else:
        mid = len(alist) // 2
        if alist[mid] == target:
            return True
        else:
            if target < len(alist[mid]):
                return isMember(alist[:mid], target)
            else:
                return isMember(alist[mid + 1:], target)

    return None
    






    


