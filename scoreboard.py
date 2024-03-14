from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape()
        self.penup()
        self.hideturtle()
        self.level_no= 1
        self.level_turtle()

    def level_turtle(self):
        self.goto(x=-200, y=250)
        self.write(arg=f"Level : {self.level_no} ",align="center",font=FONT)
    def incr_turtle(self):
        self.level_no += 1
        self.clear()
        self.level_turtle()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER ", move=False, align="center")



