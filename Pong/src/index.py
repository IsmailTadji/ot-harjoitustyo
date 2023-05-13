import pygame
from logic.pong_logic import Pong
from running.game_loop import GameLoop
from config import WIDTH, HEIGHT
from database_connection import get_database_connection
from repositories.db_scores import DbScores

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Pong")
    pong = Pong()
    db_scores = DbScores(get_database_connection())
    loop = GameLoop(screen, clock, pong, db_scores)
    loop.game_loop()


if __name__ == "__main__":
    main()
