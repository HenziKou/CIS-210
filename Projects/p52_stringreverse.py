'''
Project 5.2: Number Conversions Revisited
    "String Reversal"
CIS 210

Author: Henzi Kou
Credits:          <--- REMEMBER TO FILL IN

Write and implement iterative and recursive algorithms to reverse a string.
    Practice with:
        - Systematic testing functions
        - Recursion functions/algorithms
'''

import doctest



def strReverseR(s):
    '''
    (str) -> str
    
    The function takes a single string argument, s, and then returns the
    reverse of the argument.
        - This is a recursive implementation.

    Examples:
    >>> strReverseR('hello world')
    'dlrow olleh'
    >>> strReverseR('woohoo i got it')
    'ti tog i oohoow'
    '''

    if s == "":
        return s
    else:
        return strReverseR(s[1:]) + s[0]

    return None



def strReverseI(s):
    '''
    (str) -> str

    The function takes a single string argument, s, and then returns the
    reverse of the argument.
        - This is an iterative implementation of the string reverse algorithm.

    Examples:
    >>> strReverseI('dlrow olleh')
    'hello world'
    >>> strReverseI('ti tog i oohoow')
    'woohoo i got it'
    '''

    new_str = ''
    i = len(s)

    while i > 0:
        new_str += s[i - 1]
        i -= 1

    return new_str



# EXTRA CREDIT
def hailstone(n):
    '''
    (int) -> float

    A recursive functiion which prints the hailstone sequence beginning
    at n. Function stops when the sequence reaches 1.
        - If n is even, the next number in the sequence is n/2
        - If n is odd, the next number in the sequence is 3*n+1

    Example:
    >>> hailstone(10)
    10
    5.0
    16.0
    8.0
    4.0
    2.0
    1.0
    7
    '''

    count = 1
    assert n > 0
    print(n)

    if n > 1:
        if n % 2 == 0:
            count += hailstone(n / 2)
        else:
            count += hailstone((n * 3) + 1)

    return count


    
def main():
    '''
    () -> None

    Executes the functions: 'strReverseR' and 'strReverseI'.

    Allows user to input additional string.
    '''

    prompt = input("Type a string to test: ")
    
    recur = strReverseR(prompt)
    print('Using a recursive formula, the reverse string of your',
          'input is:\n {}'.format(recur))

    i = strReverseI(recur)
    print('Going back to the original string with an iterative',
          'formula it is:\n {}'.format(i))

    prompt_2 = int(input("Input number of hailstones to calculate: "))
    num = hailstone(prompt_2)
    print('The length of hailstones is:\n {}'.format(num))
    
    return None


print(doctest.testmod())

if __name__ == '__main__':
    main()





# EXTRA CREDIT
'''
If n is even, the next number in the sequence is n/2. If n is odd, the next
number in the sequence is (3 * n) + 1. Repeating this process, we generate
the hailstone sequence.

Write a recursive function 'hailstone(n)' which prints the hailstone sequence
beginning at n. Stop when the sequence reaches the number 1 (otherwise, we
would loop forever 1, 4, 2, 1, 4, 2,...). For example, when n = 5, your
program should output the following sequence:

5
16
8
4
2
1

Every hailstone sequence reaches 1 eventually, no matter what value of n we
start with.
'''














