from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# generate screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# initialize classes
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# listen for keystrokes to command snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# run game
game_is_on = True

while game_is_on:
        
    # screen refresh rate
    screen.update()
    time.sleep(0.1)
    
    # move the snake
    snake.move()
    
    # detect collision with food and make it longer
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increaseScore()
        snake.newSegment()
        
    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        #scoreboard.gameOver()
        #game_is_on = False
        
    # detect collision with any segment in tail
    for segment in snake.segments[1:]: #list slicing
        if snake.head.distance(segment) < 10:
            snake.reset()
            scoreboard.reset()
            #game_is_on = False
            
screen.exitonclick()
