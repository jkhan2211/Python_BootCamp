#Calculator


# Add two numbers
def add (n1, n2):
    return n1 + n2


#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2


#Divide
def divide(n1, n2):
    return n1 / n2



#Operation dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What is the first number: "))


for symbol in operations:
    print(symbol)

should_continue = True

while should_continue:

    operation_symbol = input("Pick an operation:  ")
    num2 = int(input("What is the next number: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit: ") == "y":
        num1 = answer
    else:
        should_continue = False