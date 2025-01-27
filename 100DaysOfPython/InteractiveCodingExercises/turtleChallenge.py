from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
#tim.color("red")
colors = ["red", "blue","green", "orange","yellow","purple","black","pink"]
angle = [90, 180, 270, 360]


pace = 50
tim.pensize(5)
tim.speed(10)
# for i in range(3, 11):
#     sides = i
#     tim.color(random.choice(colors))
#     angle = 360/i
#     for j in range (0,i):
#         tim.forward(pace)
#         tim.left(angle)

# for i in range(0,100):
#     tim.forward(pace)
#     tim.left(random.choice(angle))
#     tim.color(random.choice(colors))








screen = Screen()
screen.exitonclick()