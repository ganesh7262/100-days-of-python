from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, shape: str = ..., undobuffersize: int = ..., visible: bool = ...) -> None:
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0,250)
        self.s1=0
        self.s2=0
        self.write(f"Score\n  {self.s1}|{self.s2}",align='center',font=("Arial",14,"normal"))

    def score_update(self):
        self.clear()
        self.write(f"Score\n  {self.s1}|{self.s2}",align='center',font=("Arial",14,"normal"))

    def lp_score_update(self):
        self.s1+=1
    
    def rp_score_update(self):
        self.s2+=1