from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto((-280, 250))
        self.level = 1
        self.updateScore()
    
    def updateScore(self):
        self.clear()
        self.write("Level: " + str(self.level), move=False, align="left", font=FONT)
        
    def increaseLevel(self):
        self.level += 1
        self.updateScore()
        
    def gameOver(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align="center", font=FONT)
    