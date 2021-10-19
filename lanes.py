from turtle import Turtle

positions = [(-400,200),(-400,100),(-400,0),(-400,-100),(-400,-200)]
level = 1

class Lanes(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        for position in positions:
            self.penup()
            self.pensize(4)
            self.goto(position)
            self.setheading(0)
            self.pendown()
            while self.xcor() < 400:
                self.forward(20)
                self.penup()
                self.forward(15)
                self.pendown()
        self.penup()
        self.goto(0,260)
        self.write("FINISH", align="center", font=("Courier", 24, "normal"))
        self.goto(0, -290)
        self.write("START", align="center", font=("Courier", 24, "normal"))
        self.hideturtle()

