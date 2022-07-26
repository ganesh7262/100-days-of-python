from turtle import Turtle, Screen
from random import choice, randint
list_color = [str(x) for x in "yellow, gold, orange, red, maroon, violet, magenta, purple, navy, blue, skyblue, cyan, turquoise, lightgreen, green, darkgreen, chocolate, brown, black, gray".split(", ")]

tim = Turtle()
tim.shape('turtle')
tim.speed('fastest')


def form_square(turtle: Turtle):

    for i in [0, 90, 180, 270]:
        turtle.setheading(i)
        turtle.forward(50)


def dashed_line(turtle: Turtle):
    dx = 10
    for i in range(50):
        turtle.pendown()
        turtle.forward(5)
        turtle.penup()
        turtle.setx(turtle.xcor()+dx)


def creating_closed_shape(tim: Turtle):
    ang = 360
    for shape in range(3, 11):
        for side in range(shape):
            start_cor = tim.pos()
            tim.forward(100)
            tim.right(ang/shape)
            if tim.pos() == start_cor:
                break


def random_walk(tim: Turtle, size_of_walk: int, list_color: list):
    direction = [0, 90, 180, 270]
    for steps in range(size_of_walk):
        tim.setheading(choice(direction))
        tim.pensize(10)
        tim.pencolor(choice(list_color))
        tim.forward(30)


def random_walk2(tim: Turtle, size_of_walk: int):
    '''Random walk with random color'''
    direction = [0, 90, 180, 270]
    for steps in range(size_of_walk):
        tim.setheading(choice(direction))
        tim.pensize(10)
        tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
        tim.forward(30)




screen = Screen()
screen.colormode(255)
screen.exitonclick()
