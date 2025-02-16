import turtle
from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(500, 400)

colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']
y_start = -100
turtles = []

is_race_on = False


user_bet = screen.textinput(title="Make your bet", prompt="Which color turtle will win?: ")

for i in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(-230, y_start)
    y_start += 30
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet.lower():
                print(f"You win! The {winner} turtle won the race")
                break
            else:
                print(f"You lost! The {winner} turtle won the race")
                break

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()