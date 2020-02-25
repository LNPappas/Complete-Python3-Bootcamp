#Methods: functions built into objects
mylist = [1,2,3]
print(mylist)
mylist.append(4)
print(mylist)
mylist.pop()
print(mylist)
mylist.pop(0)
print(mylist)
help(mylist.insert)
mylist.insert(0,8)
print(mylist)

#functions: create blocks of code that can be easily used at anytime

def funName(nameparameter='defaultName'):
    '''
    docstring explaining the function (returns name input in reverse)
    help(funName) will return this info.
    '''
    print('code for whatever the function does ', nameparameter)
    return nameparameter[::-1]
result = funName()
print(result)
name = 'Lauren'
print(name)
result = funName(name)
print(result)
help(funName)

def add(n1=0,n2=0):
    return n1+n2
print(add())
print(add(2,5))

#Find if word dog is in a string with a function:

def dogcheck(mystring = ''):
    '''
    checks if dog is in string, returns boolean
    '''
    return 'dog' in mystring.lower()

print(dogcheck('dog is in this string'))
print(dogcheck('it is not in this string'))

#pig_latin: if word starts with vowel add ay to end
#           else put first letter at end then add ay

def pig_latin(word='blank'):
    '''
    if word starts with vowel add ay to end
    else put first letter at end then add ay
    default word is 'blank'
    '''
    first_letter = word[0]
    #check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + word[0] + 'ay'
    return pig_word

print(pig_latin())
print(pig_latin('word'))
print(pig_latin('apple'))

def myfunc(a,b):
    '''
    returns 5% of the sum of a and b
    '''
    return sum((a,b))*0.05

x = myfunc(40,60)
print(x)
print(type(x))

#takes args as tuples (unlimited number)
def myfunc(*args):
    print(type(args))
    return sum(args)*0.05
#can technically use *anything but args is conventionalde
print(myfunc(1,2,3,4,50))
print("\n")

#use **kwargs to turn function input into a dictionary
def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}.'.format(kwargs['fruit']))
    else:
        print("No fruit here.")

myfunc(fruit='apple', veggie='lettuce')
myfunc(veggie='lettuce', nut='almond')

print("\n")

def myfunc(*args,**kwargs):
    print('I would like {} {}'.format(args[0],kwargs['food']))

myfunc(10,20,30, fruit='orange', food='cheeeseburgers')

def myfunc(*args,**kwargs):
    print(f'I would like {args[1]} {kwargs["food"]}')

myfunc(1,2,3, fruit='orange', food='cheeeseburgers')
print("\n")

#map() function: can map a function to a list, iterating through the list and applying it to the function
def square(num):
    return num**2
nums = [i for i in range(0,6)]
for item in map(square,nums):
    print(item)

print(list(map(square, nums))) #pass in function itself as an arugument, not square()

#filter() function: filter by a function that returns true or false
def check_even(num):
    return num%2 == 0

print(list(filter(check_even, nums)))
print("\n")

#lambda expressions
def square(num): return num**2 #original function on one line

square = lambda num: num**2 #assigned to square but normally don't assign lambdas
print(square(5))

print(list(map(lambda num:num**2, nums)))
print(list(filter(lambda num:num%2==0, nums)))
names = ['Evie', 'Evan']
print(list(map(lambda x:x[0],names)))
print(list(map(lambda x:x[::-1],names)))
print("\n")

#nested statements and scope
x=25
def printer():
    x = 50
    return x
print(x)
print(printer())
'''
LEGB Rule:
Local
Enclosing function locals
Global
Built-in
'''
print(name)
def greet():
    name = 'enclosing' #enclosing function
    print(name)
    def hello():
        name = 'local' #local function, only effects function not higher scope outside unless name is global
        print('Hello '+name)
    hello()
greet()
print(name)

''' 
examples of built in functions are len() or print()
you can call help() on built in functions
'''

print("\n")

