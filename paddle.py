import turtle
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, xcor, ycor):
        super().__init__()
        self.penup()
        self.color("white")
        self.turtlesize(stretch_len=1, stretch_wid=5)
        self.shape("square")
        self.goto(xcor, ycor)
        turtle.listen()

    def up(self):
        ycor = self.ycor()
        xcor = self.xcor()
        self.goto(x=xcor, y=ycor+20)

    def down(self):
        ycor = self.ycor()
        xcor = self.xcor()
        self.goto(x=xcor, y=ycor-20)

