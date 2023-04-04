import pygame
from racket_logic import Racket
from ball_logic import Ball

width, height = 640, 480
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)



class Pong():
    def __init__(self):
        pygame.init()
        self.naytto = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Massi")
        self.clock = pygame.time.Clock()
        self.game_loop()


    def game_loop(self):
        while True:
            self.draw_screen()
            self.events()
            self.objects()

        # While loop to check key presses
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_w:
                    self.racket.move("up")
                if event.key == pygame.K_s:
                    self.racket.move("down")
                if event.key == pygame.K_UP:
                    self.racket.move("up")
                if event.key == pygame.K_DOWN:
                    self.racket.move("down")

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_LEFT:
                    self.racket_stop_move("up")
                if event.key == pygame.K_RIGHT:
                    self.racket_stop_move("down")
                if event.key == pygame.K_UP:
                    self.racket_stop_move("up")
                if event.key == pygame.K_DOWN:
                    self.racket_stop_move("down")

            if event.type == pygame.QUIT:
                exit()


    def objects(self):
        self.racket1 = Racket(10, 20, 10, 40, white)
	 
    def draw_screen(self):
        self.naytto.fill((black))
        self.racket1.draw_racket()
        self.Ball.draw_ball()
        pygame.display.flip()    
        self.kello.tick(60)

Pong()