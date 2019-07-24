import CPBsection9

def my_func():
    print("Hey! I'm in module!")

if __name__ == '__main__':
    print("module is being printed directly.")
    print("but we can still print from main: ")
    CPBsection9.func()
else:
    print("The module has been imported.")