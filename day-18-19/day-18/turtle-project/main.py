# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

#  the code above is just to catch the list below
color_list = [(213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31), (115, 155, 171), (124, 79, 99),
              (122, 175, 156), (226, 198, 131), (192, 87, 108), (11, 50, 64), (55, 38, 19), (45, 168, 126),
              (47, 127, 123), (200, 121, 143), (168, 21, 29), (228, 92, 77), (244, 162, 160), (38, 32, 35), (2, 25, 24),
              (78, 147, 171), (170, 23, 18), (19, 79, 90), (101, 126, 158), (235, 166, 171), (177, 204, 185),
              (49, 62, 84)]

from turtle import Turtle, Screen
import turtle
import random

turtle.colormode(255)
joe = Turtle()

joe.hideturtle()
joe.speed(60)
joe.up()  # the turtle doesn't need to touch the floor to draw dot

joe.setposition(-270, -250)  # Starting position

ypos = joe.ycor()  # Y coordinates

for y in range(1, 11):

    for x in range(1, 11):
        joe.dot(20, random.choice(color_list))
        joe.forward(50)

    joe.sety((ypos + 50 * y))  # moves turtle up one row with each iteration
    joe.setx(-270)


screen = Screen()
screen.exitonclick()
