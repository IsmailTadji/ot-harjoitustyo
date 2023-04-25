import pygame

WIDTH, HEIGHT = 450, 400

class Ball():
    def __init__(self, x_pos, y_pos, rad, colour, velocity):
        self.x_pos = self.original_x_pos = x_pos
        self.y_pos = self.original_y_pos = y_pos
        self.rad = rad
        self.x_speed = self.original_x_speed = velocity
        self.y_speed = 0
        self.colour = colour

    def draw_ball(self, screen):
        pygame.draw.circle(screen, self.colour, (self.x_pos, self.y_pos), self.rad)

    def move(self):
        self.x_pos += self.x_speed
        self.y_pos += self.y_speed
