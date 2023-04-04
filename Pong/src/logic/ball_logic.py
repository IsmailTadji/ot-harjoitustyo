import pygame

width, height = 640, 480

class Ball():
    def __init__(self, x, y, rad, speed, colour):
        self.x = x
        self.y = y
        self.rad = rad
        self.speed = speed
        self.colour = colour
        self.ball = self.draw_ball()

    def draw_ball(self):
        pygame.draw.circle(Main.screen, self.x, self.y, self.rad, self.speed, self.colour)

    def bounce(self, roof=False, racket=False):
        if racket:
            self.x *= -1
        if roof:
            self.y *= -1
        

    
