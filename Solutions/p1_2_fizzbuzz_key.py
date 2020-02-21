''' 
Fizzbuzz

CIS 210 F17 Project 1-2

Author: Solution

Credits: N/A

Play fizzbuzz game.
'''

def fb(n):
    '''(int) -> None

    Play fizzbuzz up to n.
    Results are printed during play;
    None value is returned

    >>> fizzbuzz(15)
    1
    2
    fizz
    4
    buzz
    fizz
    ...
    fizzbuzz
    '''
    for i in range(1, n+1):
        m3 = (i % 3) == 0
        m5 = (i % 5) == 0
        
        if m3 and m5:
            print('fizzbuzz')
        elif m3:
            print('fizz')
        elif m5:
            print('buzz')
        else:
            print(i)

    print('Game over!')

    return None

#fb(25)


    



