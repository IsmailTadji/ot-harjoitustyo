import pygame
from logic.Pong import Pong



width, height = 450, 400

def Main():
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Pong")
    pong = Pong()
    pygame.init()
    pong.game_loop()

if __name__ == "__main__":
    main