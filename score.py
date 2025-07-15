from turtle import Turtle
alingment = "center"
font = ("Arial",20,"normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0,y=290)
        self.scoring()

    def scoring(self):
        self.write(f"Score : {self.score}", align=alingment, font=font)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"Game Over", align=alingment, font=font)

    def inc_score(self):
        self.score += 1
        self.clear()
        self.scoring()
