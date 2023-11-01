# python pre installed turtle module

from turtle import Turtle, Screen
# object and acessing thier attributes

timmy = Turtle()  # turtle is class
print(timmy)
# timmy is object
timmy.shape("turtle")
timmy.color("red")
timmy.forward(45)

# here my_screen is object
# example car.spped
my_screen = Screen()
print(my_screen.canvheight)  # and canvheight is attribute

# method function
# car.stop()
my_screen.exitonclick()
