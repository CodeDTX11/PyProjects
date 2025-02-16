import turtle
from turtle import Turtle, Screen
import random
import colorgram

colors = ["red", "green", "blue", "wheat", "black", "grey", "purple", "SeaGreen", "DarkOrchid", "pink"]

tim = Turtle()
screen = Screen()
# tim.shape("turtle")

def draw_shape(sides):
    for _ in range(sides):
        tim.forward(100)
        tim.right(360 / sides)

# for num_sides in range(3,11):
#     tim.color(random.choice(colors))
#     draw_shape(num_sides)
turtle.colormode(255)

def rand_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    # r = random.randint(0, 255)
    # g = random.randint(0, 255)
    # b = random.randint(0, 255)
    # color_tuple = (r, g, b)
    # return color_tuple
    # return r, g, b

# tim.width(15)
# tim.speed(7)
# direction = [0, 90, 180, 270]

# for i in range(100):
#     tim.color(rand_color())
#     tim.setheading(random.choice(direction))
#     tim.forward(30)


turtle.colormode(255)
rgb = []
color_extract = colorgram.extract("item.jpg", 20)

for color in color_extract:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb.append((r,g,b))
# print(rgb)

for _ in range(20):
    tim.dot(20, random.choice(rgb))
    tim.forward(50)


screen.exitonclick()
