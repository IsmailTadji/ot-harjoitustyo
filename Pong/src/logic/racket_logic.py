import pygame

width, height = 640, 480

class Racket():
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.rect = pygame.rect(self.x, self.y, self.width, self.height)


    def draw_racket(self):
        pygame.draw.rect(self.rect,)

    def movement(self, dir):
        if dir == "left":
            self.x += 4
            # Stop from going out of bounds
            if self.x >= 640:
                self.x = 640
        if dir == "right":
            self.x -= 4
            # Stop from going out of bounds
            if self.x <= 0:
                self.x = 0
        if dir == "up":
            self.y -= 4
            # Stop from going out of bounds
            if self.y <= 0:
                self.y = 0
        if dir == "down":
            self.y += 4
            # Stop from going out of bounds
            if self.y >= 480:
                self.y = 480
            
    
