from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

paddle_1 = Paddle(350, 0)
screen.onkey(paddle_1.up, "Up")  # Bind the Up arrow key to paddle.up
screen.onkey(paddle_1.down, "Down")

paddle_2 = Paddle(-350,0)
screen.onkey(paddle_2.up, "w")
screen.onkey(paddle_2.down, "s")

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()
    scoreboard.update_scoreboard()

    # detect collision with right paddle
    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) <50 and ball.xcor() < -320:
        ball.bounce_x()

    # right paddle miss
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    # left paddle miss
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()
