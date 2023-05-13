import unittest
import pygame
from unittest.mock import patch
from logic.button_logic import Button
from config import WIDTH,HEIGHT

class TestButton(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.button = Button((255, 0, 0), (100, 100, 200, 50))

    def tearDown(self):
        pygame.quit()

    def test_button_initial_state(self):
        self.assertEqual(self.button.colour, (255, 0, 0))
        self.assertEqual(self.button.tple, (100, 100, 200, 50))
        self.assertIsInstance(self.button.rect, pygame.Rect)
        self.assertFalse(self.button.clicked)

    @patch('pygame.mouse.get_pressed', return_value=(1, 0, 0))
    @patch('pygame.mouse.get_pos', return_value=(150, 125))
    def test_button_click(self, mock_get_pos, mock_get_pressed):
        result = self.button.click()
        self.assertTrue(result)
        self.assertTrue(self.button.clicked)

    @patch('pygame.mouse.get_pressed', return_value=(0, 0, 0))
    def test_button_release(self, mock_get_pressed):
        self.button.clicked = True
        result = self.button.click()
        self.assertFalse(result)
        self.assertFalse(self.button.clicked)