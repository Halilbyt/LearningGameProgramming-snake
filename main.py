from turtle import Screen
import time
from snake import Snake
from food import Food
from score import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)


snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

screen.update()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 24:
        food.refresh()
        snake.grow()
        score.increase_score()

    # Detect collision with the wall
    if snake.head.xcor() > 388 or snake.head.xcor() < -388 or snake.head.ycor() > 288 or snake.head.ycor() < -288:
        score.reset()
        snake.reset()

    #  Detect collision with tail
    for segment in snake.segments[:1]:

        if segment == snake.head:
            pass

        elif snake.head.distance(segment) < 10:

            score.reset()
            snake.reset()

screen.exitonclick()
