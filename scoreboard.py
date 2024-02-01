from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.sety(280)
        self.score = 0
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Your score is {self.score}", False, "center", ("Courier", 14, "normal"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()