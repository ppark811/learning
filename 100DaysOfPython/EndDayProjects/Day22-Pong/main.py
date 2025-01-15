import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

# generate screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# initiate scoreboard
l_score = ScoreBoard((100,200))
r_score = ScoreBoard((-100, 200))

# run game

# Generate user paddles
l_paddle = Paddle((-350,0))  #user paddle
r_paddle = Paddle((350,0)) #computer paddle

# listen for screen strokes for both paddles
screen.listen()
screen.onkeypress(l_paddle.goUp, "w")
screen.onkeypress(l_paddle.goDown, "s")
screen.onkeypress(r_paddle.goUp, "Up")
screen.onkeypress(r_paddle.goDown, "Down")

# initiate ball class
ball = Ball(l_paddle, r_paddle)
sleep_time = 0.1

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    
    ball.move()
    
    # check if ball hits upper or lower wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()
    
    # check if ball hits r_paddle
    if ball.xcor() == 330 and ball.distance(r_paddle) < 63:  # check ball's x-coord and check ball's y-coord wrt paddle
        ball.bounceX()
    
    # check if ball hits l_paddle
    if ball.xcor() == -330 and ball.distance(l_paddle) < 63: # check ball's x-coord and check ball's y-coord wrt paddle
        ball.bounceX()
    
    # check if ball goes beyond r_paddle
    if ball.xcor() > 380: 
        r_score.increaseScore()
        ball.resetPosition()
    
    # check if ball goes beyond l_paddle
    if ball.xcor() < -380:
        l_score.increaseScore()
        ball.resetPosition()


screen.exitonclick()