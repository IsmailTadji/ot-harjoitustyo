import pygame

WIDTH, HEIGHT = 450, 400

class Racket():
    def __init__(self, x_pos, y_pos, width, height, colour):
        # save original positions for resetting the game
        self.x_pos = self.original_x_pos = x_pos
        self.y_pos = self.original_y_pos = y_pos
        self.width = width
        self.height = height
        self.colour = colour

    # drawing racket on screen
    def draw_racket(self, screen):
        pygame.draw.rect(screen, self.colour,
                         (self.x_pos, self.y_pos, self.width, self.height))


    # movement of racket when buttons are pressed
    def movement(self, velocity, dir_up=True):
        if dir_up:
            # move up
            self.y_pos -= velocity
            self.y_pos = max(self.y_pos,0)
        else:
            # move down
            self.y_pos += velocity
            if self.y_pos + self.height >= HEIGHT:
                self.y_pos = HEIGHT - self.height
