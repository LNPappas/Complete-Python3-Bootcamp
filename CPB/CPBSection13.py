#Generators:
# functions that get a value that can be accessed later. 
# can generate sequence of values over time. 
#   range() is a generater function
#       remembers last number sent out and step size to get adjacent numbers

def cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

print("printing list from cubes(10)")
print(cubes(10))
print("\n")

print("Printing elements of list from cubes(10):")
for x in cubes(10):
    print(x)
print("\n")

def gen_cubes(n):
    for x in range(n):
        yield x**3

print("Printing gen_cubes:")
for x in gen_cubes(10):
    print(x)
print("\n")

print("Calling gen_cubes() without iterating list:")
print(gen_cubes(10))
print('\n')

def fib(n):
    a=1
    b=1
    for _ in range(n):
        yield a
        a,b = b,a+b

print("Theh fibonacchi sequence as a generater function:")
for f in fib(10):
    print(f)
print('\n')

#next function
def simple():
    for x in range(3):
        yield x

print("Printing simple()")
for num in simple():
    print(num)
print("\n")

print("printing through simple() with next(). \nCan only print up to range(3) as defined in the function.")
g = simple()
print(next(g))
print(next(g))
print(next(g))
print('\n')

#string objects support iteration, but do not support generator functions
#can use iter to turn into gererator supported object.
s = 'hello'
s_iter = iter(s)
print("Printing s_iter with next()")
print(next(s_iter))
print(next(s_iter))

#Homework:

#Problem 1:
def squares(n):
    for x in range(n):
        yield x**2

print("Testing squares(10):")
for num in squares(10):
    print(num)
print('\n')

#Probem 2
import random

def rand(low,high,n):
    for _ in range(n):
        yield random.randint(low, high)

print("Testing rand(1,10,12):")
for num in rand(1,10,12):
    print(num)
print('\n')

#Problem 3:
st = 'hello'
st_it = iter(st)
print('testing iter(st):')
for y in st_it:
    print(y)
print('\n')

#Problem 4:

'''
You would want to use yeild instead of return to save memory. So anything that does a 
repeated calculation or step function that you might need to re-visit or easily access the data generated.
For when you do not need to have all info at once.

'''
def gen(n=3):
    for x in range(n):
        y = x**2
        yield x*y

print("yield instead of return example:")
for num in gen(10):
    print(num)
print("\n")


#Extra Credit:
'''
generator comprehension is like list comprehenstion except it returns an iterator insted of a list.
so gen comp turns list comp into generator

'''
print("Generator Comprehension Example:")
l = list(range(0,101))

gencomp = (item for item in l if item%13 == 0)
for item in gencomp:
    print(item)