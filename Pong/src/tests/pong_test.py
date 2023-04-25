import pygame
import unittest
from logic.pong_logic import Pong
pygame.init()

class TestPong(unittest.TestCase):

    def setUp(self):
        self.game = Pong()


    def test_collision(self):
        # test ball collision with top wall
        self.game.ball.y_pos = 0
        self.game.ball.y_speed = -1
        self.game.collision()
        self.assertEqual(self.game.ball.y_speed, 1)

        # test ball collision with bottom wall
        self.game.ball.y_pos = 400
        self.game.ball.y_speed = 1
        self.game.collision()
        self.assertEqual(self.game.ball.y_speed, -1)

        # test ball collision with left racket
        self.game.ball.x_pos = 25
        self.game.ball.x_speed = -4
        self.game.ball.y_pos = 200
        self.game.collision()
        self.assertEqual(self.game.ball.x_speed, 4.2)

        # test ball collision with right racket
        self.game.ball.x_pos = 440
        self.game.ball.x_speed = 4
        self.game.ball.y_pos = 200
        self.game.collision()
        self.assertEqual(self.game.ball.x_speed, -4.2)


