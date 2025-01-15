from turtle import Turtle

class NameLocation(Turtle):
    def __init__(self):
        super().__init__()
        
        self.penup()
        self.color("black")
        self.hideturtle()
        
    def stateLocation(self, state, location):
        self.goto(location)
        self.write(state)
