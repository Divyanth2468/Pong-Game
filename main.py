from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()

paddle1 = Paddle(xcor=350, ycor=0)
paddle2 = Paddle(xcor=-350, ycor=0)
ball = Ball()

score = Score()

screen.tracer(0)

screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.colormode(255)
screen.bgcolor("black")

screen.onkey(fun=paddle1.up, key="Up")
screen.onkey(fun=paddle1.down, key="Down")
screen.onkey(fun=paddle2.up, key="w")
screen.onkey(fun=paddle2.down, key="s")

play = True

while play:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.xcor() > 320 and ball.distance(paddle1) < 50 or ball.xcor() < -320 and ball.distance(paddle2) < 50:
        ball.bounce_x()
    elif ball.xcor() > 400:
        ball.reset()
        score.left_score()
    elif ball.xcor() < -400:
        ball.reset()
        score.right_score()


screen.exitonclick()
