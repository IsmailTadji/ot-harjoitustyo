import pygame
from Rackets import Racket
from Ball import Ball

width, height = 640, 480
white = (255,255,255)
red = (255,0,0)

class Pong():
    def __init__(self):
        self.racket = Racket(width/2, height-20, 40, 15, white)
        self.ball = Ball(width/2, height/2, 5, 10, red)

    def draw_objects(self):
        self.ball.draw_ball()

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
