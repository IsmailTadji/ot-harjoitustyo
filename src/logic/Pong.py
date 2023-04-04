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
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Pong")
        self.clock = pygame.time.Clock()
        self.game_loop()


    def game_loop(self):
        while True:
            self.events()
            self.objects()
            self.draw_screen()

        # While loop to check key presses
    def events(self):
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                keys = pygame.key.get_pressed()
                
                if keys[pygame.K_UP]:
                    self.racket.movement(-4)
                
                elif keys[pygame.K_DOWN]:
                    self.racket.movement(4)
            
            if event.type == pygame.QUIT:
                pygame.quit()



    def objects(self):
        self.racket = Racket(width//2, height//2, 10, 40, white)


    def draw_screen(self):
        self.screen.fill((black))
        self.racket.draw_racket(self.screen)
        pygame.display.flip()    
        self.clock.tick(60)

Pong()