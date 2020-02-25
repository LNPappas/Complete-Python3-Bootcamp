#errors and exception handling:

def add(n1=1,n2=100):
    print_to_file(str(n1+n2))

def ask_for_int():

    while True:
        try:
            result = int(input("Please provide a number:\n"))
        except:
            print("Whoops! that is not a number!\n")
            continue
        else:
            break   
    add(result)

def print_to_file(answer):
    while True:
        try: 
            f=open('testfile','w')
            f.write(answer)
        except TypeError:
            print("There was a type error!")
            ask_for_int()
        except OSError:
            print("Hey, you have an OS Error")
            ask_for_int()
        else:
            break

if __name__ == '__main__':

    ask_for_int()

#homework:

    #handle exception for:
#1
    try:
        for i in ['a','b','c']:
            print(i**2)
    except TypeError:
        print("I'm sorry, you must provide an integer.\n")

#2
    try:
        x=5
        y=0
        z=x/y
    except ZeroDivisionError:
        print("I'm sorry, you can't divide a number by 0.")
    finally:
        print("All done!\n")

#3
    def ask():
        while True:
            try:
                num = int(input("What # would you like to square?\n"))
            except TypeError:
                print("I'm sorry, please type a # like 1 or 35429.")
            except ValueError:
                print("I'm sorry, please type a # like 1 or 35429.")
            else:
                print(num**2)
                break
    ask()

#Unit testing:
#PEP8 = style conventional rules

