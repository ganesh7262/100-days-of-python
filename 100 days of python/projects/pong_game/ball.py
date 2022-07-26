from random import choice,randint
from select import select
from turtle import Turtle
from typing_extensions import Self


class Ball(Turtle):


    def __init__(self, shape: str = ..., undobuffersize: int = ..., visible: bool = ...) -> None:
        super().__init__()
        self.shape('circle')
        self.shapesize(0.7,0.7)
        self.color('white')
        self.penup()
        self.dx=10
        self.dy=10

    def ball_move(self):
        new_x=self.xcor()+self.dx
        new_y=self.ycor()+self.dy
        self.goto(new_x,new_y)

    def bounce(self):
        self.dy*=-1
    
    def bounce_peddle(self):
        self.dx*=-1
    
    
    


