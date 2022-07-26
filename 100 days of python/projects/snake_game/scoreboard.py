from turtle import Turtle, hideturtle


class Scoreboard(Turtle):
    
    def __init__(self, shape: str = ..., undobuffersize: int = ..., visible: bool = ...) -> None:
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(0,260)
        self.write(f"Score: {self.score}",align="center",font=("Arial",14,"normal"))
        
    def score_increase(self):
        self.clear()
        self.score+=1
        self.write(f"Score: {self.score}",align="center",font=("Arial",14,"normal"))
        
