from turtle import Turtle, hideturtle

GAME_DATA='game_data.txt'


class Scoreboard(Turtle):
    
    def __init__(self, shape: str = ..., undobuffersize: int = ..., visible: bool = ...) -> None:
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        with open(GAME_DATA) as f:
            self.highest_score=int(f.read())
        self.setpos(0,260)
        self.write(f"Score: {self.score}  |  Highest Score:{self.highest_score}",align="center",font=("Arial",14,"normal"))
        
    def score_increase(self):
        self.clear()
        self.score+=1
        self.write(f"Score: {self.score}  |  Highest Score:{self.highest_score}",align="center",font=("Arial",14,"normal"))
    
    def reset(self):
        if self.score>self.highest_score:
            self.highest_score=self.score
            self.score=0
            with open(GAME_DATA,mode='w') as f:
                f.write(f"{self.highest_score}")
              
    
        
