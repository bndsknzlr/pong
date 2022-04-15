from turtle import Turtle

STARTING_POSITIONS_pl1 = [(-560, 40), (-560, 23), (-560, 6), (-560, -11), (-560, -28)]
STARTING_POSITIONS_pl2 = [(560, 40), (560, 23), (560, 6), (560, -11), (560, -28)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Player1(Turtle):
    def __init__(self):
        super().__init__("square")
        self.penup()
        self.color("white")
        self.segments_pl1 = []
        self.shapesize(0.8)
        self.create()
        self.head_pl1 = self.segments_pl1[0]
        # self.goto(self.head_pl1)
        # self.move()

    def create(self):
        for position in STARTING_POSITIONS_pl1:
            self.add_segment(position)

    def add_segment(self, position_pls):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.shapesize(0.8)
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position_pls)
        self.segments_pl1.append(new_segment)

    def up(self):
        self.head_pl1.setheading(UP)
        self.move()

    def down(self):
        self.head_pl1.setheading(DOWN)
        self.move()

    def move(self):
        for seg_num in range(len(self.segments_pl1) - 1, 0, -1):
            new_x = self.segments_pl1[seg_num - 1].xcor()
            new_y = self.segments_pl1[seg_num - 1].ycor()
            self.segments_pl1[seg_num].goto(new_x, new_y)

        self.head_pl1.forward(MOVE_DISTANCE)


class Player2(Turtle):
    def __init__(self):
        super().__init__("square")
        self.penup()
        self.color("white")
        self.shapesize(0.8)
        self.head_pl2 = STARTING_POSITIONS_pl2[0]
        self.goto(self.head_pl2)

    def up(self):

        self.head_pl2.setheading(UP)

    def down(self):

        self.head_pl2.setheading(DOWN)







