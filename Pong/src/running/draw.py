import pygame
#initialise pygame to update the screen
pygame.init()

# GLOBAL VARIABLES
WIDTH, HEIGHT = 450, 400
BLACK = (0,0,0)
WHITE = (255,255,255)
FONT = pygame.font.SysFont("arial", 40)
FONT_END = pygame.font.SysFont("arial", 20)

class Draw:
    # define objects
    def __init__(self, screen, pong, ball, score):
        self.screen = screen
        self.pong = pong
        self.ball = ball
        self.score = score


    def draw(self):
        self.screen.fill((BLACK))
        # define scores
        p1_score = FONT.render(f"{self.score.score_p1}", 1, WHITE)
        p2_score = FONT.render(f"{self.score.score_p2}", 1, WHITE)
        # draw scores on screen
        self.screen.blit(p1_score, (WIDTH * (3 / 4) - p1_score.get_width() // 2, 15))
        self.screen.blit(p2_score, (WIDTH // 4 - p2_score.get_width() // 2, 15))

        # draw the ball and racket
        self.pong.racket_p1.draw_racket(self.screen)
        self.pong.racket_p2.draw_racket(self.screen)
        self.pong.ball.draw_ball(self.screen)
        pygame.display.update()

    def end_screen(self):
        # fill the screen to a black background
        self.screen.fill(BLACK)
        # find out who won
        if self.score.score_p1 > self.score.score_p2:
            winner = "Player 1"
        else:
            winner = "Player 2"
        # define texts for the end screen
        end_text = FONT_END.render(f"{winner} wins! Final score: \
                    {self.score.score_p1} - {self.score.score_p2}", 1, WHITE)
        new_game = FONT_END.render("Press space to play again", 1, WHITE)
        # draw the texts on the end screen
        self.screen.blit(end_text, (WIDTH // 2 - end_text.get_width() // 2,\
                                     HEIGHT // 2 - end_text.get_height() // 2))
        self.screen.blit(new_game, (WIDTH // 2 - new_game.get_width() // 2,\
                                     HEIGHT // 2 + 40 - new_game.get_height() // 2))
        pygame.display.update()

    def start(self):
        # space start
        start_text = FONT_END.render("Press space to start", 1, WHITE)
        # draw on screen
        self.screen.blit(start_text,(WIDTH // 2 - start_text.get_width() // 2,\
                                      HEIGHT//2 - 40 - start_text.get_height() // 2))
        pygame.display.update()
