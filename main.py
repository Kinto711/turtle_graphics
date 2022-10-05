from turtle import Turtle, Screen
import random

colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]
path = ["forward", "right", "left", "backward"]


tim = Turtle()
tim.pensize(10)


def ran_walk():
    while True:
        ran_color = random.choice(colors)
        ran_path_length = random.randint(1,100)
        ran_angle = random.randint(1,360)
        ran_path = random.choice(path)
        if ran_path == "forward":
            tim.color(ran_color)
            tim.forward(ran_path_length)
        elif ran_path == "backward":
            tim.color(ran_color)
            tim.backward(ran_path_length)
        elif ran_path == "right":
            tim.color(ran_color)
            tim.right(ran_angle)
            tim.forward(ran_path_length)
        elif ran_path == "left":
            tim.color(ran_color)
            tim.left(ran_angle)
            tim.forward(ran_path_length)

ran_walk()






















# def draw_shape(num_of_sides):
#     angle = 360 / num_of_sides
#     for i in range(num_of_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for side in range(3,11):
#     draw_shape(side)

# for i in range(4):
#
#     tim.forward(50)
#     tim.right(90)
#
# for i in range(3):
#     tim.forward(50)
#     tim.right(120)
#
# for i in range(5):
#     tim.forward(50)
#     tim.right(72)
#
# for i in range(6):
#     tim.forward(50)
#     tim.right(60)
#
#
# for i in range(7):
#     tim.forward(50)
#     tim.right(51.4)




screen = Screen()
screen.exitonclick()
