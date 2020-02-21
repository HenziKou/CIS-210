''' 
CIS 210 STYLE
CIS 210 F17 Project 1

Author: Henzi Kou

Credits: N/A

Add docstrings to Python functions implementing quiz 1 pseudocode.
'''

def q1(onTime, absent):
    '''
    Returns 3 different phrases depending on time of arrival:
        - If someone is on-time, then output is "Hello!"
        - If someone is absent, then output is "Is anyone there?"
        - If someone is late, then output is "Better late than never."
    None value is returned.
    '''
    
    if onTime:
        print('Hello!')
    elif absent:
        print('Is anyone there?')
    else:
        print('Better late than never.')

    return None

#q1(False, False)

def q2(age, salary):
    '''
    Returns the age of a person and their salary if their age is below 18 and
    their salary is below $10,000.
    '''
    return (age < 18) and (salary < 10000)

#print(q2(18, 5000))
#print(q2(16, 5000))

def q3():
    '''
    Returns 6 becuase the values of p=1 and q=2 do not satisfy the if statement
    of p < q nor does it satisfy the inequality of q > 4. Thus as a result
    the only statement that p and q can satisfy is the else statement. Anything
    entered into the defined funcion of q3() will result in an infinite loop
    with nothing displayed because it is not defined in the program.
    '''
    p = 1
    q = 2
    result = 4
    if p < q:
        if q > 4:
            result = 5
        else:
            result = 6

    return result

#print(q3())

def q4(balance, deposit):
    '''
    Prints out a statement giving the current balance of money with the
    addition of the amount being deposited into the account as well. Uses
    a count as a basket function to count the amount of money within the
    account.
    '''
    count = 0
    while count < 10:
        balance = balance + deposit
        count += 1

    return balance

#print(q4(100, 10))

def q5(nums):
    '''
    Given a list of numbers it will append the length of numbers to the i list.
    In doing so as the i list is expanding so does the result list.
    '''
    result = 0
    i = 0
    while i < len(nums):
        if nums[i] >= 0:
            result += 1

        i += 1

    return result

#print(q5([0, 1, 2, 3, 4, 5]))
#print(q5([0, -1, 2, -3, 4, -5]))

def q6():
    '''
    By commenting out the line "i = 1" this code prints out "2-power is,
    p," where p is any input that you input into q6(). If the line "i = 1"
    is left in the code then it will run an infinte loop where nothing is
    returned. The p-value is multiplied by two in order to get the new
    p-value when the i value is greater than 4.

    In addition the code keeps track of number of i times it has been ran.
    '''
    i = 0
    p = 1
    while i < 4:
        # i = 1 
        p = p * 2
        i += 1

    print('2-power is', p)
    return None


#q6()




    
    
     
        
    
