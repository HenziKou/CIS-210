

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
        idxC1 = (consonantList.find(lastTwo[0]))
        idxC2 = str(idxC1 * 5)
    
        idxV1 = vowelList.find(lastTwo[1])
        idxV2 = str(idxV1 + (idxV1 % 5))
        

        pin = idxC2 + pin
        pin = idxV2 + pin
        
        return pin

        
    
        

        
