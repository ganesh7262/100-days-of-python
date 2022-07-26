from turtle import Turtle
from random import randint

class Food(Turtle):
    

    def __init__(self, shape: str = ..., undobuffersize: int = ..., visible: bool = ...) -> None:
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('blue')
        self.shapesize(0.5,0.5)
        self.speed('fastest')
        self.new_loation()

    def new_loation(self):
        self.goto(randint(-280,280),randint(-280,280))
        