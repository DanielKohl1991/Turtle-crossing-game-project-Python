import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
cars = CarManager()
score = Scoreboard()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.add_car()
    cars.move()

    for car in cars.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            score.game_over()

    if player.ycor() > -200:
        player.reset()
        cars.increase()
        score.point()


screen.exitonclick()