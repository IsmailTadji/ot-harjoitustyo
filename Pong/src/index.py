import pygame
from logic.pong_logic import Pong
from running.game_loop import GameLoop


width, height = 450, 400


def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Pong")
    pong = Pong()
    loop = GameLoop(screen, clock, pong)
    loop.game_loop()


if __name__ == "__main__":
    main()
