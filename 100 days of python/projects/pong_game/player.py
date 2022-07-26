from turtle import Turtle


class Player(Turtle):
    
    def __init__(self,co_ordinates, shape: str = ..., undobuffersize: int = ..., visible: bool = ...) -> None:
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(5,0.5)
        self.penup()
        self.speed('fastest')
        self.co_ord=co_ordinates
        self.goto(self.co_ord)
        self.score=0


    