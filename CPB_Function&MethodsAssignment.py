import math
from collections import Counter

def vol(rad):
    '''calculates volume of sphere with given radius'''
    return 4/3*math.pi*rad**3
help(vol)
print(vol(2))
print("\n")

def ran_check(num,low,high):
    ''' checks if # in given range inclusive of high & low, prints statement '''
    if low<num<high:
        print(f'{num} is range of {low} & {high}')
    else:
        print(f'{num} is not in range of {low} & {high}')
def ran_bool(num,low,high):
    ''' checks if # in given range inclusive of high & low, returns boolean '''
    return low<num<high
help(ran_check)
help(ran_bool)
ran_check(5,2,9)
print(ran_bool(5,2,9))
ran_check(1,2,9)
print(ran_bool(1,2,9))
print("\n")

def up_low(string):
    '''returns number of both uppercase and lowercase letters'''
    count_upper = 0
    count_lower = 0
    for letter in string:
        if letter.isupper():
            count_upper +=1
        elif letter.islower():
            count_lower +=1
    print(f'There are {count_upper} uppercase letters and {count_lower} lowercase letters in this string.')
    return list([count_upper,count_lower])
    #u = Counter(string.isupper())
    #l = Counter(string.islower())
    #return u and l

u = up_low('a StRiNg to cOUnt Upper and lower')
print(u)
print("\n")

def unique_list(l):
    ''' takes in a list and returns only unique elements of list '''
    return list(set(l))

print(unique_list([1,1,1,1,1,2,2,3,3,3,3,3,3,3,7,8,9,10,10]))
print("\n")

def mulitply(num):
    n = 1
    for x in num:
        n = n*x
    return n
print(mulitply([1,2,3,4,5,6,100]))
print("\n")

def palindrome(s):
    '''detects if string is palindrome (sam front to back)'''
    string = ' '.join(list([x for x in s if x != ' ']))
    reverse = string[::-1]
    return string == reverse

print(palindrome('racecar'))
print(palindrome('nurses run'))
print(palindrome('racecars'))
print(palindrome('abcdecba'))
print("\n")

import string
def ispangrams(string, alphabet=string.ascii_lowercase):
    '''detects if string is pangram (contains every letter of the alphabet)'''
    #string = string.lower()
    #print(string)
    s = list(set([x for x in string.lower() if x != ' ']))
    s.sort()
    alphabet = list(alphabet)
    return s == alphabet

print(ispangrams("The quick brown fox jumps over the lazy dog"))
print("\n")


