from turtle import Turtle

FONT = ("Arial", 24, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def inc_score(self):
        self.score += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)