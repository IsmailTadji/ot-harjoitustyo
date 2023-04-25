import pygame

WIDTH, HEIGHT = 450, 400

class Racket():
    def __init__(self, x_pos, y_pos, width, height, colour):
        self.x_pos = self.original_x_pos = x_pos
        self.y_pos = self.original_y_pos = y_pos
        self.width = width
        self.height = height
        self.colour = colour

    def draw_racket(self, screen):
        pygame.draw.rect(screen, self.colour,
                         (self.x_pos, self.y_pos, self.width, self.height))

    def movement(self, velocity, dir_up=True):
        if dir_up:
            self.y_pos -= velocity
            self.y_pos = max(self.y_pos,0)
        else:
            self.y_pos += velocity
            if self.y_pos + self.height >= HEIGHT:
                self.y_pos = HEIGHT - self.height
