#Decorators
#  allow extra functionality to an already existing function
#  @some_decorator
#  decorators easily turn on and off

def hello():
    return "hello!"

print(hello())

greet = hello
print(greet())

del hello
print(greet())

#return function inside another function:
def hello(name = 'Lauren'):
    print(f"The hello function is being executed {name}")

    def greet():
        return f'\t This is the greet function inside hello {name}'

    def welcome():
        return f'\t This is the welcome function {name}'

    if name == 'Lauren':
        return greet
    else:
        return welcome

hello()
l = hello()
print(l())
hello('Danielle')
e = hello('Evie')
print(e())

def cool():
    def super_cool():
        return 'Super Cool!!'
    return super_cool

fun = cool()
print(fun())

#passing a function into another function: (a function as an argument)
def hey():
    return "Hey!"

def other(some_def_func):
    print('This is the other function')
    print(some_def_func())

other(hey)

#Decorator!

def new_decorator(orig_func):

    def wrap_func(): #represents extra functionality wraping original function
        print('Oh, did you want to be decorated?')
        orig_func()
        print('Consider yourself decorated!\n')
    
    return wrap_func

    
def dec_needed():
    print("Decorate Me!")

dec_needed()
after_dec = new_decorator(dec_needed)
after_dec()

#special syntax!
@new_decorator
def dec_needed():
    print("Decorate Me!")

dec_needed()


