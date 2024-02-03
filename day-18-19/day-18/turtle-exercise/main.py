from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

joe = Turtle()
joe.shape("circle")
# joe.color("red", "black")

# for _ in range(4):
#     joe.forward(100)
#     joe.left(90)

# for _ in range(15):
#     joe.forward(20)
#     joe.up()
#     joe.forward(20)
#     joe.down()

joe.speed(20)
# joe.pensize(2)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]

# # triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
# for i in range(3, 11):
#     angle = 360 / i
#     for j in range(i):
#         r = random.randint(0, 255)
#         g = random.randint(0, 255)
#         b = random.randint(0, 255)
#         joe.forward(100)
#         joe.right(angle)
#         joe.color(r, g, b)

# #  random walk (only 90 angles) and random color
# for _ in range(150):
#     angle = random.choice(directions)
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     joe.color((r, g, b))
#     joe.setheading((angle))
#     joe.forward(20)

#  360 circles with 100 radius
angle = 0
for _ in range(71):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    joe.color((r, g, b))
    joe.circle(100)
    angle += 5
    joe.setheading(angle)


screen.exitonclick()