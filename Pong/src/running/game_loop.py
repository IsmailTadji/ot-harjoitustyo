import pygame
from running.draw import Draw
from running.score import Score
black = (0, 0, 0)


class GameLoop:
    def __init__(self, screen, clock, pong):
        self.running = True
        self.pong = pong
        self.ball = self.pong.ball
        self.racket_p1 = self.pong.racket_p1
        self.racket_p2 = self.pong.racket_p2
        self.screen = screen
        self.clock = clock
        self.score = Score(self.ball)
        self.draw = Draw(self.screen, self.pong, self.ball, self.score)

    def game_loop(self):
        while self.running:
            self.clock.tick(60)
            self.events()
            self.ball.move()
            self.pong.collision()
            self.score.point()
            if self.score.score_bool == True:
                self.score.score_bool = False
                self.reset()
            if self.score.score_p1 == 5 or self.score.score_p2 == 5:
                break
            self.draw.draw()

    def events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()

        keys = pygame.key.get_pressed()
        self.pong.move(keys)

    def reset(self):
        self.ball.x_pos = self.ball.original_x_pos
        self.ball.y_pos = self.ball.original_y_pos
        self.ball.x_speed = self.ball.original_x_speed
        self.ball.y_speed = 0
        self.racket_p1.x_pos = self.racket_p1.original_x_pos
        self.racket_p1.y_pos = self.racket_p1.original_y_pos
        self.racket_p2.x_pos = self.racket_p2.original_x_pos
        self.racket_p2.y_pos = self.racket_p2.original_y_pos