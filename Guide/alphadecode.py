

def alphapinDecode_stub (word):
    

def alphapinDecode (word):
    """
Str -> int
Given a alphacode, converts this alphacode back
into the orgional pin number.
Returns Pin
>>> alphapinDecode('lohi')
4327
"""
    i = 0
    pin = ''
    vowelList = 'aeiou'
    consonantList = 'bcdfghijklmnpqrstvwyz'
    for i in range(0, len(word), 2):
        lastTwo = word [i:i+2]
 #       consonant = lastTwo[0]
        idxC = str(consonantList.find(lastTwo[0]))
        
        idxV = str(vowelList.find(lastTwo[1]))
        print (lastTwo)
        pin = idxC + pin
        pin = idxV + pin

        print (pin)
        

        
        
    
        

        
