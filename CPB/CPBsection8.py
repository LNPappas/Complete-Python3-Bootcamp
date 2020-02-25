#Object Oriented Programming:

class NameOfClass():
    def __init__(self,param1,param2):
        self.param1 = param1
        self.param2 = param2
    
    def some_method(self):
        #perform some action
        print(self.param1)

#Attributes and Class keywords:

class Dog():
    #__init__ :initiates the class (constructor) first def in every class
    #self :represents as instance of object itself
    def __init__(self, breed, name, spots): #breed is an attribute
        self.breed = breed 
        #conventionally it's self.attribute_name (in this case breed)
        #it can be self.anything as long as it = the attribute.
        self.name = name #expect name to be a string
        self.spots = spots #expect boolean for spots, but user won't know with/out type control

my_dog = Dog(breed='Black Lab', name='Teddy', spots=False)
print(type(my_dog))
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)

#class object attribues & methods:
class Dog():
    #Class object attribute
    #same for any instance of a class
    species = 'mammal'

    #__init__ :initiates the class (constructor) first def in every class
    #self :represents as instance of object itself
    def __init__(self, breed, name, spots): #breed is an attribute
        self.breed = breed 
        #conventionally it's self.attribute_name (in this case breed)
        #it can be self.anything as long as it = the attribute.
        self.name = name #expect name to be a string
        self.spots = spots #expect boolean for spots, but user won't know with/out type control

    #methods are operations/Actions
    #they are esentailly functions inside a class
    def bark(self):
        print(f"Woof! My name is {self.name}.")


my_dog = Dog('Yellow Lab', 'Jack', False)
print("\n")
print(type(my_dog))
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
print(my_dog.species)
my_dog.bark()
print("\n")

class Circle():
    #Class object attribute (true for any instance of the class)
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def get_circumfrence(self):
        return 2*Circle.pi*self.radius

    def get_area(self):
        return self.pi*self.radius**2

mycircle1 = Circle()
mycircle2 = Circle(30)

print(mycircle1.get_circumfrence())
print(mycircle1.get_area(), "\n")

print(mycircle2.get_circumfrence())
print(mycircle2.get_area(), "\n")

#inheritance and polymorphism

#inheritance:
class Animal():

    def __init__(self):
        print("Animal Created")
    
    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

myanimal = Animal()
myanimal.eat()
print("\n")

class Dog(Animal):
    #Class object attribute
    #same for any instance of a class
    species = 'mammal'


    #all attributes and methods in animal are now in dog
    def __init__(self): #breed is an attribute
        Animal.__init__(self)     #__init__ of animal class because inherited.
        print("Dog Created")

    #Can re-write animal class specifically for dog
    def who_am_i(self):
        print("I am a Dog")

    def bark(self):
        print(f"Woof!")

my_dog = Dog()
my_dog.bark()
my_dog.eat()
print("\n")

#Polymorphism:
class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says WOOF!'

class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says MEOW!'

my_dog = Dog("niko")
my_cat = Cat("felix")
print(my_dog.speak())
print(my_cat.speak(), '\n')

#two different classes use the same method so can use for loop to call both classes
for pet in [my_dog, my_cat]:
    print(type(pet))
    print(pet.speak())

print("\n")
#can create a function that calls method from multiple classes with same method
def pet_speak(pet):
    print(pet.speak())

pet_speak(my_dog)
pet_speak(my_cat)
print('\n')

#abstract class (base class, will never create instance of this class.)
class Animal():
    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

class Dog(Animal):

    def speak(self):
        return self.name + " says woof!"

class Cat(Animal):
    
    def speak(self):
        return self.name + " says meow!"

fido = Dog('Fido')
fred = Cat('Fred')
print(fido.speak())
print(fred.speak(),'\n')

#Magic/Dunder Methods
mylist = [x for x in range(1,4)]
print(mylist,' len:', len(mylist))

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object has been deleted")

b = Book('A Book', 'Lauren', 105)
print(b, 'Length:', len(b))
del(b)

#Homework

#Problem 1: Fill in LIine Class methods to accept 
# coordinates as a pair of tuples and return the slope 
# and the distance of a line

class Line():

    def __init__(self, coor1, coor2):
        self.x1 = coor1[0]
        self.y1 = coor1[1]
        self.x2 = coor2[0]
        self.y2 = coor2[1]

    def distance(self):
        return ((self.x2-self.x1)**2 + (self.y2-self.y1)**2)**0.5

    def slope(self):
        return (self.y2-self.y1)/(self.x2-self.x1)

coordinate1 = (3,2)
coordinate2 = (8,10)
line = Line(coordinate1, coordinate2)
print('Distance: ', line.distance())
print('Slope: ', line.slope(), '\n')

class Cylinder:

    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.pi*(self.radius**2)*self.height

    def surface_area(self):
        return self.volume() + self.height*((2*self.pi)*self.radius)

c = Cylinder(2,3)
print('Volume: ', c.volume())
print('Surface Area: ', c.surface_area(), '\n')

#Challange

class Account:

    def __init__(self, owner='Lauren', balance=0):
        self.owner = owner
        self.balance = balance
        print(f'Good day {self.owner}.\n')

    def __str__(self):
        return f' Account Owner: {self.owner}\n Account Balance: ${self.balance}'

    def deposit(self, in_money):
        self.balance = self.balance + in_money
        print(f'{self.owner}, your new balance is: ${self.balance}')

    def withdrawl(self, out_money):
        if self.balance - out_money > 0:
            self.balance = self.balance - out_money
            print(f'{self.owner}, your new balance is: ${self.balance}')
        else:
            print(f"I'm sorry {self.owner}, you're withdrawl cannot succeed your current balance of ${self.balance}.")

account = Account('Harvey', 100)
print(account)
print(account.owner)
print(account.balance)
account.withdrawl(200)
account.deposit(200)
account.withdrawl(200)

        

