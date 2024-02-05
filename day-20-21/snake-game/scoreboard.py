from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.up()
        self.goto(0, 265)
        self.write(f"Score: {self.score}", align="center", font=FONT)
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)


    def increase_score(self):
        self.score += 10
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
