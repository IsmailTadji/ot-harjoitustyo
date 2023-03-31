import pygame

width, height = 640, 480

class Main():
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Pong")
        
