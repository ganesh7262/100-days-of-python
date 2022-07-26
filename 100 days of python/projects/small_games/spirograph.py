from turtle import Turtle,Screen
from random import randint


tim=Turtle()
tim.speed('fastest')



def spirogrph(tim:Turtle):
    
    for i in range(0,361,5):
        tim.pencolor(randint(0,255),randint(0,255),randint(0,255))
        tim.circle(100)
        tim.setheading(i)
        
    




screen=Screen()
screen.colormode(255)
spirogrph(tim=tim)
screen.exitonclick()