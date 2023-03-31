import pygame
from Rackets import Racket

class Pong():
    def __init__(self):
        self.racket = Racket()


        # While loop to check key presses
    def events(self):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_LEFT:
                        self.racket.move("left")
                    if event.key == pygame.K_RIGHT:
                        self.racket.move("right")
                    if event.key == pygame.K_UP:
                        self.racket.move("up")
                    if event.key == pygame.K_DOWN:
                        self.racket.move("down")

                if event.type == pygame.KEYUP:

                    if event.key == pygame.K_LEFT:
                        self.racket_stop_move(left)
                    if event.key == pygame.K_RIGHT:
                        self.racket_stop_move(right)
                    if event.key == pygame.K_UP:
                        self.racket_stop_move(up)
                    if event.key == pygame.K_DOWN:
                        self.racket_stop_move(down)

                if event.type == pygame.QUIT:
                    exit()
