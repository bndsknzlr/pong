from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__("turtle")
        self.color("white")
        self.shapesize(0.75)
        self.penup()
        self.bounce_heading = None
        self.start_heading()

    def start_heading(self):
        rand_degree = random.randint(0, 360)
        self.seth(rand_degree)

    def move_ball(self):
        self.forward(20)

    def bounce_ball(self, ball_heading):
        self.bounce_heading = ball_heading * 2
        self.seth(self.bounce_heading)






