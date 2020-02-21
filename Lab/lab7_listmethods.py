# LIST METHODS AND COMMON BUGS
# Link to Python's list method documentation: https://docs.python.org/3/tutorial/datastructures.html
# That's all of them!
'''
Methods that return None, but modify the list:
append(x)           # append element x to end of list
insert(x, i)        # insert element x at index i
remove(x)           # remove element x from list (if it exists)
sort()              # sort elements in list (ascending)
extend(iterable)    # add all the elements from 'iterable' to end of list
clear()             # remove ALL elements from list
reverse()           # reverses order of list

Methods that return Something, AND modify the list:
pop(index)          # pop the element at index (removes from list AND returns element)


Methods that return Something, and DON'T modify the list:
slice syntax        # mylist[4:] <--- returns a copy of your list, from index 4 to the end
concatenation       # mylist + yourlist <---- returns a NEW list that is the concatenation of these lists
copy()              # returns a SHALLOW copy of the list
count(x)            # returns a count of number of occurences of item x in list             

'''



# List assignment to None function
# where we DON'T want the return value...

faveshows = ['spongebob', 'rugrats', 'avatar', 'rick and morty']

def shows_poll(showlist):
    '''
    (list) -> list

    Collect and return inputs from user about shows they watched.
    '''

    # THIS IS INCORRECT
    # WILL RETURN NONE B/C APPENDING TO A FUNCTION PARAMETER
    showlist = showlist.append('rocket power')
    #           ^^^^^^

    # CORRECT ANSWER
    # showlist.append('rocket power')
    
    answers = []

    for show in showlist:
        print('Did you watch ', show, '?')
        answer = input('y\n: ')
        answers.append(answer)

    return answer


# Calling functions that get ignored (return value unused)
# Where we DO want the return value

names = ['santa claus', 'tooth fairy', 'easter bunny']

def capitalize(namelist):
    '''
    (list) -> None

    Capitalize the letters in each string in namelist.
    '''

    # THIS IS WRONG WAY
    # for name in namelist:
    #    name = name.upper()

    for i in range(len(namelist)):
        namelist[i] = namelist[i].upper()

    return None




# Pass by reference!
# Example of object immutability / mutability in the context of user-defined
# functions.

STRING = 'I love'

def add_ladybugs(s):
    '''
    (str) -> str
    '''

    s = s + 'ladybugs'

    return s

LIST = ['bumblebees', 'grasshoppers', 'butterflies']

def append_ladybugs(alist):
    '''
    (list) -> list
    '''

    alist.append('ladybugs')

    return alist


# Print results
print('{: <24}'.format('STRING = '), STRING)
print('{: <24}'.format('add_ladybugs(STRING) = '), add_ladybugs(STRING))
print('{: <24}'.format('STRING = '), STRING)
print()
print('{: <24}'.format('LIST = '), LIST)
print('{: <24}'.format('append_ladybugs(LIST) = '), append_ladybugs(LIST))
print('{: <24}'.format('LIST = '), LIST)
