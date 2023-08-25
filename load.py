from turtle import *
import random
x=0
class load(Turtle):
    def __init__(self):
        super().__init__()
        self.write(f"score: ",align="center",font=("Courier",20,"normal"))
        self.penup()
        self.goto(x=0,y=50)
        self.pendown()
        self.pensize(10)                   
        global x,r,g,b
    def loading(self):                                        
            self.color(random.choice(["red","blue","green","cyan","black","white"]))            
            self.circle(50)


