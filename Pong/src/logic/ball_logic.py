import pygame

width, height = 640, 480


class Ball():
    def __init__(self, x, y, rad, colour, velocity):
        self.x = x
        self.y = y
        self.rad = rad
        self.x_speed = velocity
        self.y_speed = 0
        self.colour = colour

    def draw_ball(self, screen):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.rad)

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed
