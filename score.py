from turtle import Turtle

SCORE_NUMBERS_pl1 = [{0: [(- 100, 360), (- 100, 350), (- 100, 340), (- 100, 330), (- 100, 320),
                          (- 110, 310), (- 120, 310), (- 110, 370), (- 120, 370),
                          (- 130, 360), (- 130, 350), (- 130, 340), (- 130, 330), (- 130, 320), ]},
                     {1: [(- 100, 370), (- 100, 360), (- 100, 350), (- 100, 340), (- 100, 330), (- 100, 320),
                          (- 100, 310)]},
                     {2: [(- 130, 370), (- 120, 370), (- 110, 370), (- 100, 360),
                          (- 100, 350), (- 110, 340), (- 120, 340), (- 130, 340),
                          (- 140, 330), (- 140, 320), (- 130, 310), (- 120, 310), (- 110, 310)]},
                     {3: [(- 100, 360), (- 100, 350), (- 100, 330), (- 100, 320),
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

SCORE_NUMBERS_pl2 = [{0: [(- 100, 360), (- 100, 350), (- 100, 340), (- 100, 330), (- 100, 320),
                          (- 110, 310), (- 120, 310), (- 110, 370), (- 120, 370),
                          (- 130, 360), (- 130, 350), (- 130, 340), (- 130, 330), (- 130, 320), ]},
                     {1: [(- 140, 370), (- 140, 360), (- 140, 350), (- 140, 340), (- 140, 330), (- 140, 320),
                          (- 140, 310)]},
                     {2: [(- 130, 370), (- 120, 370), (- 110, 370), (- 140, 360),
                          (- 140, 350), (- 110, 340), (- 120, 340), (- 130, 340),
                          (- 100, 330), (- 100, 320), (- 130, 310), (- 120, 310), (- 110, 310)]},
                     {3: [(- 140, 360), (- 140, 350), (- 140, 330), (- 140, 320),
                          (- 130, 370), (- 120, 370), (- 110, 370),
                          (- 130, 310), (- 120, 310), (- 110, 310), (- 130, 340)]},
                     {4: [(- 100, 340), (- 110, 340), (- 120, 340), (- 130, 340), (- 140, 340), (- 120, 350),
                          (- 120, 330), (- 120, 320), (- 120, 310), (- 100, 350), (- 100, 360), (- 100, 370)]},
                     {5: [(- 130, 370), (- 120, 370), (- 110, 370), (- 100, 360),
                          (- 100, 350), (- 110, 340), (- 120, 340), (- 130, 340),
                          (- 140, 330), (- 140, 320), (- 110, 310), (- 120, 310), (- 130, 310)]},
                     {6: [(- 130, 370), (- 120, 370), (- 110, 370), (- 100, 360),
                          (- 100, 350), (- 100, 340), (- 140, 330), (- 140, 320), (- 130, 340), (- 120, 340),
                          (- 110, 340), (- 100, 330), (- 100, 320), (- 110, 310), (- 120, 310), (- 130, 310)]},
                     {7: [(- 140, 370), (- 130, 370), (- 120, 370), (- 110, 370), (- 100, 370), (- 140, 360),
                          (- 140, 350), (- 140, 340), (- 140, 330), (- 140, 320),
                          (- 140, 310)]},
                     {8: [(- 100, 360), (- 100, 350), (- 110, 340), (- 120, 340), (- 100, 330), (- 100, 320),
                          (- 110, 310), (- 120, 310), (- 110, 370), (- 120, 370),
                          (- 130, 360), (- 130, 350), (- 130, 330), (- 130, 320), ]},
                     {9: [(- 100, 360), (- 100, 350), (- 110, 340), (- 120, 340), (- 130, 330), (- 130, 320),
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
        if score_count_pl1 < 10:
            for limbo in SCORE_NUMBERS_pl1[score_count_pl1][score_count_pl1]:
                self.block = Turtle("square")
                self.block.shapesize(0.5)
                self.block.penup()
                self.block.color('white')
                self.block.goto(limbo)
        else:
            score_str = str(score_count_pl1)
            fst_digit = int(score_str[0])
            sec_digit = int(score_str[1])
            for limbo in SCORE_NUMBERS_pl1[sec_digit][sec_digit]:
                self.block = Turtle("square")
                self.block.shapesize(0.5)
                self.block.penup()
                self.block.color('white')
                self.block.goto(limbo)
            for limbo in SCORE_NUMBERS_pl1[fst_digit][fst_digit]:
                self.block = Turtle("square")
                self.block.shapesize(0.5)
                self.block.penup()
                self.block.color('white')
                limbo_list = list(limbo)
                # print(limbo_list)
                # print(limbo_list[0])
                limbo_left = limbo_list[0] - 70
                # print(limbo_left)
                limbo_list[0] = limbo_left
                limbo_list_tuple = tuple(limbo_list)
                # print(limbo_list_tuple)
                self.block.goto(limbo_list_tuple)

    def build_score_pl2(self, score_count_pl2):
        """takes score_count for player two as an input and builds score from list SCORE NUMBERS"""
        if score_count_pl2 < 10:
            for limbo in SCORE_NUMBERS_pl2[score_count_pl2][score_count_pl2]:
                self.block = Turtle("square")
                self.block.shapesize(0.5)
                self.block.penup()
                self.block.color('white')
                limbo_list = list(limbo)
                # print(limbo_list)
                # print(limbo_list[0])
                limbo_neg = limbo_list[0] * -1
                # print(limbo_neg)
                limbo_list[0] = limbo_neg
                limbo_list_tuple = tuple(limbo_list)
                # print(limbo_list_tuple)
                self.block.goto(limbo_list_tuple)
        else:
            score_str_2 = str(score_count_pl2)
            fst_digit_2 = int(score_str_2[0])
            sec_digit_2 = int(score_str_2[1])
            for limbo in SCORE_NUMBERS_pl2[fst_digit_2][fst_digit_2]:
                self.block = Turtle("square")
                self.block.shapesize(0.5)
                self.block.penup()
                self.block.color('white')
                limbo_list = list(limbo)
                # print(limbo_list)
                # print(limbo_list[0])
                limbo_neg = limbo_list[0] * -1
                # print(limbo_neg)
                limbo_list[0] = limbo_neg
                limbo_list_tuple = limbo_list
                # print(limbo_list_tuple)
                self.block.goto(limbo_list_tuple)
            for limbo in SCORE_NUMBERS_pl2[sec_digit_2][sec_digit_2]:
                self.block = Turtle("square")
                self.block.shapesize(0.5)
                self.block.penup()
                self.block.color('white')
                limbo_list = list(limbo)
                # print(limbo_list)
                # print(limbo_list[0])
                limbo_neg = limbo_list[0] * -1 + 40
                # print(limbo_neg)
                limbo_list[0] = limbo_neg
                limbo_list_tuple = tuple(limbo_list)
                # print(limbo_list_tuple)
                self.block.goto(limbo_list_tuple)

# fixme 1 : position number 1
# fixme 2 : limbo list tuple
