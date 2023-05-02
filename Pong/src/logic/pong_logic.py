import pygame
from logic.racket_logic import Racket
from logic.ball_logic import Ball

# Global variables
WIDTH, HEIGHT = 450, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BALL_RADIUS = 5
RACKET_HEIGHT = 60
RACKET_WIDTH = 15
BALL_VELOCITY = 4
VELOCITY = 4

class Pong():

    def __init__(self):
        # create two separate rackets with their own variables, and a ball
        self.racket_p2 = Racket(
            10, HEIGHT // 2 - RACKET_HEIGHT // 2, RACKET_WIDTH, RACKET_HEIGHT, WHITE)
        self.racket_p1 = Racket(
            WIDTH - 20, HEIGHT // 2 - RACKET_HEIGHT // 2, RACKET_WIDTH, RACKET_HEIGHT, WHITE)
        self.ball = Ball(WIDTH // 2, HEIGHT // 2,
                         BALL_RADIUS, WHITE, BALL_VELOCITY)

    def collision(self):
        self.keys = pygame.key.get_pressed()

        # collision with bottom of the screen
        if self.ball.y_pos + self.ball.rad >= HEIGHT:
            self.ball.y_speed *= -1

        # collision with top of the screen
        elif self.ball.y_pos - self.ball.rad <= 0:
            self.ball.y_speed *= -1

# check if ball going right
        if self.ball.x_speed > 0:

            # check if the ball is within the same height of the racket
            if self.ball.y_pos >= self.racket_p1.y_pos and \
            self.ball.y_pos <= self.racket_p1.y_pos + RACKET_HEIGHT:

                # check if the ball is in the same x axis value as the racket
                if self.ball.x_pos + self.ball.rad >= self.racket_p1.x_pos:
                    self.ball.x_speed *= -1
                    self.ball.x_speed -= 0.2

                    # ball redirection
                    racket_middle = self.racket_p1.y_pos + RACKET_HEIGHT // 2
                    angle = (self.ball.y_pos - racket_middle) / \
                        (RACKET_HEIGHT / 2 / BALL_VELOCITY)
                    self.ball.y_speed = angle

        # check if ball going left
        else:

            # check if the ball is within the same height of the racket
            if self.ball.y_pos >= self.racket_p2.y_pos \
            and self.ball.y_pos <= self.racket_p2.y_pos + RACKET_HEIGHT:

                # check if the ball is in the same x axis value as the racket
                if self.ball.x_pos - self.ball.rad <= self.racket_p2.x_pos + RACKET_WIDTH:
                    self.ball.x_speed *= -1
                    self.ball.x_speed += 0.2

                    # ball redirection
                    racket_middle = self.racket_p2.y_pos + RACKET_HEIGHT // 2
                    angle = (self.ball.y_pos - racket_middle) / \
                        (RACKET_HEIGHT / 2 / BALL_VELOCITY)
                    self.ball.y_speed = angle

    # call movement function if players press movement button
    def move_p1(self, keys):
        if keys[pygame.K_w]:
            self.racket_p2.movement(VELOCITY, dir_up=True)

        elif keys[pygame.K_s]:
            self.racket_p2.movement(VELOCITY, dir_up=False)

    def move_p2(self, keys):
        if keys[pygame.K_UP]:
            self.racket_p1.movement(VELOCITY, dir_up=True)

        elif keys[pygame.K_DOWN]:
            self.racket_p1.movement(VELOCITY, dir_up=False)
