from turtle import Turtle as t, Screen
tim = t()

for _ in range(15):

    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = Screen()  # this  used for screen don't exit without permission
screen.exitonclick()
