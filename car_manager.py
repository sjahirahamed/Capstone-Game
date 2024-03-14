from turtle import Turtle, Screen
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
RANDOM_VAR_CAR = random.randint(10, 15)


class CarManager:

    def __init__(self):
        self.x_vau = 0  # Initialize x_vau
        self.y_vau = 0  # Initialize y_vau
        self.speed_of_car=0.1
        self.all_car=[]

    def create(self):
        random_num_car=random.randint(1,6)
        if random_num_car==1:
            car_turtle = Turtle()
            car_turtle.shapesize(1,2)
            self.y_vau = random.randint(-280, 280)
            car_turtle.shape("square")
            car_turtle.penup()
            car_turtle.color(random.choice(COLORS))
            car_turtle.goto(300, self.y_vau)
            self.all_car.append(car_turtle)
    def move_car(self):
        for car in self.all_car:
            car.backward(STARTING_MOVE_DISTANCE)













