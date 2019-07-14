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
print("for a,b in newlist: \n\tprint(a) \n\tprint(b)")
newlist = [(1,2),(3,4),(5,6)]
for a,b in newlist:
    print(a)
    print(b)
print("\n")
print("for a,b in newlist: \n\tprint(b)")
for a,b in newlist:
    print(b)
print("\n")

print("\n")
#While Loops
print("While loops ")