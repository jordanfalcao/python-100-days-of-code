from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

my_snake = []
x_pos = 0

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -290:
        is_on = False
        score.game_over()

    # Detect collision with tail
    for segment in snake.my_snake[1:]:
        if snake.head.distance(segment) < 10:
            is_on = False
            score.game_over()

screen.exitonclick()
