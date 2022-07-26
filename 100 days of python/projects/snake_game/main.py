import turtle
from food import Food
from snake import Snake
from turtle import Screen
from time import sleep
from scoreboard import Scoreboard

screen = Screen()
screen.colormode(255)
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake game')
screen.tracer(0)
 

scorebaord = Scoreboard()
snake = Snake()
screen.update()
food = Food()
screen.listen()


screen.onkeypress(fun=snake.left, key='a')
screen.onkeypress(fun=snake.right, key='d')
screen.onkeypress(fun=snake.up, key='w')
screen.onkeypress(fun=snake.down, key='s')


game_on = True
while game_on:
    screen.update()
    sleep(0.1)
    snake.snake_movement()
    # increases score and respawns new food
    if snake.snake_head.distance(food) < 15:
        snake.extend_snake()
        food.new_loation()
        scorebaord.score_increase()
    # close game window if user hits the wall
    if -280 < snake.snake_head.xcor() > 280 or -280 < snake.snake_head.ycor() > 280:
        print("you loose")  
        screen.bye()
        break

    for segment in snake.segment[1:]:
        if snake.snake_head.distance(segment) < 10:
            game_on = False
            print(f"You Loose, Final Score:{scorebaord.score}")
