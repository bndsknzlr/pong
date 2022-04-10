from turtle import Turtle

SCORE_NUMBERS = [{0: [(- 100, 360), (- 100, 350), (- 100, 340), (- 100, 330), (- 100, 320),
                      (- 110, 310), (- 120, 310), (- 110, 370), (- 120, 370),
                      (- 130, 360), (- 130, 350), (- 130, 340), (- 130, 330), (- 130, 320), ]},
                 {1: [(- 100, 370), (- 100, 360), (- 100, 350), (- 100, 340), (- 100, 330), (- 100, 320),
                      (- 100, 310)]},
                 {2: [(- 130, 370), (- 120, 370), (- 110, 370), (- 100, 360),
                      (- 100, 350), (- 110, 340), (- 120, 340), (- 130, 340),
                      (- 140, 330), (- 140, 320), (- 130, 310), (- 120, 310), (- 110, 310)]},
                 {3: [(- 100, 360), (- 100, 350), (- 100, 340), (- 100, 330), (- 100, 320),
                      (- 130, 370), (- 120, 370), (- 110, 370),
                      (- 130, 310), (- 120, 310), (- 110, 310), (- 110, 340)]},
                 {4: [(- 100, 340), (- 110, 340), (- 120, 340), (- 130, 340), (- 140, 340), (- 120, 350),
                      (- 120, 330), (- 120, 320), (- 120, 310), (- 140, 350), (- 140, 360), (- 140, 370)]},
                 {5: [(- 130, 370), (- 120, 370), (- 110, 370), (- 140, 360),
                      (- 140, 350), (- 130, 340), (- 120, 340), (- 110, 340),
                      (- 100, 330), (- 100, 320), (- 110, 310), (- 120, 310), (- 130, 310)]},
                 {6: [(- 130, 370), (- 120, 370), (- 110, 370), (- 140, 360),
                      (- 140, 350), (- 140, 340), (- 140, 330), (- 140, 320), (- 130, 340), (- 120, 340),
                      (- 110, 340), (- 100, 330), (- 100, 320), (- 110, 310), (- 120, 310), (- 130, 310)]},
                 {7: [(- 140, 370), (- 130, 370), (- 120, 370), (- 110, 370), (- 100, 370), (- 100, 360),
                      (- 100, 350), (- 100, 340), (- 100, 330), (- 100, 320),
                      (- 100, 310)]},
                 {8: [(- 100, 360), (- 100, 350), (- 110, 340), (- 120, 340), (- 100, 330), (- 100, 320),
                      (- 110, 310), (- 120, 310), (- 110, 370), (- 120, 370),
                      (- 130, 360), (- 130, 350), (- 130, 330), (- 130, 320), ]},
                 {9: [(- 100, 360), (- 100, 350), (- 110, 340), (- 120, 340), (- 100, 330), (- 100, 320),
                      (- 110, 310), (- 120, 310), (- 110, 370), (- 120, 370),
                      (- 130, 360), (- 130, 350)]}

                 ]


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.block = None
        self.pl_1_score = 0
        self.pl_2_score = 0
        self.hideturtle()
        self.build_start_score()

    def track_score_pl1(self):
        self.pl_1_score += 1
        score_count_pl1 = self.pl_1_score
        self.build_score_pl1(score_count_pl1)

    def track_score_pl2(self):
        self.pl_1_score += 1
        score_count_pl2 = self.pl_2_score
        self.build_score_pl2(score_count_pl2)

    def build_start_score(self):
        self.build_score_pl1(0)
        self.build_score_pl2(0)

    def build_score_pl1(self, score_count_pl1):
        """takes the score count and builds the score gfx"""
        for limbo in SCORE_NUMBERS[score_count_pl1][score_count_pl1]:
            self.block = Turtle("square")
            self.block.shapesize(0.5)
            self.block.penup()
            self.block.color('white')
            self.block.goto(limbo)
            print(limbo)

    def build_score_pl2(self, score_count_pl2):
        for limbo in SCORE_NUMBERS[score_count_pl2][score_count_pl2]:
            self.block = Turtle("square")
            self.block.shapesize(0.5)
            self.block.penup()
            self.block.color('white')
            limbo_list = list(limbo)
            neg_list = []
            for items in limbo_list[1:]:
                limbo_neg = float(items * -1)
                neg_list.append(limbo_neg)
            neg_limbo = tuple(neg_list)
            # fixme 1. : just one parameter changes - needs two
            self.block.goto(neg_limbo)
            print(neg_limbo)
