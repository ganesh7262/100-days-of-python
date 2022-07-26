from turtle import Turtle
START_POS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
        
    def __init__(self) -> None:
        self.segment=[]
        self.create_snake()
        self.snake_head=self.segment[0]
    

    def create_snake(self):
        for positions in START_POS:
            self.add_segment(positions)




    def add_segment(self,positions):
            new_segment = Turtle("square")
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(positions)
            self.segment.append(new_segment)
    
    def extend_snake(self):
        self.add_segment(self.segment[-1].pos())
    
    
    def snake_movement(self):
        for seg_num in range(len(self.segment)-1, 0, -1):
            new_x = self.segment[seg_num-1].xcor()
            new_y = self.segment[seg_num-1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(20)

    def up(self):
        if self.segment[0].heading()==270:
            return
        self.segment[0].seth(90)

    def down(self):
        if self.segment[0].heading()==90:
            return
        self.segment[0].seth(270)
    
    def right(self):
        if self.segment[0].heading()==180:
            return
        self.segment[0].seth(0)
    
    def left(self):
        if self.segment[0].heading()==0:
            return
        self.segment[0].seth(180)
        





