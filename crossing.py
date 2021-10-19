from turtle import Turtle
import random

colors = ["red", "blue", "white", "black", "pink", "purple", "orange", "yellow"]

class Jimmy(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(stretch_len=1.5, stretch_wid=1.5)
        self.color(random.choice(colors))
        self.setheading(90)
        self.penup()
        self.goto(0,-230)

    def move(self):
        self.forward(10)