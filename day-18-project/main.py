# import colorgram

# rgb_colors = []
# colors = colorgram.extract('day-18-project\hirst.jpg', 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)


import turtle as turtle_module
import random

turtle_module.colormode(255)
timmy = turtle_module.Turtle()
timmy.hideturtle()
timmy.penup()
timmy.speed("fastest")


# Extracted from colorgram; see script above
color_list = [
    (244, 238, 242), (237, 243, 240), (210, 155, 109), (52, 95, 137), (159, 82, 48), (222, 209, 109),
    (19, 36, 58), (127, 163, 196), (183, 163, 28), (54, 30, 19), (191, 141, 159), (126, 69, 93), (207, 91, 70),
    (47, 128, 71), (125, 180, 155), (159, 22, 13), (59, 30, 42), (128, 27, 44), (21, 52, 43), (192, 91, 111),
    (51, 167, 99), (41, 61, 96), (231, 165, 188), (26, 92, 52), (108, 119, 170), (226, 177, 168),
    (224, 206, 5), (10, 87, 104)
]


timmy.setheading(225)
timmy.forward(280)
timmy.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
