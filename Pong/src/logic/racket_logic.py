import pygame

width, height = 640, 480


class Racket():
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.racket_rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_racket(self, screen):
        pygame.draw.rect(screen, self.colour, self.racket_rect)

    def movement(self, speed):
            self.y += speed
            # Stop from going out of bounds
            if self.y <= 0:
                self.y = 0
            # Stop from going out of bounds
            if self.y + self.height >= height:
                self.y = height - self.height



            
    
