from turtle import Turtle


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


# fixme 1 : position number 1
# fixme 2 : limbo list tuple
