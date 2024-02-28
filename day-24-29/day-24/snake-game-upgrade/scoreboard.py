from turtle import Turtle

# constants
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:  # open and read data.txt file
            self.highscore = int(file.read())  # sets the var to the file content
        self.color("White")
        self.up()
        self.goto(0, 265)  # position
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=FONT)

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:  # write high score in the file 'data.txt'
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=FONT)

    def increase_score(self):
        self.score += 10
        self.update_scoreboard()
