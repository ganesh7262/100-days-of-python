from turtle import Turtle,Screen


tim=Turtle()


def fordward():
    tim.forward(10)

def turn_left():
    tim.setheading(tim.heading()+10)

def turn_right():
    tim.setheading(tim.heading()-90)
def backward():
    tim.backward(10)

def clear():
    screen.clear()
    tim.home()





screen=Screen()
screen.onkeypress(fun=turn_left,key='a')
screen.onkeypress(fun=turn_right,key='d')
screen.onkeypress(fun=fordward,key='w')
screen.onkeypress(fun=backward,key='s')
screen.onkeypress(fun=clear,key='c')
screen.listen()
screen.exitonclick()
