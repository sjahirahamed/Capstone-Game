import time
from turtle import Screen
from player import Player,FINISH_LINE_Y
from car_manager import CarManager,RANDOM_VAR_CAR
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
car=CarManager()
score=Scoreboard()
screen.listen()
screen.onkey(player.move_turtle, key="Up")



#Make the turtle to repeat
game_is_on = True

while game_is_on:
    time.sleep(car.speed_of_car)#speed of the car
    screen.update()
    car.create()
    car.move_car()#moving car forward

    #Check if the player cross the screen then level up from first position
    if player.ycor() > FINISH_LINE_Y:
        player.finish_line()#this were the player go the first position
        #Make the level up
        if player.ycor()==-280:
            score.incr_turtle()
            car.speed_of_car *= 0.95#increase speed of the car
    #Detect the player collision with car
    for car_one_manager in car.all_car:
        if player.distance(car_one_manager) < 15:
            game_is_on = False
            score.game_over()



screen.exitonclick()

