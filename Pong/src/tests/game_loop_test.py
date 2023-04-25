import pygame
import unittest
from logic.pong_logic import Pong
from running.game_loop import GameLoop


class TestGameLoop(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.pong = Pong()
        self.game_loop = GameLoop(self.screen, self.clock, self.pong)

    def test_game_loop(self):
        self.game_loop.running = False
        self.game_loop.game_loop()
        self.assertFalse(self.game_loop.running)

    def test_reset(self):
        self.game_loop.reset()
        self.assertEqual(self.game_loop.ball.x_pos, self.game_loop.ball.original_x_pos)
        self.assertEqual(self.game_loop.ball.y_pos, self.game_loop.ball.original_y_pos)
        self.assertEqual(self.game_loop.ball.x_speed, self.game_loop.ball.original_x_speed)
        self.assertEqual(self.game_loop.ball.y_speed, 0)
        self.assertEqual(self.game_loop.racket_p1.x_pos, self.game_loop.racket_p1.original_x_pos)
        self.assertEqual(self.game_loop.racket_p1.y_pos, self.game_loop.racket_p1.original_y_pos)
        self.assertEqual(self.game_loop.racket_p2.x_pos, self.game_loop.racket_p2.original_x_pos)
        self.assertEqual(self.game_loop.racket_p2.y_pos, self.game_loop.racket_p2.original_y_pos)

    def tearDown(self):
        pygame.quit()

