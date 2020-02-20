''' 
CIS 210
CIS 210 FizzBuzz Revisited

Author: Henzi Kou

Credits: N/A
'''


def fb(n):
    '''
    With this code, inputing any integer for n into fb(n) will return either:
    'Fizz' if the number is a multiple of 3, or 'Buzz' if the number is a
    multiple of 5, or if the number is a multiple of both 3 and then the code
    will return 'FizzBuzz' as a response. Meanwhile entering 'n' will end the
    FizzBuzz game.
    '''
        
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)
    
