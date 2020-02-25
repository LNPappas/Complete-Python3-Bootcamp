#Modules and Packages
import module
from main_package import main
from main_package.sub_package import sub

def func():
    print("This is a function in the main file.")

#__name__ & "__main__"

if __name__ == "__main__":
    func()
    module.my_func()
    main.main_report()
    sub.sub_report()
