from turtle import Turtle

SCORE_NUMBERS_pl1 = [{0: [(- 100, 260), (- 100, 250), (- 100, 240), (- 100, 230), (- 100, 220),
                          (- 110, 210), (- 120, 210), (- 110, 270), (- 120, 270),
                          (- 130, 260), (- 130, 250), (- 130, 240), (- 130, 230), (- 130, 220), ]},
                     {1: [(- 100, 270), (- 100, 260), (- 100, 250), (- 100, 240), (- 100, 230), (- 100, 220),
                          (- 100, 210)]},
                     {2: [(- 130, 270), (- 120, 270), (- 110, 270), (- 100, 260),
                          (- 100, 250), (- 110, 240), (- 120, 240), (- 130, 240),
                          (- 140, 230), (- 140, 220), (- 130, 210), (- 120, 210), (- 110, 210)]},
                     {3: [(- 100, 260), (- 100, 250), (- 100, 230), (- 100, 220),
                          (- 130, 270), (- 120, 270), (- 110, 270),
                          (- 130, 210), (- 120, 210), (- 110, 210), (- 110, 240)]},
                     {4: [(- 100, 240), (- 110, 240), (- 120, 240), (- 130, 240), (- 140, 240), (- 120, 250),
                          (- 120, 230), (- 120, 220), (- 120, 210), (- 140, 250), (- 140, 260), (- 140, 270)]},
                     {5: [(- 130, 270), (- 120, 270), (- 110, 270), (- 140, 260),
                          (- 140, 250), (- 130, 240), (- 120, 240), (- 110, 240),
                          (- 100, 230), (- 100, 220), (- 110, 210), (- 120, 210), (- 130, 210)]},
                     {6: [(- 130, 270), (- 120, 270), (- 110, 270), (- 140, 260),
                          (- 140, 250), (- 140, 240), (- 140, 230), (- 140, 220), (- 130, 240), (- 120, 240),
                          (- 110, 240), (- 100, 230), (- 100, 220), (- 110, 210), (- 120, 210), (- 130, 210)]},
                     {7: [(- 140, 270), (- 130, 270), (- 120, 270), (- 110, 270), (- 100, 270), (- 100, 260),
                          (- 100, 250), (- 100, 240), (- 100, 230), (- 100, 220),
                          (- 100, 210)]},
                     {8: [(- 100, 260), (- 100, 250), (- 110, 240), (- 120, 240), (- 100, 230), (- 100, 220),
                          (- 110, 210), (- 120, 210), (- 110, 270), (- 120, 270),
                          (- 130, 260), (- 130, 250), (- 130, 230), (- 130, 220), ]},
                     {9: [(- 100, 260), (- 100, 250), (- 110, 240), (- 120, 240), (- 100, 230), (- 100, 220),
                          (- 110, 210), (- 120, 210), (- 110, 270), (- 120, 270),
                          (- 130, 260), (- 130, 250)]}
                     ]

SCORE_NUMBERS_pl2 = [{0: [(- 100, 260), (- 100, 250), (- 100, 240), (- 100, 230), (- 100, 220),
                          (- 110, 210), (- 120, 210), (- 110, 270), (- 120, 270),
                          (- 130, 260), (- 130, 250), (- 130, 240), (- 130, 230), (- 130, 220), ]},
                     {1: [(- 140, 270), (- 140, 260), (- 140, 250), (- 140, 240), (- 140, 230), (- 140, 220),
                          (- 140, 210)]},
                     {2: [(- 130, 270), (- 120, 270), (- 110, 270), (- 140, 260),
                          (- 140, 250), (- 110, 240), (- 120, 240), (- 130, 240),
                          (- 100, 230), (- 100, 220), (- 130, 210), (- 120, 210), (- 110, 210)]},
                     {3: [(- 140, 260), (- 140, 250), (- 140, 230), (- 140, 220),
                          (- 130, 270), (- 120, 270), (- 110, 270),
                          (- 130, 210), (- 120, 210), (- 110, 210), (- 130, 240)]},
                     {4: [(- 100, 240), (- 110, 240), (- 120, 240), (- 130, 240), (- 140, 240), (- 120, 250),
                          (- 120, 230), (- 120, 220), (- 120, 210), (- 100, 250), (- 100, 260), (- 100, 270)]},
                     {5: [(- 130, 270), (- 120, 270), (- 110, 270), (- 100, 260),
                          (- 100, 250), (- 110, 240), (- 120, 240), (- 130, 240),
                          (- 140, 230), (- 140, 220), (- 110, 210), (- 120, 210), (- 130, 210)]},
                     {6: [(- 130, 270), (- 120, 270), (- 110, 270), (- 100, 260),
                          (- 100, 250), (- 100, 240), (- 140, 230), (- 140, 220), (- 130, 240), (- 120, 240),
                          (- 110, 240), (- 100, 230), (- 100, 220), (- 110, 210), (- 120, 210), (- 130, 210)]},
                     {7: [(- 140, 270), (- 130, 270), (- 120, 270), (- 110, 270), (- 100, 270), (- 140, 260),
                          (- 140, 250), (- 140, 240), (- 140, 230), (- 140, 220),
                          (- 140, 210)]},
                     {8: [(- 100, 260), (- 100, 250), (- 110, 240), (- 120, 240), (- 100, 230), (- 100, 220),
                          (- 110, 210), (- 120, 210), (- 110, 270), (- 120, 270),
                          (- 130, 260), (- 130, 250), (- 130, 230), (- 130, 220), ]},
                     {9: [(- 100, 260), (- 100, 250), (- 110, 240), (- 120, 240), (- 130, 230), (- 130, 220),
                          (- 110, 210), (- 120, 210), (- 110, 270), (- 120, 270),
                          (- 130, 260), (- 130, 250)]}
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
        self.pl_2_score += 1
        score_count_pl2 = self.pl_2_score
        self.build_score_pl2(score_count_pl2)

    def build_start_score(self):
        self.build_score_pl1(0)
        self.build_score_pl2(0)

    def reset_score(self):
        self.reset()

    def build_score_pl1(self, score_count_pl1):
        """takes the score count and builds the score gfx"""
        if score_count_pl1 < 10:
            for limbo in SCORE_NUMBERS_pl1[score_count_pl1][score_count_pl1]:
                self.hideturtle()
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
                self.hideturtle()
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
