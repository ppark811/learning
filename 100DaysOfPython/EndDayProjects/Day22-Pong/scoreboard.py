from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 60, "normal")

class ScoreBoard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.penup()
        self.color("white")
        self.goto(position)
        self.score = 0
        
        self.hideturtle()
        self.showScore()
        
        
    def increaseScore(self):
        self.score += 1
        self.clear()
        self.showScore()
        
        
    def showScore(self):
        self.write(str(self.score), move=False, align=ALIGNMENT, font=FONT)