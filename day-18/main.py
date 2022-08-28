import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color

# colors_defined = ["blue", "sea green", "chocolate", "yellow", "medium purple", "dodger blue",
# "cadet blue", "dark cyan",
#           "maroon", "light steel blue", "yellow green", "black",]

directions = [0, 90, 180, 270]
# speed = ["fastest", "fast", "normal", "slow", "slowest"]

timmy = Turtle()
timmy.shape("turtle")
timmy.speed("fastest")

# TODO 1 - Draw polygons starting from triangle to decagon
# def draw_shape(number_sides):
#     angle = 360 / number_sides
#     for i in range(number_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
#
# for shape_side_n in range(3, 21):
#     timmy.color(random.choice(colors))
#     draw_shape(shape_side_n)


# TODO 2 - Random Walk
# for i in range(199):
#     timmy.color(random_color())
#     timmy.speed(random.choice(speed))
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))
#
# print(timmy.position())


# TODO 3 - Spirograph
#
# def draw_spirograph(size_of_gap):
#     for i in range(int(360 / size_of_gap)):
#         timmy.color(random_color())
#         timmy.circle(100)
#         timmy.setheading(timmy.heading() + size_of_gap)
#
#
# draw_spirograph(5)







screen = Screen()
screen.exitonclick()
