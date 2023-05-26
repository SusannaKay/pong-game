from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard()

POS_RIGHT = (350, 0)
POS_LEFT = (-350, 0)

pad_right = Paddle(POS_RIGHT)
pad_left = Paddle(POS_LEFT)
ball = Ball()

screen.listen()
screen.onkey(pad_right.up, "Up")
screen.onkey(pad_right.down, "Down")
screen.onkey(pad_left.up, "w")
screen.onkey(pad_left.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Collisione con il tetto
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Collisione con i player
    if ball.distance(pad_right) < 50 and ball.xcor() > 320 or ball.distance(pad_left) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    # se il player di sinistra perde la palla
    if ball.xcor() < -400:
        ball.reset_ball()
        scoreboard.r_point()
        screen.update()

# se il player di destra perde la palla
    if ball.xcor() > 400:
        ball.reset_ball()
        scoreboard.l_point()
        screen.update()

screen.exitonclick()
