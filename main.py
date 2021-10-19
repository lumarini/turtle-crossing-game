from turtle import Screen, Turtle
from lanes import Lanes
from crossing import Jimmy
from cars import Cars
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("grey")
screen.title("Turtle Crossing")
screen.tracer(0)

lanes = Lanes()

level = 1

colors = ["red", "blue", "white", "black", "pink", "purple", "orange", "yellow"]
car_list = []

screen.listen()
jimmy = Jimmy()
screen.onkey(jimmy.move, "Up")

scoreboard = Turtle()
scoreboard.color("yellow")
scoreboard.penup()
scoreboard.goto(290, 270)
scoreboard.write(f"LEVEL:{level}", align="center", font=("Courier", 14, "bold"))
scoreboard.hideturtle()

cars = Cars()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    if len(cars.car_list) > level + 2:
        pass
    else:
        cars.create_cars()
    cars.move_cars()
    cars.delete_car()

    if jimmy.ycor() > 250:
        level += 1
        scoreboard.clear()
        scoreboard.write(f"LEVEL:{level}", align="center", font=("Courier", 14, "bold"))
        jimmy.goto(0,-230)

    for car in cars.car_list:
        if jimmy.distance(car) < 40:
            game_is_on = False
            game_over = Turtle()
            game_over.color("red")
            game_over.goto(0, 0)
            game_over.penup()
            game_over.hideturtle()
            game_over.write("GAME OVER", align="center", font=("Courier", 60, "bold"))





screen.exitonclick()
