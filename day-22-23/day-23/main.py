import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# initiating screen object
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0) # hold the draw until update

# initiating player, scoreboard and car_manager objects
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

# when press 'w', turtle go up
screen.listen()
screen.onkeypress(player.move_forward, "w")

# while loop until crash with a car
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # every 0.1 sec, create and move a car (creation speed was decreased in CarManager Class)
    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with cars:
    for car in car_manager.cars:
        if car.distance(player) < 21:
            scoreboard.game_over()
            game_is_on = False

    # detect when got to finish line:
    if player.ycor() > 280:
        scoreboard.increase_level()
        player.reset_position()
        car_manager.speed_up()


screen.exitonclick()
