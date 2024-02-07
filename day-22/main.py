import time
from turtle import Screen
from ball import Ball
from scoreboard import Scoreboard
from paddle import Paddle
import datetime

# create screen object
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # delay the draw until update

# initiating right and left paddles objects with the corresponding position
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# initiating ball and scoreboard objects
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)  # control ball velocity with a delay
    screen.update()  # update the draw after the tracer(0)
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < 320:
        ball.bounce_x()

    # when right_paddle misses:
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset()

    # when left_paddle misses:
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset()

    # when someone wins the game
    if scoreboard.l_score > 90 or scoreboard.r_score > 90:
        scoreboard.game_over()
        is_game_on = False

screen.exitonclick()