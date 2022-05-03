from turtle import Turtle

MOVE_DISTANCE = 17
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=0.75)
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 10
        self.goto(x=self.xcor(), y=new_y)

    def down(self):
        new_y = self.ycor() - 10
        self.goto(x=self.xcor(), y=new_y)

# Todo 3 : make paddle stop at boundary
