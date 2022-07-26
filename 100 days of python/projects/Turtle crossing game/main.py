import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title('Turtle crossing game')
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Player

player=Player()


# Movement

screen.onkeypress(player.move,"w")


# Random Cars

cars=CarManager()


# Scoreboard
scoreboard=Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car(scoreboard.score)
    cars.car_movement()
    for car in cars.car_list:
        if car.distance(player)<20:
            scoreboard.game_over()
            game_is_on=False
    if player.finish_line():
        scoreboard.score_update()
        cars.car_speed_up()


        

