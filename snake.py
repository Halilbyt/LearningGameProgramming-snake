from turtle import Turtle

STARTIN_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
SPEED = 1
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_sneak()
        self.head = self.segments[0]

    def create_sneak(self):
        for position in STARTIN_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_snake = Turtle('square')
        new_snake.color('white')
        new_snake.speed(SPEED)
        new_snake.penup()
        new_snake.goto(position)
        self.segments.append(new_snake)

    def grow(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
