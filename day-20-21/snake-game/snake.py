from turtle import Turtle, Screen

MOVE_DISTANCE = 20
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.my_snake = []
        self.x_pos = 0
        self.create_snake()
        self.head = self.my_snake[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.my_snake.append(new_snake)

    def extend(self):
        self.add_segment(self.my_snake[-1].position())

    def move(self):
        for seg_num in range(len(self.my_snake) - 1, 0, -1):  # start, stop, step
            new_x = self.my_snake[seg_num - 1].xcor()
            new_y = self.my_snake[seg_num - 1].ycor()
            self.my_snake[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.my_snake[0].heading() != 180:
            self.my_snake[0].setheading(0)

    def left(self):
        if self.my_snake[0].heading() != 0:
            self.my_snake[0].setheading(180)
