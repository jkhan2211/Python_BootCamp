import another_module
print(another_module.another_variable)
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
#Object Methods
timmy.color("bisque")
timmy.forward(100)

#Object attributes
my_screen = Screen()
print(my_screen.canvheight)


#Object Methods
my_screen.exitonclick()