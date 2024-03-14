from turtle import Turtle,Screen

MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.x_vau=0
        self.y_vau=-280
        self.goto(self.x_vau,self.y_vau)


    def move_turtle(self):
        self.forward(MOVE_DISTANCE)
    def finish_line(self):
        self.y_vau *=-1
        self.goto(self.x_vau,self.y_vau)
