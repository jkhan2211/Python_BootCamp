# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("Hello")
    print("World")
    print("!")

greet()

# Function that allows for input 

""" def greet_with_name(name):
    print(f"Hello {name}")
    print("World")
    print("!")

greet_with_name("Junaid") """

# Function with more than 1 input
""" def greet_with(name, age):
    print(f"Hello {name} you are {age} years old")
    print("World")
    print("!")

greet_with("Junaid", "28")
 """


 # Function with keyword arguments
def greet_with(name, location):
    print(f"Hello {name} you are from {location}")
    print("World")
    print("!")

greet_with(name="Junaid", location="London")