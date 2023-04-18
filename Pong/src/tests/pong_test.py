import unittest
from src.logic.pong import Pong

width, height = 450, 400


class TestPong(unittest.TestCase):

    def setUp(self):
        self.pong = Pong()

    def test_rackets_x_and_y(self):
        pos1 = (self.pong.racket_p1.x, self.pong.racket_p1.y)
        self.assertEqual(pos1, (430, 170))
        pos2 = (self.pong.racket_p2.x, self.pong.racket_p2.y)
        self.assertEqual(pos2, (10, 170))
