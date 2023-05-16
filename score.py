from turtle import Turtle
import os

FONT = font = ("Courier", 16, "bold")
SCORE_X_POSITION = 0
SCORE_Y_POSITION = 270
TEXT_ALIGNMENT = 'center'
COLOR = 'white'
PATH = r"C:\Users\D4rkS\Desktop\projects\python100days\snake_game\high_score.txt"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.score = 0
        self.high_score = self.read_hight_score()
        self.penup()
        self.goto(SCORE_X_POSITION, SCORE_Y_POSITION)
        self.hideturtle()
        self.set_scoreboard()

    def set_scoreboard(self):
        self.write(f"Score : {self.score} High Score: {self.high_score}", False,
                   align=TEXT_ALIGNMENT, font=FONT)

    def update(self):
        self.clear()
        self.set_scoreboard()

    def gameover(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.setposition(0, 0)
        self.write("   GAME OVER!\nYour Score is: {}".format(self.score), True,
                   align=TEXT_ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        # if you want to high_score change every iteration then put this line of code inside the if intendation
        self.save_high_score()
        self.score = 0
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()

    def save_high_score(self):
        isFile = os.path.isfile(PATH)
        # put this conditions becouse if you want to all score would be saved
        if isFile:
            with open("high_score.txt", mode='a') as file:
                file.write(str(self.high_score)+"\n")
        else:
            with open('high_score.txt', mode='w') as file:
                file.write(str(self.high_score)+"\n")

    def read_hight_score(self):
        isFile = os.path.isfile(PATH)
        if isFile:
            with open("high_score.txt", "r") as file:
                return int(file.readline()[-1])
        else:
            return 0
