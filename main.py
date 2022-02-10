from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
screen.listen()
screen.update()

my_snake = Snake()
food = Food()

score_board = Score()
game_on = True

screen.onkey(key="w", fun=my_snake.move_snake_up)
screen.onkey(key="s", fun=my_snake.move_snake_down)
screen.onkey(key="a", fun=my_snake.move_snake_left)
screen.onkey(key="d", fun=my_snake.move_snake_right)

while game_on:
    screen.update()
    time.sleep(0.1)
    my_snake.snake_moving()
    if my_snake.head.distance(food) < 15:
        food.refresh()
        score_board.increase_score()
        my_snake.grow()
    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() > 280 or my_snake.head.ycor() \
            < -280:
        game_on = False
        score_board.game_over()
    for segment in my_snake.segments[1:]:
        if my_snake.head.distance(segment) < 10:
            game_on = False
            score_board.game_over()

screen.exitonclick()