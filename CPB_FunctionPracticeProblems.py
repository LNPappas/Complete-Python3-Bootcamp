#lesser of two evens

def lesser_of_two_evens(x,y):
    '''
    This function returns the lowest number if both numbers are even
    otherwise it returns the highest number.
    '''
    if x%2==0 and y%2 ==0:
        return min(x,y)
    else:
        return max(x,y)

print(lesser_of_two_evens(2,8))
print(lesser_of_two_evens(2,7))
print(lesser_of_two_evens(2,0))
print(lesser_of_two_evens(3,8))
print("\n")

#
def animal_crackers(string):
    '''
    this function takes a string and returns True 
    if all words begin with the same letter
    '''
    mylist = string.split()
    return mylist[0][0] == mylist[1][0]

print(animal_crackers('apple Adam'))
print(animal_crackers('apple ape'))
print(animal_crackers('Banana Rama'))
print("\n")

#Makes Twenty:
def makes_twenty(a,b):
    '''
    return True if sum of integers is 20 or one of integers is 20
    else return False
    '''
    return a == 20 or b == 20 or a+b == 20

print(makes_twenty(10,10))
print(makes_twenty(10,5))
print(makes_twenty(10,20))
print(makes_twenty(20,10))

#Old Macdonald:
def old_macdonald(name):
    '''
    capitalize first and 4th letters of a name
    '''
    return name[0:3].capitalize() + name[3:].capitalize()

print(old_macdonald('James'))
print(old_macdonald('james'))
print(old_macdonald('evan'))
print("\n")
#Master Yoda
def master_yoda(string):
    '''
    returns sentence with words in reverse
    '''
    return ' '.join(string.split()[::-1])

print(master_yoda('write this backwards'))
print(master_yoda('this too'))
print("\n")

#Almost There
def almost_there(n):
    '''
    return true if n is within 10 of 100 or 200
    '''
    return 89<n<111 or 189<n<211

print(almost_there(5))
print(almost_there(97))
print(almost_there(90))
print(almost_there(110))
print(almost_there(109))
print(almost_there(197))
print(almost_there(190))
print(almost_there(97))
print(almost_there(90))
print(almost_there(110))
print(almost_there(150))
print(almost_there(210))
print(almost_there(209))
print("\n")

#Find 33
def has_33(mylist):
    '''
    return true if list has two consecutive 3's
    '''
    y = 0
    for x in mylist:
        if y+1 < len(mylist):
            z = mylist[y+1]
            y +=1
            if x == 3 and z == 3:
                return True
        else:
            return False

def has_33(nums):
    for i in range(0, len(nums)-1):
        if nums[i:i+2] == [3,3]:
            return True  
    return False

print(has_33([1,2,3,3,4,5]))
print(has_33([1,2,3,4,5]))
print(has_33([1,2,3,4,5,3]))
print("\n")

#Paper Doll
def paper_doll(string):
    '''
    return a string that tripples each letter of original string
    '''
    newstring = ''
    for letter in string:
        newstring = newstring + letter*3
    return newstring

print(paper_doll('hello'))
print(paper_doll('Mississippi'))
print("\n")

#Blackjack
def blackjack(x,y,z):
    '''
    input 3 int. If sum <= 21, return sum.
    if sum > 21 but has 11 return sum - 10
    else return bust
    '''
    if sum((x,y,z)) <= 21:
        return sum((x,y,z))
    else:
        if 11 in (x,y,z) and sum((x,y,z)) <= 31:
            return sum((x,y,z)) - 10
        else:
            return 'BUST'

print(blackjack(1,2,3))
print(blackjack(11,10,3))
print(blackjack(9,9,9))
print("\n")

#Summer Of '69
def summer_69(mylist=0):
    '''
    return sum of array except ignore sections that start
    at 6 up to and including the next 9
    Return 0 for no numbers
    '''
    new_list = []
    i=0;
    while i < len(mylist):
        if mylist[i] == 6:
            while i < len(mylist):
                i+=1
                if mylist[i] == 9:
                    i+=1
                    break
        else:
            new_list.append(mylist[i])
            i+=1
    return new_list

print(summer_69([2,3,4,5,6,7,8,9,10]))
print(summer_69([2,3,4,5,6,9,10,16,19]))
print(summer_69([0,1,2,3,4,5]))
        
#Spy Game
def spy_game(mylist=[]):
    '''
    take list of integers
    returns True if list contains 007 in order
    '''
    for index, num in enumerate(mylist):
        if num == 7:
            if mylist[index+1] == 0:
                if mylist[index+2] == 0:
                    return True
    return False

def spy_game(nums):
    '''
    alt solution for spy_games()
    '''
    code = [0,0,7,'x']    
    for num in nums:
        if num == code[0]:
            code.pop(0)   # code.remove(num) also works      
    return len(code) == 1

print(spy_game([0,1,2,3,4,5]))
print(spy_game([0,1,7,0,0,5]))
print(spy_game([0,7,0,3,0,5]))
print(spy_game([0,7,2,3,4,0]))

#Count Primes
def count_primes(num):
    '''
    this function returns any primes that exist
    up to and including the given #
    '''
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:  # use the primes list!
            if x%y == 0:
                x += 2
                break
            else:
                primes.append(x)
                x += 2
    print(primes)
    return len(primes)

print(count_primes(3))
print(count_primes(1))
print(count_primes(7))
print(count_primes(11))
print(count_primes(25))
print(count_primes(500))

#PRINT BIG
def print_big(letter):
    '''
    takes a single letter and returns 5x5 represntation
    '''
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])
print(print_big('a'))
print(print_big('b'))
print(print_big('c'))
print(print_big('d'))
print(print_big('e'))