from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__("square")
        self.color("white")
        self.shapesize(0.5)
        self.penup()
        self.bounce_heading = None
        self.start_heading()

    def start_heading(self):
        rand_degree = random.randint(0, 360)
        self.seth(rand_degree)

    def move_ball(self):
        self.forward(3)

    def bounce_ball(self, ball_heading):
        self.bounce_heading = ball_heading + 10
        self.seth(self.bounce_heading)






