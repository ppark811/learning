from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 1
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.level = 0  
        
        
    def createCar(self):
        random_chance = random.randint(1,15)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)


    def moveCars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE + self.level)
        
        
    def increaseLevel(self):
        self.level += MOVE_INCREMENT
        
