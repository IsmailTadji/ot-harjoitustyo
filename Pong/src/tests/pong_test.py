import unittest
import pygame
from logic.pong_logic import Pong
from config import RACKET_HEIGHT, VELOCITY, AI_VELOCITY


class TestPong(unittest.TestCase):
    
    def setUp(self):
        pygame.init()
        self.pong = Pong()

    def test_init(self):
        # check if both rackets are initialized
        self.assertIsNotNone(self.pong.racket_p1)
        self.assertIsNotNone(self.pong.racket_p2)

        # check if ball is initialized
        self.assertIsNotNone(self.pong.ball)

    def test_collision_with_top_wall(self):
        self.pong.ball.y_pos = 0
        self.pong.ball.y_speed = -1
        self.pong.collision()
        self.assertEqual(self.pong.ball.y_speed, 1)

    def test_collision_with_bottom_wall(self):
        self.pong.ball.y_pos = self.pong.ball.rad
        self.pong.ball.y_speed = 1
        self.pong.collision()
        self.assertEqual(self.pong.ball.y_speed, -1)

    def test_collision_with_racket_p1(self):
        self.pong.ball.x_speed = 2
        self.pong.ball.x_pos = self.pong.racket_p1.x_pos - self.pong.ball.rad
        self.pong.ball.y_pos = self.pong.racket_p1.y_pos + self.pong.racket_p1.height // 2
        self.pong.collision()
        self.assertEqual(self.pong.ball.x_speed, -2.2)

    def test_collision_with_racket_p2(self):
        self.pong.ball.x_speed = -2
        self.pong.ball.x_pos = self.pong.racket_p2.x_pos + self.pong.racket_p2.width + self.pong.ball.rad
        self.pong.ball.y_pos = self.pong.racket_p2.y_pos + self.pong.racket_p2.height // 2
        self.pong.collision()
        self.assertEqual(self.pong.ball.x_speed, 2.2)

    def test_ai_movement_ball_above_racket(self):
        self.pong.ball.y_pos = self.pong.racket_p2.y_pos
        initial_y_pos = self.pong.racket_p2.y_pos
        self.pong.ai_movement()
        self.assertEqual(self.pong.racket_p2.y_pos, initial_y_pos - AI_VELOCITY)

    def test_ai_movement_ball_below_racket(self):
        self.pong.ball.y_pos = self.pong.racket_p2.y_pos + RACKET_HEIGHT 
        initial_y_pos = self.pong.racket_p2.y_pos
        self.pong.ai_movement()
        self.assertEqual(self.pong.racket_p2.y_pos, initial_y_pos + AI_VELOCITY)