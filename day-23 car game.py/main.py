from turtle import Screen
import time
from player import Player
from car_manger import CarManger
from scoreboard import Scoreboard

#---------------------------------------------------------------------
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#---------------------------------------------------------------------
player = Player()
car_manger = CarManger()
scoreboard = Scoreboard()

#---------------------------------------------------------------------
screen.listen()
screen.onkey(player.go_up, "Up")

#---------------------------------------------------------------------
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    #---------------------------------------------------------------------
    car_manger.create_car()
    car_manger.move_cars()
    
    #---------------------------------------------------------------------
    # detect collision with car
    for car in car_manger.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            
    #---------------------------------------------------------------------
    # detect succesful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manger.level_up()
        scoreboard.increase_level()

screen.exitonclick()
