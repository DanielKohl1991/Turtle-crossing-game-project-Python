from turtle import Screen, Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE
    def add_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(x=300, y=random.randint(-250, 250))
            self.all_cars.append(new_car)



    def move(self):
        for car in self.all_cars:
            car.backward(self.speed)



    def increase(self):
        self.speed += MOVE_INCREMENT
