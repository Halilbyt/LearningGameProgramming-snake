from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color('yellow')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        self.goto(x=random.randint(-380, 380), y=random.randint(-280, 280))
