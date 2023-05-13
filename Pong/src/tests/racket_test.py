import pygame
import unittest
from src.logic.racket_logic import Racket
from src.config import WIDTH, HEIGHT, VELOCITY


class TestRacket(unittest.TestCase):

    def setUp(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.racket = Racket(50, 100, 10, 50, (255, 255, 255))

    def test_racket_drawn_correctly(self):
        self.racket.draw_racket(self.screen)
        color_at_top_left_corner = self.screen.get_at((self.racket.x_pos, self.racket.y_pos))
        self.assertEqual(color_at_top_left_corner, (255, 255, 255))

    def test_racket_movement_up(self):
        original_y_pos = self.racket.y_pos
        self.racket.movement(VELOCITY, dir_up=True)
        self.assertLess(self.racket.y_pos, original_y_pos)

    def test_racket_movement_down(self):
        original_y_pos = self.racket.y_pos
        self.racket.movement(VELOCITY,dir_up=False)
        self.assertGreater(self.racket.y_pos, original_y_pos)

    def test_racket_movement_up_bound(self):
        self.racket.y_pos = 0
        self.racket.movement(VELOCITY, dir_up=True)
        self.assertEqual(self.racket.y_pos, 0)

    def test_racket_movement_down_bound(self):
        self.racket.y_pos = HEIGHT - self.racket.height
        self.racket.movement(VELOCITY, dir_up=False)
        self.assertEqual(self.racket.y_pos, HEIGHT - self.racket.height)

