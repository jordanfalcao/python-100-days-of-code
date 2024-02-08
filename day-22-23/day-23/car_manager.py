from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 8


class CarManager():
    def __init__(self):
        self.cars = []  # empty list to append cars
        self.car_speed = STARTING_MOVE_DISTANCE  # attribute to be increased

    def create_car(self):
        random_chance = random.randint(1, 6) # decrease car creation speed
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.up()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            self.cars.append(new_car)  # append new_car to cars list

    # move each car
    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

    # increase move speed
    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
