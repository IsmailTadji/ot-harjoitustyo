WIDTH, HEIGHT = 450, 400

class Score:
    def __init__(self, ball):
        self.score_p1 = 0
        self.score_p2 = 0
        self.ball = ball
        self.score_bool = False
    
    def point(self):
        if self.ball.x_pos > WIDTH:
            self.score_p2 += 1
            self.score_bool = True
            return self.score_bool
        if self.ball.x_pos < 0:
            self.score_p1 += 1
            self.score_bool = True
            return self.score_bool