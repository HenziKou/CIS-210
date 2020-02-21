'''
Exploring ciphers.
CIS 210 F17 Project 4-1.

Author: [Solution]

Credits:  N/A

Encrypt and decrypt a message
using substitution cipher algorithm.

Credits: text, ch. 3

Practice with:
-software development - understand algorithm, revise code
-software development - program with multiple functions
-cipher algorithm
-string data type/operations
-doctest module
'''
import doctest

def removeMatches(myStr, removeStr):
    '''(str, str) -> str

    create a new string which is myStr
    with all occurrences of characters
    in removeStr removed.  Return the
    new string. (text p. 107)

    >>> removeMatches('abcdefghi', 'ceg')
    'abdfhi'
    '''
    newStr = ''
    for ch in myStr:
        if ch not in removeStr:
            newStr += ch
            
    return newStr

def removeMatches2(myStr, removeStr):
    '''
    another way to implement
    same functionality as removeMatches
    '''
    newStr = myStr
    for ch in removeStr:
        newStr = newStr.replace(ch, '')
    return newStr

def removeDupes(myStr):
    '''(str) -> str

    Create a new string which is
    myStr with all duplicate chars
    removed.  Return the new string.
    (text p. 106)

    >>> removeDupes('aaabbbccc')
    'abc'
    >>> removeDupes('')
    ''
    >>> removeDupes('the quick brown fox')
    'the quickbrownfx'
    '''
    newStr = ''
    for ch in myStr:
        if ch not in newStr:
            newStr += ch

    return newStr

#''.join(set('aaabbbccc'))

def genKeyFromPass(psw):
    '''(str) -> str

    Use psw to generate a scrambled
    alphabet cipher key, which is
    returned (text p. 107, revised
    for style)

    Calls: removeDups, removeMatches

    >>> genKeyFromPass('ajax')
    'ajxyzbcdefghiklmnopqrstuvw'
    >>> genKeyFromPass('topsecret')
    'topsecruvwxyzabdfghijklmnq'
    '''
    key = 'abcdefghijklmnopqrstuvwxyz'

    #clean up the psw
    keyPsw = removeDupes(psw)

    #determine position of last ch
    #to be removed from key
    lastCh = keyPsw[-1]
    lastIdx = key.find(lastCh)

    #use this to split the key
    beforeStr = key[:lastIdx]
    afterStr = key[lastIdx+1:]

    #remove psw chars from head and tail keys
    beforeStr = removeMatches(beforeStr, keyPsw)
    afterStr = removeMatches(afterStr, keyPsw)

    #now form the new key
    return keyPsw + afterStr + beforeStr

def subEncrypt(plainText, psw):
    '''(str, str) -> str

    Use substitution cipher, with a key
    generated from psw, to encrypt plainText.
    Encrypted string eText is returned.
    (text p. 102, revised to remove spaces
    from plainText and to generate the
    substitution key from psw)

    Calls:  removeMatches, genKeyFromPass

    >>> subEncrypt('the quick brown fox', 'ajax')
    'qdznrexgjoltkblu'

    '''
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

    #clean up plain text
    plainText = plainText.lower()
    plainText = removeMatches(plainText, ' ')

    #generate the key
    key = genKeyFromPass(psw)

    #and use it to create encrypted text
    cipherText = ''

    for ch in plainText:
        idx = ALPHABET.find(ch)

        #ignore non-alpha-chars (in case there are any)
        #could also include them in argument when
        #removeMatches is called - just spaces now
        
        if idx != -1:
            cipherText += key[idx]

    return cipherText

def subDecrypt(cipherText, psw):
    '''(str, str) -> str

    Substitution cipher decrypt,
    for cipherText, with key generated
    by psw (which was also used
    to encrypt the original plaintext).
    Original spaces and other non-alpha
    characters (if any) are not recovered.

    Calls:  genKeyFromPass

    >>> subDecrypt('qdznrexgjoltkblu', 'ajax')
    'thequickbrownfox'
    '''
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    cipherText = cipherText.lower() #just in case
    
    key = genKeyFromPass(psw)
    
    plainText = ''

    for ch in cipherText:
        idx = key.find(ch)
        plainText += ALPHABET[idx]

    return plainText


def main():
    '''
    main function for checking encrypt/decrypt functions
    '''
    p1 = input('Enter a string to encrypt: ')
    password = input('Please enter a password: ')
    
    e = subEncrypt(p1, password)
    print('The encrypted string is:', e)
    p2 = subDecrypt(e, password)
    print('The decrypted string is:', p2)
    
    return None

'''    
if __name__ == '__main__':
    main()
'''

        
