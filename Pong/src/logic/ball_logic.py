import pygame
from config import WHITE

class Ball():
    """
    Class, that draws the ball, and handles its movements logic
    
    Attributes:

        y_speed: Integer, holds the value for the balls vertical speed
    """
    def __init__(self, x_pos, y_pos, rad, velocity):
        """
        Class constructor

        Args:

            x_pos: Integer, balls position on x-axis
            original_x_pos: Integer, stores ball's original x-axis position for resetting the board
            y_pos: Integer, balls position on y-axis
            original_x_pos: Integer, stores ball's original y-axis position for resetting the board
            rad: Integer, balls radius
            x_speed: Integer, balls horisontal speed

        """
        self.x_pos = self.original_x_pos = x_pos
        self.y_pos = self.original_y_pos = y_pos
        self.rad = rad
        self.x_speed = self.original_x_speed = velocity
        self.y_speed = 0

    def draw_ball(self, screen):
        """
        Draws the ball on window
        
        
        Args:

            screen (pygame.surface): Pygame window where all elements are drawn

        """
        pygame.draw.circle(screen, WHITE, (self.x_pos, self.y_pos), self.rad)

    def move(self):
        """
        Movement logic of the ball
        
        """
        self.x_pos += self.x_speed
        self.y_pos += self.y_speed
