import pygame
from config import HEIGHT, AI_VELOCITY

class Racket():
    """
    Class that draws the racket, and handles the racket movement

    """

    def __init__(self, x_pos, y_pos, width, height, colour):
        """
        Class constructor

        Args:
        
            x_pos: Integer, rackets position on x-axis
            original_x_pos: Integer, stores racket's original x-axis position for resetting board
            y_pos: Integer, rackets position on y-axis
            original_x_pos: Integer, stores racket's original y-axis position for resetting board
            width: Integer, stores the width of the racket
            height: Integer, stores the height of the racket
            colour: Tuple, stores the colour of the racket

        """
        self.x_pos = self.original_x_pos = x_pos
        self.y_pos = self.original_y_pos = y_pos
        self.width = width
        self.height = height
        self.colour = colour

    def draw_racket(self, screen):
        """
        Draws the racket on the screen

        Args:
        
            screen (pygame.surface): Pygame window where all elements are drawn

        """
        pygame.draw.rect(screen, self.colour,
                         (self.x_pos, self.y_pos, self.width, self.height))


    def movement(self, velocity, dir_up=True):
        """
        Racket movement logic

        
        Args:
            velocity: Integer, speed of the racket
            dir_up: Bool, determines whether the racket is going up or down

        """
        if dir_up:
            # move up
            self.y_pos -= velocity
            self.y_pos = max(self.y_pos,0)
        else:
            # move down
            self.y_pos += velocity
            if self.y_pos + self.height >= HEIGHT:
                self.y_pos = HEIGHT - self.height

    def movement_ai(self, dir_up=True):
        """
        Ai racket movement logic

        
        Args:
            dir_up: Bool, determines whether the racket is going up or down

        """
        if dir_up:
            # move up
            self.y_pos -= AI_VELOCITY
            self.y_pos = max(self.y_pos,0)
        else:
            # move down
            self.y_pos += AI_VELOCITY
            if self.y_pos + self.height >= HEIGHT:
                self.y_pos = HEIGHT - self.height
