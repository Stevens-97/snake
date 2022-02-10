from turtle import Turtle, Screen
import main


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
screen.listen()
screen.update()

screen.onkey(key="w", fun=my_snake.move_snake_up)
screen.onkey(key="s", fun=my_snake.move_snake_down)
screen.onkey(key="a", fun=my_snake.move_snake_left)
screen.onkey(key="d", fun=my_snake.move_snake_right)