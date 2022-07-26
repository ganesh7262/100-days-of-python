from random import randint
from turtle import Turtle, Screen

is_race_on=False
screen = Screen()
screen.colormode(255)
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    "who will win?", prompt="choose a color from rainbow as player")

rainbow_colors = ["Red", "orange", "yellow",
                  "green", "blue", "indigo", "violet"]

all_players=[]

def pre_game_setup():
    x, y = -230, -105
    for i in range(len(rainbow_colors)):
        tim=Turtle()
        tim.shape('turtle')
        tim.color(rainbow_colors[i])
        tim.penup()
        tim.goto(x,y)
        all_players.append(tim)
        y+=30
        


if user_bet:
    is_race_on=True

pre_game_setup()
while is_race_on:
    for player in all_players:
        if player.xcor()>230:
            winner=player.color()[1]
            if user_bet.lower()==str(winner).lower():
                print("You win")
            else:
                print('You loose')
                print(f"Winner is {player.color()[1]}")
            is_race_on=False
        rand_distance=randint(1,10)
        player.forward(rand_distance)


screen.exitonclick()
