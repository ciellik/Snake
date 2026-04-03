from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 22, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.score = 0
        with open(r"data.txt", "r") as data:
            self.highscore = int(data.read())
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.write_score()

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(r"data.txt", "w") as data:
                data.write(str(self.highscore))
        self.score = 0
        self.write_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)