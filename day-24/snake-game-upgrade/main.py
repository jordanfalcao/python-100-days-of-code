from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

# initiating screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")  # background color
screen.title("My Snake Game")
screen.tracer(0)  # delay in the animation until screen.update

# initiating snake, food and score instances
snake = Snake()
food = Food()
score = Scoreboard()

# when click specific key, call the methods created on Snake Class
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

# while loop until touch the border or the tail
is_on = True
while is_on:
    screen.update()  # update screen after screen.tracer
    time.sleep(0.1)
    snake.move()  # move method

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()  # create another random food
        score.increase_score()
        snake.extend()  # create another tail segment

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -290:
        score.reset_score()
        snake.reset_snake()

    # Detect collision with tail
    for segment in snake.my_snake[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_score()
            snake.reset_snake()

screen.exitonclick()
