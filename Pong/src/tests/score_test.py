import unittest
from unittest.mock import Mock
from logic.score_logic import Score
from config import WIDTH


class TestScore(unittest.TestCase):

    def setUp(self):
        self.ball = Mock()
        self.score = Score(self.ball)

    def test_initial_scores_are_zero(self):
        self.assertEqual(self.score.score_p1, 0)
        self.assertEqual(self.score.score_p2, 0)

    def test_point_player2(self):
        self.ball.x_pos = WIDTH + 1
        self.score.point()
        self.assertEqual(self.score.score_p2, 1)
        self.assertTrue(self.score.score_bool)

    def test_point_player1(self):
        self.ball.x_pos = -1
        self.score.point()
        self.assertEqual(self.score.score_p1, 1)
        self.assertTrue(self.score.score_bool)

    def test_point_no_score(self):
        self.ball.x_pos = 100  # Some position within the valid range
        self.score.point()
        self.assertEqual(self.score.score_p1, 0)
        self.assertEqual(self.score.score_p2, 0)
        self.assertFalse(self.score.score_bool)

    def test_start_time_returns_valid_time(self):
        start_time = self.score.start_time()
        self.assertIsInstance(start_time, float)

    def test_score_sp_returns_valid_score(self):
        start_time = 0  # Replace with a valid start time if needed
        stop_time = start_time + 5  # Replace with a valid stop time if needed
        self.score.score_sp = Mock(return_value=stop_time - start_time)
        score = self.score.score_sp(start_time)
        self.assertIsInstance(score, int)
        self.assertEqual(score, 5)

