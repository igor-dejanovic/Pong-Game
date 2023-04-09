from turtle import Screen
from paddle import Paddle

paddle = Paddle()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


screen.listen()
screen.onkeypress(key="Up", fun=paddle.move_up)
screen.onkeypress(key="Down", fun=paddle.move_down)

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()