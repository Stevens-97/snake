from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.penup()
        self.hideturtle()
        self.goto(x=-30, y=280)
        self.color("white")
        self.counter = 0
        self.write(f"Score: {self.counter}", False, align="left", font=("Arial", 12, "normal"))

    def increase_score(self):
        self.counter += 1
        self.clear()
        self.write(f"Score: {self.counter}", False, align="left", font=("Arial", 12, "normal"))

    def game_over(self):
        self.clear()
        self.goto(-65,0)
        self.write(f"GAMEOVER! Score: {self.counter}", False, align="left", font=("Arial", 12, "normal"))


