from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.createPaddle()
    
    
    def createPaddle(self):
        self.shape("square")
        self.penup()
        self.goto(self.position)
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        
        
    def goUp(self):
        if self.ycor() < 250: # don't let paddle go out of screen
            new_y = self.ycor() + 50
            self.goto(self.xcor(), new_y)
    
    
    def goDown(self):
        if self.ycor() > -250: # don't let paddle go out of screen
            new_y = self.ycor() - 50
            self.goto(self.xcor(), new_y)
            
    