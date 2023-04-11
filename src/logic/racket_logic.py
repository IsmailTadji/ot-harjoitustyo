import pygame

width, height = 450, 400
velocity = 4

class Racket():
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour

    def draw_racket(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))

    def movement(self, up=True):
            if up:
                self.y -= velocity
                if self.y <= 0:
                     self.y = 0
            else:
                self.y += velocity
                if self.y + self.height >= height:
                     self.y = height - self.height




            
    
