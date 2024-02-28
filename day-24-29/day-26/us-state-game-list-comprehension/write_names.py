from turtle import Turtle


class WriteNames(Turtle):
    def __init__(self, state_name, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(state_name, align="left", font=("Courier", 12, "normal"))

#
#     def update_score(self, x, y, state_name):
#
