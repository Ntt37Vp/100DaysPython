from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

# screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0) # Turns off the animation

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update() # Refresh for the animation
    ball.move()

screen.exitonclick()
