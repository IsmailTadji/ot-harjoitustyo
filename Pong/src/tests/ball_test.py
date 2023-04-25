import pygame
import unittest
from logic.ball_logic import Ball

pygame.init()
WIDTH, HEIGHT = 450, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))

X_POS = WIDTH // 2
Y_POS = HEIGHT // 2
RAD = 5
WHITE = (255, 255, 255)
VELOCITY = 5

class TestBall(unittest.TestCase):
    def setUp(self):
        self.ball = Ball(X_POS, Y_POS, RAD, WHITE, VELOCITY)

    def test_initial_position(self):
        self.assertEqual(self.ball.x_pos, X_POS)
        self.assertEqual(self.ball.y_pos, Y_POS)

    def test_initial_velocity(self):
        self.assertEqual(self.ball.x_speed, VELOCITY)
        self.assertEqual(self.ball.y_speed, 0)

    def test_move(self):
        self.ball.move()
        self.assertEqual(self.ball.x_pos, X_POS + VELOCITY)
        self.assertEqual(self.ball.y_pos, Y_POS)

    def test_draw_ball(self):
        surface = pygame.Surface((WIDTH, HEIGHT))
        self.ball.draw_ball(surface)
        pixel_colour = surface.get_at((X_POS, Y_POS))

        self.assertEqual(pixel_colour, WHITE)


