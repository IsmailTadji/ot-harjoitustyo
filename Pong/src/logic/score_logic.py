import time
from config import WIDTH

class Score:
    """
    Class for keeping the score of the game

    Attributes:
        score_p1: Integer, stores player 1 score
        score_p2: Integer, stores player 2 score
        score_bool: Bool, stores information whether a player has scored

    """
    def __init__(self, ball):
        """
        Class constructor

        Args:
            ball: Ball class, used to determine whether a point has been scored

        """
        self.score_p1 = 0
        self.score_p2 = 0
        self.ball = ball
        self.score_bool = False

    def point(self):
        """
        Point logic

        Returns:
            whether a point has been scored
        """
        # player 2 point
        if self.ball.x_pos > WIDTH:
            self.score_p2 += 1
            self.score_bool = True
        # player 1 point
        if self.ball.x_pos < 0:
            self.score_p1 += 1
            self.score_bool = True

        return self.score_bool

    def start_time(self):
        """
        Start time of a single player game


        Returns:
            start time of a single player game
        """
        start = time.time()
        return start

    def score_sp(self, start):
        """
        Final time for single player game

        Returns:
            Time spent playing
        """
        stop_time = time.time()
        return int(stop_time - start)
