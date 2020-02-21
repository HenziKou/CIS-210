'''
Binary Search. Project 6 Part 1.
Author: Quinn Milionis
Credits: Otton Lara
Two binary search funcitons, one using
recursion and one using iteration.
'''

def is_memberR(alist, target):
    """
list, str -> boolean
using recursion, performs a binary
search on alist for target.
returns True if found, and False
if not.
>>> is_memberR([1,2,3,4], 3)
True
>>> is_memberR([1,2,3,4], 5)
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
>>> is_memberI([1,2,3,4], 3)
True
>>> is_memberI([1,2,3,4], 5)
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

