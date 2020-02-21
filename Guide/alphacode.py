'''
Memorable Pins. Project 3, Part 2. CIS 210
Author: Quinn Milionis
Credits: Bradley N. Mililer and David L. Ranum
given a pin number of any length, will generate
an easy to pronounce word.
'''

def alphapinEncode_stub (pin):
    """
int -> str
given a pin number, returns an easily pronouncable
word.
returns word
>>> alphapinEncode(4327)
'lohi'
    
"""  
    pass
    #return word

def alphapinEncode (pin):
    """
int -> str
given a pin number, returns an easily pronouncable
word.
returns word
>>> alphapinEncode(4327)
'lohi'

"""
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwyz'
    word = ''
    while pin > 0:
        lastTwo = pin % 100
        #print (lastTwo)
        pin = pin // 100

        word = (vowels [lastTwo % 5]) + word 
        word = (consonants [lastTwo // 5]) + word

    return word



    

        
        
        

        
        

    
    
    
        
