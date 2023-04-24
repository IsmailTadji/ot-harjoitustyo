import pygame
from running.score import Score

pygame.init()
WIDTH, HEIGHT = 450, 400
BLACK = (0,0,0)
WHITE = (255,255,255)
FONT = pygame.font.SysFont("arial", 40)

class Draw:
    def __init__(self, screen, pong, ball, score):
        self.screen = screen
        self.pong = pong
        self.ball = ball
        self.score = score

        
    def draw(self):
        self.screen.fill((BLACK))
        p1_score = FONT.render(f"{self.score.score_p1}", 1, WHITE)
        p2_score = FONT.render(f"{self.score.score_p2}", 1, WHITE)
        self.screen.blit(p1_score, (WIDTH * (3 / 4) - p1_score.get_width() // 2, 15))
        self.screen.blit(p2_score, (WIDTH // 4 - p2_score.get_width() // 2, 15))

        self.pong.racket_p1.draw_racket(self.screen)
        self.pong.racket_p2.draw_racket(self.screen)
        self.pong.ball.draw_ball(self.screen)
        pygame.display.update()