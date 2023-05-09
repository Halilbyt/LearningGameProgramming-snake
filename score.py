from turtle import Turtle

FONT = font = ("Courier", 16, "bold")
SCORE_X_POSITION = 0
SCORE_Y_POSITION = 270
TEXT_ALIGNMENT = 'center'
COLOR = 'white'


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.score = 0
        self.penup()
        self.goto(SCORE_X_POSITION, SCORE_Y_POSITION)
        self.hideturtle()
        self.set_scoreboard()

    def set_scoreboard(self):
        self.write(f"Score : {self.score}", False,
                   align=TEXT_ALIGNMENT, font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.set_scoreboard()

    def gameover(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.setposition(0, 0)
        self.write("   GAME OVER!\nYour Score is: {}".format(self.score), True,
                   align=TEXT_ALIGNMENT, font=FONT)
