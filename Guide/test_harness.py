'''
Function Testing. Project 7, Part 1.
Author: Quinn Milionis
Credits: None
Automates the testing of
two binary search funcitons. 
'''

import doctest



def is_memberR(alist, target):
    """
list, str -> boolean
using recursion, performs a binary
search on alist for target.
returns True if found, and False
if not.
>>> is_memberR([1,2,3,4],3)
True
>>> is_memberR([1,2,3,4],5)
False
"""
    if len(alist) == 0:
        
        return False
    else:
        mid = len(alist)//2  
        if alist [mid] == target:
            return True
        else:
            if target < alist[mid]:
                return is_memberR (alist[:mid],target)
            else:
                return is_memberR (alist[mid+1:],target)



def is_memberI (alist, target):
    """
list, str -> boolean
using iteration, performs a binary
search on alist for target.
returns True if found, and False
if not.
>>> is_memberI([1,2,3,4],3)
True
>>> is_memberI([1,2,3,4],5)
False
"""
    left = 0
    right = len(alist) -1
    while left <= right:
        mid = (left + right) // 2
        if alist[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

        if left >= 0 and left < len (alist) and alist [left] == target:
            return True
    return False

def test_is_member (f):
    """
function -> boolean
Given f, the function to test, tests either
is_memberR or is_memberI with a variety of
test cases, returning True if the funciton
passes the tests, and prints the failed
test case otherwise and returns False
>>> test_is_member (is_memberI)
True
>>> test_is_member (is_memberR)
True
"""
    if f([1, 3, 5, 7], 4)!= False:
        print ('Error when even number of item in list - False')
        return False
    if f([23, 24, 25, 26, 27], 5) != False:
        print ('Error when odd number of items in list - False')
        return False
    if f([0, 1, 4, 5, 6, 8], 4) != True:
        print ('Error when even number of items in list - True')
        return False
    if f([0, 1, 2, 3, 4, 5, 6], 3) != True:
        print('Error when odd number of items in list - True')
        return False
    if f([1, 3], 1) != True:
        print ('Error when target is first item in the list')
        return False
    if f([2, 10], 10) != True:
        print ('Error when target is last item in the list')
        return False
    if f([99, 100], 101) != False:
        print ('Error in short list - False')
        return False
    if f([42], 42) != True:
        print ('Error when single item list - True')
        return False
    if f([43], 44) != False:
        print ('Error when single item list - False')
        return False
    if f([],99) != False:
        print ('Error when empiy list')
        return False

    else:
        return True
        
         
    
    

print(doctest.testmod())










