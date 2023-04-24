import pygame
from logic.racket_logic import Racket
from logic.ball_logic import Ball

WIDTH, HEIGHT = 450, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BALL_RADIUS = 5
RACKET_HEIGHT = 60
RACKET_WIDTH = 15
BALL_VELOCITY = 4


class Pong():

    def __init__(self):
        self.racket_p2 = Racket(
            10, HEIGHT // 2 - RACKET_HEIGHT // 2, RACKET_WIDTH, RACKET_HEIGHT, WHITE)
        self.racket_p1 = Racket(
            WIDTH - 20, HEIGHT // 2 - RACKET_HEIGHT // 2, RACKET_WIDTH, RACKET_HEIGHT, WHITE)
        self.ball = Ball(WIDTH // 2, HEIGHT // 2,
                         BALL_RADIUS, WHITE, BALL_VELOCITY)

    def collision(self):

        if self.ball.y_pos + self.ball.rad >= HEIGHT:
            self.ball.y_speed *= -1

        elif self.ball.y_pos - self.ball.rad <= 0:
            self.ball.y_speed *= -1

        # ball going right
        if self.ball.x_speed > 0:

            if self.ball.y_pos >= self.racket_p1.y_pos and \
            self.ball.y_pos <= self.racket_p1.y_pos + RACKET_HEIGHT:

                if self.ball.x_pos + self.ball.rad >= self.racket_p1.x_pos:
                    self.ball.x_speed *= -1
                    self.ball.x_speed -= 0.2

                    # ball redirection
                    racket_middle = self.racket_p1.y_pos + RACKET_HEIGHT // 2
                    angle = (self.ball.y_pos - racket_middle) / \
                        (RACKET_HEIGHT / 2 / BALL_VELOCITY)
                    self.ball.y_speed = angle

        # ball going left
        else:
            if self.ball.y_pos >= self.racket_p2.y_pos \
            and self.ball.y_pos <= self.racket_p2.y_pos + RACKET_HEIGHT:

                if self.ball.x_pos - self.ball.rad <= self.racket_p2.x_pos + RACKET_WIDTH:
                    self.ball.x_speed *= -1
                    self.ball.x_speed += 0.2

                    # ball redirection
                    racket_middle = self.racket_p2.y_pos + RACKET_HEIGHT // 2
                    angle = (self.ball.y_pos - racket_middle) / \
                        (RACKET_HEIGHT / 2 / BALL_VELOCITY)
                    self.ball.y_speed = angle

    def move(self, keys):
        if keys[pygame.K_w]:
            self.racket_p2.movement(dir_up=True)

        elif keys[pygame.K_s]:
            self.racket_p2.movement(dir_up=False)

        elif keys[pygame.K_UP]:
            self.racket_p1.movement(dir_up=True)

        elif keys[pygame.K_DOWN]:
            self.racket_p1.movement(dir_up=False)