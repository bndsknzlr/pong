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
        new_x = self.xcor() + self.dir_x
        new_y = self.ycor() + self.dir_x * -1
        self.goto(new_x, new_y)

    def bounce_ball_paddle(self):
        new_x = self.xcor() * -1
        new_y = self.ycor()
        self.goto(new_x, new_y)

    # def bounce_ball(self, ball_heading):
    #     self.forward(0)
    #     self.bounce_heading = ball_heading *2
    #     self.seth(self.bounce_heading)
    #     self.forward(4)
