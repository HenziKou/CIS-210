# SCOPE RESOLUTION RULE - LEGB

#  L E G B
#  o n l u
#  c c o i
#  a l b l
#  l o a t
#    s l -
#    e   I
#    d   n


'''
LOOK AT CHAPTER 6 ABOUT NAMESPACES

>>> import os
>>> os.getcwd()
'C:\\Users\\Henzi\\Documents\\University of Oregon\\CIS 210\\Lab'
>>> os.chdir('Projects')
>>> import 'filename' as aName
'''

import random

def foo():
    '''
    Example function foo.
    '''

    print('in foo')

    return None

def bar():
    '''
    Example function bar.
    '''

    return 'in bar'

def main():
    '''
    '''

    foo()
    bar()

    return None

if __name__ == '__main__':
    main()
