from scoreboard import Scoreboard
from time import sleep
from turtle import Screen, xcor
from ball import Ball
from player import Player

screen=Screen()
screen.bgcolor('black')
screen.setup(600,600)
screen.title('Pong game')
screen.tracer(0)

# movement
speed=20

def up_p1():
    new_y=l_player.ycor()+speed
    l_player.goto(-280,new_y)
def up_p2():
    new_y=r_player.ycor()+speed
    r_player.goto(280,new_y)

def down_p1():
    new_y=l_player.ycor()-speed
    l_player.goto(-280,new_y)
def down_p2():
    new_y=r_player.ycor()-speed
    r_player.goto(280,new_y)
    
    

screen.listen()
screen.onkeypress(fun=up_p1,key='w')
screen.onkeypress(fun=down_p1,key='s')
screen.onkeypress(fun=up_p2,key='Up')
screen.onkeypress(fun=down_p2,key='Down')





# player instance
l_player=Player((-280,0))
r_player=Player((280,0))


# Scoreboard instance

scoreboard=Scoreboard(l_player.score,r_player.score)

# Ball instancne
ball=Ball(l_player.score,r_player.score)

game_on=True
while game_on:
    screen.update()
    ball.ball_move()
    sleep(0.1)
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()
    
    if ball.xcor()>320:
        scoreboard.lp_score_update()
        scoreboard.score_update()
        ball.home()
    if ball.xcor()<-320:
        scoreboard.rp_score_update()
        scoreboard.score_update()
        ball.home()
    
    if ball.distance(r_player)<50 and ball.xcor()>260 or ball.distance(l_player)<50 and ball.xcor()<-260:
        ball.bounce_peddle()
        
    

screen.exitonclick()