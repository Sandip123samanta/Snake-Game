from turtle import Screen, Turtle
import random
from load import load
COLOR = (0.60156, 0, 0.99218)  # (154, 0, 254)
TARGET = (0.86328, 0.47656, 0.31250)  # (221, 122, 80)
x=0
r=0
g=0
b=0
class loadingscreen(Turtle):
    def __init__(self):
        super().__init__()
        self.WIDTH, self.HEIGHT = screen.window_width(), screen.window_height()
        self.deltas = [(hue - COLOR[index]) / self.HEIGHT for index, hue in enumerate(TARGET)]
        self.color(COLOR)
        self.penup()
        self.goto(-self.WIDTH/2, self.HEIGHT/2)
        self.pendown()
        self.direction = 1
        for distance, y in enumerate(range(self.HEIGHT//2, -self.HEIGHT//2, -1)):
            self.forward(self.WIDTH * self.direction)
            self.color([COLOR[i] + delta * distance for i, delta in enumerate(self.deltas)])
            self.sety(y)
            self.direction *= -1
screen= Screen()
screen.tracer(0)

wn=loadingscreen()
x=load()
for m in range(0,5):
    x.loading()
screen.tracer(1)
screen.exitonclick()