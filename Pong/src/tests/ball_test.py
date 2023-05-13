import pygame
import unittest
from logic.ball_logic import Ball
from src.config import WIDTH, HEIGHT, BALL_RADIUS, BALL_VELOCITY, WHITE

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))



class TestBall(unittest.TestCase):
    def setUp(self):
        self.ball = Ball(WIDTH//2, HEIGHT//2, BALL_RADIUS, BALL_VELOCITY)

    def test_initial_position(self):
        self.assertEqual(self.ball.x_pos, WIDTH//2)
        self.assertEqual(self.ball.y_pos, HEIGHT//2)

    def test_initial_velocity(self):
        self.assertEqual(self.ball.x_speed, BALL_VELOCITY)
        self.assertEqual(self.ball.y_speed, 0)

    def test_move(self):
        self.ball.move()
        self.assertEqual(self.ball.x_pos, WIDTH//2 + BALL_VELOCITY)
        self.assertEqual(self.ball.y_pos, HEIGHT//2)

    def test_draw_ball(self):
        surface = pygame.Surface((WIDTH, HEIGHT))
        self.ball.draw_ball(surface)
        pixel_colour = surface.get_at((WIDTH//2, HEIGHT//2))

        self.assertEqual(pixel_colour, WHITE)


