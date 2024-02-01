import time
from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
STARTING_POSITIONS = [(0,0), (0,-20), (0,-40)]

class Snake:

    def __init__(self):
        self.segments = []
        self.x_cor = 0
        self.make_snake()
        self.head = self.segments[0]

    def make_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def move(self):
        time.sleep(0.1)
    
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() == DOWN:
            pass
        else:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() == UP:
            pass
        else:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() == RIGHT:
            pass
        else:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() == LEFT:
            pass
        else:
            self.head.setheading(RIGHT)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self,position):
        seg = Turtle("square")
        seg.color("white")
        seg.penup()
        seg.goto(position)
        self.x_cor -= 20
        self.segments.append(seg)