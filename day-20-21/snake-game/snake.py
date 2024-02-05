from turtle import Turtle

# constants
MOVE_DISTANCE = 20
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.my_snake = []
        self.x_pos = 0
        self.create_snake()
        self.head = self.my_snake[0]  # head position [0]

    def create_snake(self):
        for position in STARTING_POSITION:  # loop through tuple list
            self.add_segment(position)  # calling add_segment method

    # add new segment to a specif position parameter
    def add_segment(self, position):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.my_snake.append(new_snake)  # append new segment to our my_snake list

    def extend(self):
        self.add_segment(self.my_snake[-1].position())

    def move(self):
        for seg_num in range(len(self.my_snake) - 1, 0, -1):  # start, stop, step
            new_x = self.my_snake[seg_num - 1].xcor()
            new_y = self.my_snake[seg_num - 1].ycor()
            self.my_snake[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:  # the snake can't turn over in the opposite direction
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:  # the snake can't turn over in the opposite direction
            self.head.setheading(270)

    def right(self):
        if self.my_snake[0].heading() != 180:  # the snake can't turn over in the opposite direction
            self.my_snake[0].setheading(0)

    def left(self):
        if self.my_snake[0].heading() != 0:  # the snake can't turn over in the opposite direction
            self.my_snake[0].setheading(180)
