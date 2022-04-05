from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.write(f"Score: {self.score}",align="center",font=("Arial",14,"normal"))
        self.hideturtle()

    def game_over(self):
        self.home()
        self.write("Game Over", align="center", font=("Arial", 14, "normal"))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 14, "normal"))