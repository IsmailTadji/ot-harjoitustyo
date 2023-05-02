import unittest
import pygame
from logic.pong_logic import Pong

VELOCITY = 4

class TestPong(unittest.TestCase):
    
    def setUp(self):
        pygame.init()
        self.game = Pong()

    def tearDown(self):
        pygame.quit()

    def test_init(self):
        # check if both rackets are initialized
        self.assertIsNotNone(self.game.racket_p1)
        self.assertIsNotNone(self.game.racket_p2)

        # check if ball is initialized
        self.assertIsNotNone(self.game.ball)

    def test_collision_with_top_wall(self):
        self.game.ball.y_pos = 0
        self.game.ball.y_speed = -1
        self.game.collision()
        self.assertEqual(self.game.ball.y_speed, 1)

    def test_collision_with_bottom_wall(self):
        self.game.ball.y_pos = self.game.ball.rad
        self.game.ball.y_speed = 1
        self.game.collision()
        self.assertEqual(self.game.ball.y_speed, -1)

    def test_collision_with_racket_p1(self):
        self.game.ball.x_speed = 2
        self.game.ball.x_pos = self.game.racket_p1.x_pos - self.game.ball.rad
        self.game.ball.y_pos = self.game.racket_p1.y_pos + self.game.racket_p1.height // 2
        self.game.collision()
        self.assertEqual(self.game.ball.x_speed, -2.2)

    def test_collision_with_racket_p2(self):
        self.game.ball.x_speed = -2
        self.game.ball.x_pos = self.game.racket_p2.x_pos + self.game.racket_p2.width + self.game.ball.rad
        self.game.ball.y_pos = self.game.racket_p2.y_pos + self.game.racket_p2.height // 2
        self.game.collision()
        self.assertEqual(self.game.ball.x_speed, 2.2)
