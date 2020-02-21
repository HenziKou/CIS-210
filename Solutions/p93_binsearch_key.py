"""
CIS210 Project 9 Part 3 Fall 2017 

Author: [Solution]

Credits: N/A

Check for the occurrence of a particular integer in
a sorted list, using a recursive and iterative
implementations of binary search. 

Practice:
-- binary search
-- recursion
-- testing
"""
import doctest
       
def isMemberR(seq, n):
    """(sequence, item) -> boolean

    Use binary search to check for membership
    of int n in sorted sequence, seq. Return 
    True if n is a member, else return False.

    >>> isMemberR((1, 2, 3, 3, 4), 4)
    True
    >>> isMemberR((1, 2, 3, 3, 4), 2)
    True
    >>> isMemberR('aeiou', 'i')
    True
    >>> isMemberR('aeiou', 'y')
    False
    >>> isMemberR((1, 3, 5, 7), 4)	    # even number of items in sequence - False
    False
    >>> isMemberR((23, 24, 25, 26, 27), 5)  # odd number of items in sequence - False
    False
    >>> isMemberR((0, 1, 4, 5, 6, 8), 4)    # even number of items in sequence - True
    True
    >>> isMemberR((0, 1, 2, 3, 4, 5, 6), 3) # odd number of items in sequence - True
    True
    >>> isMemberR((1, 3), 1)		    # target is first (zeroth) item in sequence
    True
    >>> isMemberR((2, 10), 10)		    # target is last item in sequence
    True
    >>> isMemberR((99, 100), 101)	    # short sequence - False
    False
    >>> isMemberR((42,), 42)		    # one item sequence - True
    True
    >>> isMemberR((43,), 44)		    # one item sequence - False
    False
    >>> isMemberR((), 99)		    # empty sequence
    False
    """
    if len(seq) == 0:
        return False
    else:
        mid = len(seq) // 2

        if seq[mid] == n:
            return True
        elif seq[mid] > n:
            return(isMemberR(seq[:mid], n))
        else:
            return(isMemberR(seq[mid+1:], n))			

def isMemberI(seq, n):
    """(sequence, item) -> boolean

    Use binary search to check for membership
    of int n in sorted sequence seq. Return True
    if n is a member, else return False.
    
    Note: seq is not maintained in its original
    form inside this function.

    >>> isMemberI((1, 2, 3, 3, 4), 4)
    True
    >>> isMemberI((1, 2, 3, 3, 4), 2)
    True
    >>> isMemberI('aeiou', 'i')
    True
    >>> isMemberI('aeiou', 'y')
    False
    >>> isMemberI((1, 3, 5, 7), 4)		# even number of items in sequence - False
    False
    >>> isMemberI((23, 24, 25, 26, 27), 5)	# odd number of items in sequence - False
    False
    >>> isMemberI((0, 1, 4, 5, 6, 8), 4)	# even number of items in sequence - True
    True
    >>> isMemberI((0, 1, 2, 3, 4, 5, 6), 3)	# odd number of items in sequence - True
    True
    >>> isMemberI((1, 3), 1)			# target is first (zeroth) item in sequence
    True
    >>> isMemberI((2, 10), 10)			# target is last item in sequence
    True
    >>> isMemberI((99, 100), 101)		# short sequence - False
    False
    >>> isMemberI((42,), 42)			# one item sequence - True
    True
    >>> isMemberI((43,), 44)			# one item sequence - False
    False
    >>> isMemberI((), 99)			# empty sequence
    False
    """
    if len(seq) == 0:
        return False

    while len(seq) > 0:
        mid = len(seq) // 2

        if seq[mid] == n:
            return True
        elif seq[mid] > n:
            seq = seq[:mid]
        else:
            seq = seq[mid+1:]

    return False

print(doctest.testmod())



