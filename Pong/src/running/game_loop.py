import pygame
black = (0, 0, 0)


class GameLoop:
    def __init__(self, screen, clock, pong):
        self.running = True
        self.pong = pong
        self.ball = self.pong.ball
        self.screen = screen
        self.clock = clock

    def game_loop(self):
        while self.running:
            self.clock.tick(60)
            self.events()
            self.ball.move()
            self.pong.collision()
            self.draw_screen()

    def events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()

        keys = pygame.key.get_pressed()
        self.pong.move(keys)

    def draw_screen(self):
        self.screen.fill((black))
        self.pong.racket_p1.draw_racket(self.screen)
        self.pong.racket_p2.draw_racket(self.screen)
        self.ball.draw_ball(self.screen)
        pygame.display.update()
