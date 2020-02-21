# 210 Final Review Examples

# =============================================================================

# What is wrong with this function??
def rainfall(rainli):
    '''
    (list) -> float

    Returns the average monthly rainfall based on list of monthly
    rainfalls. Returns -999 if there are no valid (positive!) entries in
    the list.

    Examples:
    >>> rainfall([])
    -999
    >>> rainfall([5.5, 6.5, 6])
    6.0
    >>> rainfall([-1, -0.02, -9, -25])
    -999
    '''

    clean_data = [] # initialize

    if rainli == []:
        return -999

    for entry in rainli: # collect valid data
        if entry >= 0:
            clean_data.append(entry)

    # Correct way to catch empty list (safety net)
    # With these two lines then don't need 'if rainli == [] \ return -999'
    if len(clean_data) == 0:
           return -999

    average = sum(clean_data) / len(clean_data) # <-- would divided by empty li

    return average





# =============================================================================

# What's wrong with this function?
def remove_negatives(numlist):
    '''
    (list) -> None

    Removes any negative values from supplied list.

    Examples:
    >>> mylist = [9, 0, -21.43, 53.01, -8]
    >>> remove_negatives(mylist)
    >>> mylist
    [9, 0, 53.01]
    '''

    for i in range(len(numlist)):
        if numlist[i] < 0:
            numlist.remove(numlist[i])

    return None





def corrected_remove_negatives(numlist):
    '''
    (list) -> None

    Removes any negative values from supplied list.

    Examples:
    >>> mylist = [9, 0, -21.43, 53.01, -8]
    >>> corrected_remove_negatives(mylist)
    >>> mylist
    [9, 0, 53.01]
    '''

    for number in numlist:
        if number < 0:
            numlist.remove(number)

    return None





# =============================================================================

# Complete the following function, consistent with its docstring.
def list_split(alist, splitval):
    '''
    (list) -> list (of lists)

    Splits a list of integers into sublists, splitting on (and omitting) the
    second argument. Returns as list of all sublists.

    Examples:
    >>> list_split([4, 6, 5, 7, 4, 4, 9], 4)
    [[6, 5, 7], [9]]
    >>> list_split([])
    []
    >>> list_split([0, 0, 0], 0)
    []
    '''

    result = []
    currentrun = []

    for n in alist:
        if n == splitval:
            if len(currentrun) > 0:
                result.append(currentrun)
                currentrun = []
        else:
            currentrun.append(n)
    if len(currentrun) > 0:
        result.append(currentrun)

    return result

print('listsplit = ', list_split([4, 6, 4, 4, 5, 7, 4, 4, 5, 4, 89, 76], 4))






# =============================================================================
# PRACTICE PROBLEM #2
# Complete the following function, consistent with its docstring.
# Note that the function may reference the global variable SCRABBLE_POINTS
#   and that auxiliary functions may be created if they help organize and/or
#   simplfy your code.

SCRABBLE_POINTS = [[1, "eaionrtlsu"], [2, "dg"], [3, "bcmp"], [4, "fhvwy"], [5, "k"], [8, "jx"], [10, "qz"]]
def highest_score(wordlist):
    '''
    (list) -> string

    Finds and returns the string in wordlist with the highest Scrabble score,
    based on SCRABBLE_POINTS. Ties may be broken arbitrarily.

    Example:
    >>> highest_score(['onyx', 'wild', 'snake'])
    'onyx'
    '''

    best = ''
    high_score = 0
    
    for word in wordlist:
        score = 0
        for letter in word:
            score += value(letter)
        if score > high_score:
            high_score = score
            best = word

    return best






def value(letter):
    for pair in SCRABBLE_POINTS:
        if letter in pair[1]:
            return pair[0]

    print('Invalid Scrabble letter: ', letter)

    return None





# =============================================================================

# Let's make the scrabble code more efficient. Instead of searching a list for
#   letter values, let's put them all in a dictionary.
# Complete the function in accordance with it's docstring:

def unpack_table(letter_scores):
    '''
    (list) -> dictionary

    Converts a list of two-element lists into a dictionary in which the first
    element of each sublist becomes the value for each key, which are the
    individual letters in the string that is the second item of the sublist.

    Returns the dictionary.

    Example:
    >>> unpack_table([2, 'abc'], [3, 'def'])
    {'a': 2, 'b': 2, 'c': 2, 'd': 3, 'e': 3, 'f': 3}
    '''

    table = {} # initialize a dictionary
    for pair in letter_scores:
        value = pair[0]
        letters = pair[1]
        for letter in letters:
            table[letter] = value

    return table





# =============================================================================

'''
***NO GUARANTEE THAT THIS LIST IS COMPLETE***

FINAL TOPICS:
- Basic types:
    -> integer
    -> float
    -> string
    -> character
    -> boolean

- Python Collections:
    -> tuples
    -> lists
    -> dictionaries

- List/string methods, slice notation

- Mutability vs. Immutability
    -> implications for arguments passing and aliasing
    -> return values vs. side effects
    -> documentation (docstrings)
    -> scope and namespaces
    -> aliasing (pass-by-reference/assignment)

- Introspection Tools (note that these are all built-in functions)
    -> dir
    -> help
    -> id
    -> type

- Types of Errors
    -> syntax
    -> logical

- Recursion

- Iteration

- Files
    -> opening and closing
    -> reading, writing

- Reading From the Web
    -> urllib
    -> decode

- List Comprehensions

'''























