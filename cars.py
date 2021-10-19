from turtle import Turtle
import random

colors = ["red", "blue", "white", "black", "pink", "purple", "orange"]
pace = [10,20,35,50]
lane = [-170,-130,-70,-30,30,70,130,170]
car_list = []

class Cars:
    def __init__(self):
        self.car_list = []

    def create_cars(self):
        new_car = Turtle("square")
        new_car.color(random.choice(colors))
        new_car.setheading(180)
        new_car.shapesize(stretch_wid=2, stretch_len=5)
        new_car.penup()
        new_car.goto(400, random.choice(lane))
        new_car.velocity = random.choice(pace)
        self.car_list.append(new_car)

    def move_cars(self):
        for car in self.car_list:
            car.forward(car.velocity)

    def delete_car(self):
        for car in self.car_list:
            if car.xcor() < -440:
                self.car_list.remove(car)


