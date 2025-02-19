from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.title('Pong')
screen.tracer(0)

screen.listen()

LEFT_POSITION = (-350, 0)
RIGHT_POSITION = (350, 0)

l_paddle = Paddle(LEFT_POSITION)
r_paddle = Paddle(RIGHT_POSITION)

# screen.onkey(l_paddle.go_up, "w")
# screen.onkey(l_paddle.go_down, "s")
# screen.onkey(r_paddle.go_up, "Up")
# screen.onkey(r_paddle.go_down, "Down")

screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

ball = Ball()
scoreboard = Scoreboard()

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 400:
        scoreboard.l_point()
        ball.reset_position()

    if ball.xcor() < -400:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()