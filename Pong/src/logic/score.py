WIDTH, HEIGHT = 450, 400

class Score:
    # Values
    def __init__(self, ball):
        self.score_p1 = 0
        self.score_p2 = 0
        self.ball = ball
        self.score_bool = False

    # point logic
    def point(self):
        # player 2 point
        if self.ball.x_pos > WIDTH:
            self.score_p2 += 1
            self.score_bool = True
        # player 1 point
        if self.ball.x_pos < 0:
            self.score_p1 += 1
            self.score_bool = True

        return self.score_bool
