from time import sleep
from turtle import Turtle
from random import choice,randint


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]



class CarManager():
    def __init__(self) -> None:
        self.base_speed = 5
        self.difficulty=0
        self.car_list=[]
        
    
    def create_car(self,level):
        if level>=6:
            level=5
        random_chance=randint(1,6-level)
        if random_chance==1:
            car=Turtle('square')
            car.penup()
            car.shapesize(1,2)
            car.color(choice(COLORS))
            car.goto(280,randint(-250,250))
            self.car_list.append(car)
        
    
    def car_movement(self):
        for car in self.car_list:
            car.setheading(180)
            car.forward(self.base_speed+self.difficulty)

    def car_speed_up(self):
        self.difficulty+=10
        
        
        
        

    
