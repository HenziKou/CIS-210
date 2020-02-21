'''
Project 9.3 - Binary Search
CIS 210

Author: Henzi Kou
Credits: interactivepython.org

Design, implement, and test recursive and iterative algorithms for
determing sequence inclusion using binary search.
'''


import doctest



def isMemberR(aseq, target):
    '''
    (tuple, integer) -> Boolean

    A recursive function to implement a binary search algorithm to
    determine whether a given element is a member of a given sequence.
        - 'aseq' is a sorted sequence (tuple) of integers
        - 'target' is a non-negative integer

    Returns True if found, and False otherwise.

    Examples:
    >>> isMemberR((1, 2, 3, 4), 4)
    True
    >>> isMemberR('aeiou', 'i')
    True
    >>> isMemberR('aeiou', 'v')
    False
    >>> isMemberR((23, 24, 25, 26, 27), 5)
    False
    >>> isMemberR((), 99)
    False
    '''

    if len(aseq) == 0:
        return False
    else:
        mid = len(aseq) // 2

        if aseq[mid] == target:
            return True
        else:
            if target < aseq[mid]:
                return isMemberR(aseq[:mid], target)
            else:
                return isMemberR(aseq[mid + 1:], target)



def isMemberI(aseq, target):
    '''
    (tuple, integer) -> Boolean

    An iterative function to implement a binary search algorithm to
    determine whether a given element is a member of a given sequence.
        - 'aseq' is a sorted sequence (tuple) of integers
        - 'target' is a non-negative integer

    Returns True if found, and False otherwise.

    Examples:
    >>> isMemberI((1, 2, 3, 4), 4)
    True
    >>> isMemberI('aeiou', 'i')
    True
    >>> isMemberI('aeiou', 'v')
    False
    >>> isMemberI((23, 24, 25, 26, 27), 5)
    False
    >>> isMemberI((), 99)
    False
    '''
    
    first = 0
    last = len(aseq) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2
        if aseq[mid] == target:
            found = True
        else:
            if target < aseq[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found
            

print(doctest.testmod())



























