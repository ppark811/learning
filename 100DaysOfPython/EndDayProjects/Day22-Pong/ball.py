from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self, l_paddle, r_paddle):
        super().__init__()
        self.l_paddle = l_paddle
        self.r_paddle = r_paddle
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        
    def bounceY(self):
        self.y_move *= -1
    
    def bounceX(self):
        self.x_move *= -1
        self.move_speed *= 0.7
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move        
        self.goto(new_x, new_y)
        
    def resetPosition(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounceX()
