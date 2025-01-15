from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")

        # Change position
        self.penup()
        self.goto((0,270))
        self.hideturtle()
        
        self.showScore()
        
    def increaseScore(self):
        self.score += 1
        self.clear()
        self.showScore()
        
    def showScore(self): # Define what the score shows
        self.write("Score: " + str(self.score), move=False, align=ALIGNMENT, font=FONT)
        
    def gameOver(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align="center", font=("Courier", 16, "normal"))