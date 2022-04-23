from turtle import Turtle

MOVE_DISTANCE = 17
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__("square")
        self.penup()
        self.color("white")
        self.setheading(UP)
        self.shapesize(stretch_wid=0.75, stretch_len=5)
        self.goto(position)

    def up(self):
        self.setheading(UP)
        self.forward(30)

    def down(self):
        self.setheading(DOWN)
        self.forward(30)


# Todo 3 : make paddle stop at boundary
