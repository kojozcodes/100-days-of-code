from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


def read_high_score():
    with open("data.txt") as file:
        content = file.read()
    return content


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(read_high_score())
        self.color('white')
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def write_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def reset_s(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()

        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
