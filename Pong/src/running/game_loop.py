import pygame
from running.draw import Draw
from logic.score import Score
black = (0, 0, 0)


class GameLoop:
    def __init__(self, screen, clock, pong):
        # boolean values to allow pausing the game
        self.paused = False
        self.running = False
        self.drawn = False
        self.start = True
        # define variables
        self.pong = pong
        self.ball = self.pong.ball
        self.racket_p1, self.racket_p2 = self.pong.racket_p1, self.pong.racket_p2
        self.screen = screen
        self.clock = clock
        # initialise the score class
        self.score = Score(self.ball)
        # initialise the draw class
        self.draw = Draw(self.screen, self.pong, self.ball, self.score)

    # game loop
    def game_loop(self):
        while self.start:
            self.clock.tick(60)
            self.events()
            if not self.drawn:
                self.draw.draw()
                self.drawn = True
            # draw press space to start
            self.draw.start()
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                self.start = False
                self.running = True

        # main game loop
        while self.running:
            self.clock.tick(60)
            self.events()

            if not self.paused:
                self.ball.move()
                self.pong.collision()
                self.score.point()
                self.draw.draw()

            # if player scores resets the playing field
            if self.score.score_bool:
                self.score.score_bool = False
                self.reset(restart=False)
            # if a player reaches 5 points game ends
            if self.score.score_p1 == 5 or self.score.score_p2 == 5:
                self.paused = True
                self.draw.end_screen()
                # if player wishes to play again
                if key[pygame.K_SPACE]:
                    self.reset(restart=True)
                    self.paused = False

    # pressing of keys
    def events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
        # current pressed keys
        keys = pygame.key.get_pressed()
        self.pong.move_p1(keys)
        self.pong.move_p2(keys)

    # reset the playing field
    def reset(self, restart):
        # if game restarted, zero the points
        if restart:
            self.score.score_p1 = 0
            self.score.score_p2 = 0
            restart = False
        # reset all variables and positions
        self.ball.x_pos = self.ball.original_x_pos
        self.ball.y_pos = self.ball.original_y_pos
        self.ball.x_speed = self.ball.original_x_speed
        self.ball.y_speed = 0
        self.racket_p1.x_pos = self.racket_p1.original_x_pos
        self.racket_p1.y_pos = self.racket_p1.original_y_pos
        self.racket_p2.x_pos = self.racket_p2.original_x_pos
        self.racket_p2.y_pos = self.racket_p2.original_y_pos
