from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__("square")
        self.color("white")
        self.shapesize(0.75)
        self.penup()
        self.dir_x = 10
        self.dir_y = 10

    def move_ball(self):
        new_x = self.xcor() + self.dir_x
        new_y = self.ycor() + self.dir_y
        self.goto(new_x, new_y)

    def bounce_ball_wall(self):
        self.dir_y *= -1

    def bounce_ball_paddle(self):
        self.dir_x *= -1

    def reset_ball(self):
        self.goto(0, 0)
