print("Hello World!")
print("\n")

# Data Types
print("Integers: 3, 300, -200")
print("Float: 2.3 100.0")
print('Strings" "charaters in quotes"')
print('Lists: [10, "hello", 200.3] <- any data type (objects) in List')
print('Dictionaries: {"key":"value", "name":"Charlie"}')
print('Tuples: (10,"hello",200.3) <- ordered immutable objects')
print('Sets: ("a","b") <- unordered objects')
print('Booleans: True or False <- logical values')

#Notes: Python3 performs true division by default
print("\n")

#Numbers
print("Numbers are Integers and Floats")
print("Addition: 2+2 =4")
print("Subtraction: 4-2 =2")
print("Multiplication: 2*3 =6")
print("Division: 4/2 =2")
print("Powers: 2**3 =8")
print("Roots: 4**0.5 = square root of 4 = 2")
print("Floor Division: 3//2 =1")
print("Modulous/Remainder: 7%3 =4")
print("Python follows order of opperations: 2+10*10+3 =105")
print("\n")

#Variables
print("most variables are in lowercase")
print("global variables ALL CAPS")
print("Python uses Dynamic Typing: can reassign variable to different data types")
print("the type() method can tell you what data type the variable is")
print("ex. type(a) returns float therefore variable a is a float")
print("\n")

#Strings
print("Strings can be in 'single quotes'")
print('or "double quotes"')
print("\n")

print("python uses both indexing and reverse indexing")
print("[h  e  l  l  o]")
print("[0  1  2  3  4] <- indexing")
print("[0 -4 -3 -2 -1] <- reverse indexing")
print('mystring = "Hello World"')
mystring = "Hello World"
print("mystring[0] =", mystring[0])
print("mystring[1] =", mystring[1])
print("mystring[-1] =", mystring[-1])
print("\n")

print("slicing allows you to grab a substring of multiple characters")
print("[start:stop:step]")
print('mystring = "abcdefghijk"')
mystring = "abcdefghijk"
print("start: mystring[3:] <-starts at d, displays everything after")
print("mystring[3:] = ", mystring[3:])
print("stop: mystring[:3] <- end at d, displays everything before 3 (up to, not including)")
print("mystring[:3] = ", mystring[:3])
print("mystring[3:6] <- start at d (index 3) displays after until end at g but does not include (index 6)")
print("mystring[3:6] = ", mystring[3:6])
print("mystring[::] == mystring (whole string")
print("mystring[::]  =", mystring[::], "== mystring  =", mystring)
print("step: mystring[::2] = step size of two (every other) == ", mystring[::2])
print("reverse string: mystring[::-1] == ", mystring[::-1])
print("can also do 'education'[3:6] (just a string that's not a variable) = ", 'education'[3:6])
print("\n")

print("Use escape sequences:")
print("to break lines: \n backslash n")
print("to tab use: \t backslash t")
print("\n")

print("get length of string using len() method")
print('Say a = "cat", then len(a) returns 3.')
a = "cat"
print("Like this: ", len(a))
print("\n")

print("strings are not mutable so you cannot use indexing to change individual elements")
print("Concatination: Changing letters in a string")
print("name = Sam, new_name = 'P' + name[1:]")
name = 'Sam'
new_name = 'P' + name[1:]
print("new_name: ", new_name)
print("\n")
print("2+3 = ", 2+3, " but '2'+'3' = ", '2'+'3')
print("\n")
print("string methods: string_name. <-shows list of methods available to string class")
x = "Hello World"
print('x = "Hello World" x.upper() = ', x.upper())
print('x.upper needs to be saved to a variable. so x is still: ', x)
print('x = "Hello World" x.lower() = ', x.lower())
print('x = "Hello World" x.split() = ', x.split(), 'split at space to form list')
print("x = 'Hello World' x.split('l') = ", x.split('l'), "split at l to form list, removes l's")
print("\n")
print("String interpolation: insert variable into string")
print(".format() uses {} as placeholders in a string")
mystring = 'The {} {} {}'
print("So mystring = 'The {} {} {}' prints as: ", mystring)
print("mystring.format('fox', 'brown', 'quick') = ", mystring.format('fox', 'brown', 'quick'))
print("We can reorder this with index position: So mystring = 'The {2} {1} {0}' mystring.format('fox', 'brown', 'quick')")
mystring = 'The {2} {1} {0}'
print("'The {2} {1} {0}' = ", mystring.format('fox', 'brown', 'quick'))
mystring = 'The {0} {0} {0}'
print("we can use the same index multiple times like 'The {0} {0} {0}' = ", mystring.format('fox', 'brown', 'quick'))
mystring = 'The {q} {b} {f}'
print("and we can set them equal to variables like mystring.format(f='fox', b='brown', q='quick')")
print("'The {q} {b} {f}' = ", mystring.format(f='fox', b='brown', q='quick'))
print("\n")
print("we can use this to our advantage with values and floats")
result = 100/777
print("say we have:result = 100/777 (0.1287001287001287), and mystring = 'The value was {r}'")
mystring = 'The value was {r}'
print("mystring.format(r=result) = ", mystring.format(r=result))
print("we can adjust width.precision inside our brackets like {r:1.3f}")
print("Here 1 is our width (size of overall number) and .3f is three digits after the float(.)")
mystring = 'The value was {r:1.3f}'
print("so with our mystring 'The value was {r:1.3f}' = ", mystring.format(r=result))
mystring = 'The value was {r:10.3f}'
print("and 'The value was {r:10.3f}' = ", mystring.format(r=result))
print("a 1 for your width will give you just the number with no whitespace")
print("\n")
print("f string (format strings) are ways of using format w/o the .format")
name = 'Jose'
print("say name = Jose and with want to say: 'my name is {}'.format(name)")
print("we can instead insert an f infront of the string: f'my name is {name}'")
print("so f'my name is {name}' = ", f'my name is {name}')
print("You can use f strings with multiple variables")

print("\n")

#Lists
mylist = [1,2,3]
my_list = ['STRING', 100, 23.2]
mlist = [0]*3
print("compose list: my_list = ['STRING', 100, 23.2]")
print("or if all same value: mlist = [0]*3: mlist = ", mlist)
len(mylist)
print('Lists are ordered series of elements: mylist = ', mylist)
print("They do not have to contain the same objects: my_list = ", my_list)
print('They can use len(mylist) =', len(mylist))
new_list = mylist+my_list
print('Addition: new_list = mylist + my_list = ', new_list)
print('Slicing: mylist[1:] = ', mylist[1:])
print('Indexing: mylist[0] =', mylist[0])
mylist[0] = 'ONE'
print("Change elements: mylist[0] = 'ONE': mylist = ", mylist)
mylist.append(4)
print("Can add item to end of list: mylist.append(4) : mylist = ", mylist)
popped = mylist.pop()
print("can remove item from end of list with mylist.pop() : mylist = ", mylist)
print("can save popped item. popped = mylist.pop() : popped = ", popped)
popped = mylist.pop(1)
print("can index popped = mylist.pop(1) : popped = ", popped, " mylist = ", mylist)
alpha = ['b', 'a', 'd', 'c']
alpha.sort()
print("alpha = ['b', 'a', 'd', 'c'], alpha.sort() sorts list (cannot save to variable, does not return anything)")
print("alpha.sort, alpha = ", alpha)
alpha.reverse()
print("reverse list with alpha.reverse() <- also in place (dose non return anything), alpha = ", alpha) 
mylist = [1,[2,3],4,5]
print("can have nested list: mylist = [1,[2,3],4,5]")
print("index: mylist[0] = ", mylist[0])
print("mylist[1][0] = ", mylist[1][0])
print("mylist[1][1] = ", mylist[1][1])
print("or mylist[1] = ", mylist[1])
print("mylist[2] = ", mylist[2])
print("mylist[3] = ", mylist[3])

print("\n")

#Dictionaries
mydict = {'key1':'value1', 'key2':'value2'}
print("Dictionaries: mydict = {'key1':'value1', 'key2':'value2'}")
print("dictionaries are unordered and cannot be sorted")
print("mydict['key1'] =", mydict['key1'])
print("dictionaries can hold strings, ints, floats, lists, and other dictionaies")
print("dictionaries are mutable (can change content w/o changing identity)")
print("to get list from inside d = {'k':[0,1,2]}")
print("d['k'] for whole list or d['k'][0] for first item etc...")
print("d = {'key':['a','b','c']}, make c uppercase")
d = {'key':['a','b','c']}
upC = d['key'][2].upper()
print("upC = d['key'][2].upper() = ", d['key'][2].upper())
d['key'][2]=upC
print("d['key'][2]=upC = ", d)
print("\n")
print("to get dictionary from inside d = {'k':{'k2':'v'}}")
print("d['k'] to get whole dictionary or d['k']['k2'] to get interior 'k2' value 'v'")
print("get all keys: d.keys() = ", d.keys())
print("get all values: d.values()", d.values())
print("get all keys and their values: d.items()", d.items())

print("\n")

#tuples
print("Tuples are similar to lists but immutable (cannot be changed or reassigned")
t = (1,2,3)
l = [1,2,3]
print("tuples use (): t = (1,2,3)")
print("lists use []: l = [1,2,3]")
print("can check type(): type(t) = ", type(t), "type(1) = ", type(l))
print("can check len(): len(t) = ", len(t))
print("can use mixed object types tup = ('one', 2) and use indexing the same as with lists")
print("number of times 1 occurs in t: t.count(1) = ", t.count(1))
print("find out index of 1 in t: t.index(1) = ", t.index(1))
print("if mulitples of element in tuple index will return 1st instance")
print("tuples cannot be changed, t[0] = 1 will NOT work")
print("tuples used to make sure objects won't get changed, helps in data integrity")
print("tuples can contain lists but the lists will be immutable.")

print("\n")

#Sets
print("unordered collcetion of unique elements, each element can only exist once")
myset = set()
myset.add(1)
print("myset = set() <- this is an empty set. use myset.add(1) to add element 1 to myset. myset = ", myset)
myset.add(2)
print("myset.add(2) = ", myset)
print("can turn string 'Mississippi' into set by: set('Mississippi') = ", set('Mississippi'))

#Booleans
print("booleans are operator that allow you to convey True or False statements")
print("Booleans are important for conveying logic")
print("booleans must start with capitol letter: True or False")
print("can use type(False) = ", type(False))
print("Used with operators: is 1>2 = ", 1>2)

print("\n")
b = None
print("can set variables to None so None data type: b = None, type(b) = ", type(b))

#I/O 
myfile = open('myfile.txt')
print("I/O: to open a file that exists: myfile = open('myfile.txt') where myfile.txt is the file name.")
print("this only works if file is in same location as program.")
print("myfile.read() <- returns string of everything in text file")
print(myfile.read())
print("To read again use myfile.seek(0) <- returns to top of file so you can read again")
myfile.seek(0)
print("if you want a list of each element in string file use: myfile.redlines() = ") 
print(myfile.readlines())
myfile.seek(0)
print("to get an element from a different folder use the whole pathname in open()")
print('Windows: myfile = open("C:\\Users\\UserName\\Folder\\myfile.txt")')
print('MacOS/Linux: myfile = open("/Users/UserName/Folder/myfile.txt")')
print("Now we have to close the file myfile.close()")
myfile.close()
print("to avoid errors we can do this:")
print("\n")
print("with open('myfile.txt') as myfile:")
print("\t contents = myfile.read()")
print("\n")
print("this allows you to not have to close the file.")
with open('myfile.txt') as myfile:
    contents = myfile.read()
print("Contents = ", contents)
print("\n")
print("we can use mode to only read files (mode: 'r')")
print("We can also write to files (mode:'a') and overwrite files (mode:'w') using permissions")
print("if you use mode = 'w' python will create the file if it doesn't already exist.")
print("with open('myfile.txt', mode='r') as myfile: <- this is only reading the file")
print("with open('myfile.txt', mode='a') as myfile: \t myfile.write('backslashn FOUR!')<- this is writing to the file")
with open('myfile.txt', mode='a') as myfile: 
    myfile.write('\nFOUR!')
with open('myfile.txt') as myfile:
    contents = myfile.read()
print("Contents = ", contents)