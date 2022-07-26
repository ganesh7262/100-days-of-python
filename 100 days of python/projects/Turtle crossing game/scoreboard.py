from turtle import Turtle


FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self, shape: str = ..., undobuffersize: int = ..., visible: bool = ...) -> None:
        super().__init__()
        self.score=0
        self.hideturtle()
        self.penup()
        self.color('black')
        self.goto(-240,265)
        self.write(f"Score:{self.score}",align='center',font=FONT)
    
    def score_update(self):
        self.score+=1
        self.clear()
        self.write(f"Score:{self.score}",align='center',font=FONT)

    def game_over(self):
        self.clear()
        self.color('black')
        self.goto(0,0)
        self.write(f"GAME OVER",align='center',font=FONT)