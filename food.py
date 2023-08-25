from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("white")
        self.refresh()
        
    def refresh(self):
        rendom_x=random.randint(-280,280)
        rendom_y=random.randint(-280,270)
        self.goto(rendom_x,rendom_y)