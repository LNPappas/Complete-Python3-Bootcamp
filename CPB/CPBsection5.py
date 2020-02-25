#Statements
print("Control Flow: execute certain code when particular condition met.")
print("If Elif and Else statements:")
print("if statement syntax: \n if some_condition \n \t #otherwise_do_this")
print("if else statement syntax: \n if some_condition: \n \t #execute_some_code \n else: \n\t #otherwise_do_this")
print("if elif else statement syntax: \n if some_condition: \n\t #execute_some_code") 
print(" elif some_condition: \n\t #execute_other_code \n else: \n\t  #otherwise_do_this")

print('\n')

print("name = 'Lauren'")
print('if name == "Lauren": \n\t print("Hi Lauren")')
print('else: \n\t print("What is your name?")')
    
print('\n')
name = 'Lauren'
if name == 'Lauren':
    print("Hi Lauren")
else:
    print("What is your name?")

print("\n")

#For Loops
print("Iterable: can iterate (perform an action) over every element in the object")
print("for loops operate a block of code for every iteration")

print("mylist = [1,2,3]")
print("for item in mylist: \n    print(item)")

mylist = [1,2,3]
for item in mylist:
    print(item)
print("\n")
print("for num in mylist: \n\tif num %2 == 0: \n\t\tprint(num)")

for num in mylist:
    if num %2 == 0:
        print(num)
print("\n")
print("sum = 0")
print("for num in mylist: \n\tsum = sum + num")
print("print(sum)")

sum = 0
for num in mylist:
    sum = sum + num
print(sum)
print("\n")

print("set variable to _ if don't intent to use")    
print('for _ in mylist: \n\tprint("Cool!")')
for _ in mylist:
    print("Cool!")
print("\n")
print("tuble unpacking:")
print("newlist = [(1,2),(3,4),(5,6)]")
newlist = [(1,2),(3,4),(5,6)]
print("len(newlist) =", len(newlist))
print("for a,b in newlist: \n\tprint(a) \n\tprint(b)")
for a,b in newlist:
    print(a)
    print(b)
print("\n")
print("for a,b in newlist: \n\tprint(b)")
for a,b in newlist:
    print(b)
print("\n")
d = {'k1':1, 'k2':2, 'k3':3}
print("when you iterate through a dictionary you only iterate though the keys.")
for item in d:
    print(item)
print("to iterate through everything use d.items() for dictionary d")
for item in d.items():
    print(item)
print("to print out just the values think of a dictionary like a tuple:")
print("for key,value in d:\n\tprint(value)")
for key, value in d:
    print(value)

print("\n")
#While Loops
print("While loops: while some condition remains true: do this ")
print("make sure condition changes or infinite loop")
print("x=0")
print("while x<0:\n\tprint(f'the current value of x is{x}'\n\tx=x+1)")

x=0 
while x<5:
    print(f'the current value of x is {x}')
    x = x+1
print("else: \n\tprint('x is 5')")
x=0 
while x<5:
    print(f'the current value of x is {x}')
    x = x+1 #equivalent: x +=1
else:
    print("x is 5")

#pass does nothing, use as a place holder to avoid syntax error
x = [1,2,3]
for item in x:
    pass

#continue goes to the top of a continuing loop
mystring ='Sammy'
for letter in mystring:
    if letter == 'a':
        continue
    print(letter)
print("\n")
#break exits a loop.
mystring ='Sammy'
for letter in mystring:
    if letter == 'a':
        break
    print(letter)
x=0
while x<5:
    if x==2:
        break
    print(x)
    x += 1

print("\n")

#useful operators:

#range() function for iterations
mylist = [1,2,3]
for num in range(10): #up to not including 10
    print(num) 
print("\n")
for num in range(3,10): #starting with 3
    print(num)
print("\n")
for num in range(3,10,2): #step size 2
    print(num)
print("\n")

mylist = list(range(0,11,2))
print(mylist)
print("\n")

index = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index, letter))
    index +=1
print("\n")

index = 0
word ='abcde'
for letter in word:
    print('At index', index, 'the letter is ', word[index])
    index +=1
print("\n")

index = 0
for item in enumerate(word):
    print(item)
print("\n")

index = 0
for index,letter in enumerate(word):
    print(index)
    print(letter)
    index = 0
index = 0
for item in enumerate(word):
    print(item)
print("\n")
#enumerate function    
for item in enumerate(word):
    print(item)
    print("\n")

#zip function, can only zip together up to shortest list, can do any number of lists
mylist1 = [1,2,3]
mylist2 = ['a','b','c']
for item in zip(mylist1,mylist2):
    print(item)
print("\n")
mylist3 = [1.0,2.0,3.0]
l = list(zip(mylist1,mylist3,mylist2))
print(l)
print("\n")

#in key word
print('a' in l)
print('a' in mylist2)
print('a' in "a world")
d={'mykey':value}
print('mykey' in d)
print("\n")

#min and max are key words
print(min(mylist1))
print(max(mylist1))

#can import from libraries alread in python
from random import shuffle
shuffle(mylist2) #inplace function (cannot save to variable)
print(mylist2)

from random import randint
z = randint(0,100)
print(z)
print("\n")

#user input function:
num = input('Enter a number here: ') #input excepts anything as string so cast.
print(num)
print(type(num))
num = int(input('Enter a number here: '))
print(num)
print(type(num))
num = float(input('Enter a number here: '))
print(num)
print(type(num))

#list comprehentions

mystring = 'hello'
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)

mylist2 = [letter for letter in mystring]
mylist2.reverse()
mystring2 = ''.join(mylist2)
print(mystring[::-1])
print(mystring2)
print("\n")
numlist = [num for num in range(0,11)]
numlist1 = [num**2 for num in range(0,11) if num%2 == 0]
print(numlist)
print(numlist1)
celcius = [num for num in range(10,101,10)]
print(celcius)
fahrenheit = [((9/5)*temp +32) for temp in celcius]
print(fahrenheit)

#one liners for if else statements in list comprehention
results = [x if x%2 == 0 else 'ODD' for x in range(0,11)]
print(results)
print("\n")


#nested loop
mylist = []
for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)
print(mylist)
mylist2 = [x*y for x in [2,4,6] for y in [100,200,300]]
print(mylist2)
print("\n")


#test
st = 'print words that only start with the letter s or S in this Sentance'
for word in st.split():
    if word[0].lower() == 's':
        print(word)
print("\n")
for word in st.split():
    if word[0] == 's' or word[0] == 'S':
        print(word)

#print all even numbers from 0 to 10 using range()
print("\n")
mylist = list(range(0,11,2))
print(mylist)
for num in range(0,11,2):
    print(num)

#use list comprehension to create a list of all numbers from 1 to 50 divisable by 3
mylist = [num for num in range(0,51) if num%3==0]
print(mylist)
print("\n")

#if length of word in string below is even print "even!"
st = 'Print every word in this sentence that is an even number of letters'
for word in st.split():
    if len(word)%2==0:
        print(word, ' even!')
print("\n")

#print integers from 1 to 50 but if mulitple of 3 print fizz if multiple of 5 print buzz
#and if multiple of 3 and 5 print fizzbuzz
mylist = [num for num in range(1,51)]
for num in mylist:
    if num%3==0 and num%5==0:
        print('FizzBuzz')
    elif num%3==0:
        print('Fizz')
    elif num%5==0:
        print('Buzz')
    else:
        print(num)
print("\n")

#use list comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
mylist = [x[0] for x in st.split()]
print(mylist)
print("\n")

