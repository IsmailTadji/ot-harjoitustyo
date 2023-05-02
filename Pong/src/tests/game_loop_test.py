import unittest
import pygame
from logic.pong_logic import Pong
from running.game_loop import GameLoop

WIDTH = 450

class TestGameLoop(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((450, 400))
        self.clock = pygame.time.Clock()
        self.pong = Pong()
        self.game_loop = GameLoop(self.screen, self.clock, self.pong)

    def tearDown(self):
        pygame.quit()

    def test_reset(self):
        # Check that the reset function properly resets all variables and positions
        self.game_loop.ball.x_pos = 100
        self.game_loop.ball.y_pos = 100
        self.game_loop.ball.x_speed = 5
        self.game_loop.ball.y_speed = 5
        self.game_loop.racket_p1.x_pos = 200
        self.game_loop.racket_p1.y_pos = 200
        self.game_loop.racket_p2.x_pos = 300
        self.game_loop.racket_p2.y_pos = 300
        self.game_loop.score.score_p1 = 1
        self.game_loop.score.score_p2 = 2
        self.game_loop.reset(restart=True)
        self.assertEqual(self.game_loop.ball.x_pos, self.game_loop.ball.original_x_pos)
        self.assertEqual(self.game_loop.ball.y_pos, self.game_loop.ball.original_y_pos)
        self.assertEqual(self.game_loop.ball.x_speed, self.game_loop.ball.original_x_speed)
        self.assertEqual(self.game_loop.ball.y_speed, 0)
        self.assertEqual(self.game_loop.racket_p1.x_pos, self.game_loop.racket_p1.original_x_pos)
        self.assertEqual(self.game_loop.racket_p1.y_pos, self.game_loop.racket_p1.original_y_pos)
        self.assertEqual(self.game_loop.racket_p2.x_pos, self.game_loop.racket_p2.original_x_pos)
        self.assertEqual(self.game_loop.racket_p2.y_pos, self.game_loop.racket_p2.original_y_pos)
        self.assertEqual(self.game_loop.score.score_p1, 0)
        self.assertEqual(self.game_loop.score.score_p2, 0)

    def test_point(self):
        # Check that the score is updated correctly when a point is scored
        self.game_loop.score.score_p1 = 0
        self.game_loop.score.score_p2 = 0
        self.game_loop.ball.x_pos = WIDTH + 1
        self.game_loop.ball.y_pos = self.game_loop.racket_p1.y_pos
        self.game_loop.score.point()
        self.assertEqual(self.game_loop.score.score_p1, 0)
        self.assertEqual(self.game_loop.score.score_p2, 1)


    def test_game_loop(self):
        self.game_loop.running = False
        self.game_loop.start = False
        self.game_loop.game_loop()
        self.assertFalse(self.game_loop.running)

        # check that the game loop ran without error
        self.assertTrue(True)

    def tearDown(self):
        pygame.quit()
