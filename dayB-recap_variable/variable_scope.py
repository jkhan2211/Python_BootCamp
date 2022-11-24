#LEGB(up)

#1. Local Scope
# refers to a variable declared inside a function. For example, in the code below, the variable total is only
# avaialble to code within the get_total function. Anything outside of this function will not have access to it
'''
def get_total(a,b):
    #local variable declared inside a function
    total = a + b
    return total

print(get_total(5, 2))
'''

# Accessing variable outside of the function
# print(total)
#NameError: name 'total' is not defined


#2 Enclosing scope
# referes to a function inside another function or what is commonly known as nested function

def get_total_enclose(a,b):
    #enclosed variable declare inside a function
    total = a + b

    def double_it():
        #local variable
        double = total * 2
        print(double)
    
    double_it()
    #double varible will not be accessible 
    print(double)

    return total


#3. Global Scope
# Globl scope is when a variable is declared outside of a function. This means it can be accessed from anywhere

special = 5

def get_total_global(a, b):
    #enclosed scope is when variable is declared ouside of a function. Can be accessed from anywhere
    total = a + b
    print(special)

    def double_it_two():
        #local variable
        double_two = total + 2
        print(special)
    double_it_two()

    return total


#4. Built in scope
# Built in scope referes to the reserved keywords that Python use for its built-in function: such as print, def, for, in

