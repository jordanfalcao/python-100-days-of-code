from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=500)

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color "
                                                          "(red/orange/yellow/green/cyan/blue/purple): ").lower()

my_turtles = []
y_pos = -180

for i in range(7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.up()
    new_turtle.goto(x=-230, y=y_pos)
    my_turtles.append(new_turtle)
    y_pos += 60

for i in range(7):
    my_turtles[i].speed(40)

print(my_turtles)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in my_turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! The {winning_color} is the winner!")
            else:
                print(f"You lost! The {winning_color} is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()