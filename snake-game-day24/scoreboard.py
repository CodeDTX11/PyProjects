from turtle import Turtle

FONT = ("Arial", 24, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        print(__file__)
        # with open("./snake-game-day24/data.txt") as data:
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def inc_score(self):
        self.score += 1
        self.clear()
        self.update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)