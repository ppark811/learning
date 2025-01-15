from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")

        # Change position
        self.penup()
        self.goto((0,270))
        self.hideturtle()
        
        self.showScore()
        
    def increaseScore(self):
        self.score += 1
        self.showScore()
        
    def showScore(self): # Define what the score shows
        self.clear()
        self.write("Score: " + str(self.score) + " High Score: " + str(self.high_score), move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))
            self.score = 0
            self.showScore()
        
    # def gameOver(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", move=False, align="center", font=("Courier", 16, "normal"))