import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280

# Create Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Generate player
player = Player()

# Generate cars manager
car_manager = CarManager()

# Generate scoreboard (level)
scoreboard = Scoreboard()

# Listen for keystrokes (also, if a key is held down, continue the action)
screen.listen()
screen.onkeypress(player.move, "Up")


# Run game
game_is_on = True
while game_is_on:
    time.sleep(0.016)
    screen.update()
    
    # Create cars
    car_manager.createCar()
    car_manager.moveCars()
    
    # Player collision with car
    for car in car_manager.all_cars:    
        if player.distance(car) < 20:
            scoreboard.gameOver()
            game_is_on = False    
    
    # Finish Line reached condition
    if player.isAtFinishLine():
        player.goToStart()
        scoreboard.increaseLevel()
        car_manager.increaseLevel()
        

screen.exitonclick()