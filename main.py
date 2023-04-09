from turtle import Screen
from paddle import Paddle

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.move_up)
screen.onkeypress(key="Down", fun=r_paddle.move_down)
screen.onkeypress(key="w", fun=l_paddle.move_up)
screen.onkeypress(key="s", fun=l_paddle.move_down)

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()