import pygame
from logic.racket_logic import Racket
from logic.ball_logic import Ball
from config import WIDTH, HEIGHT, WHITE, BALL_RADIUS, \
    BALL_VELOCITY, RACKET_HEIGHT, RACKET_WIDTH, VELOCITY

class Pong():
    """
    Class for the Pong logic

    Attributes:

        racket_p2: Racket class that defines the rackets values and draws it on screen
        racket_p1: Racket class that defines the rackets values and draws it on screen
        ball: Ball class that defines the balls values and draws it on screen

    """

    def __init__(self):
        """
        Class constructor

        """
        self.racket_p2 = Racket(
            10, HEIGHT // 2 - RACKET_HEIGHT // 2, RACKET_WIDTH, RACKET_HEIGHT, WHITE)
        self.racket_p1 = Racket(
            WIDTH - 20, HEIGHT // 2 - RACKET_HEIGHT // 2, RACKET_WIDTH, RACKET_HEIGHT, WHITE)
        self.ball = Ball(WIDTH // 2, HEIGHT // 2 - 10,
                         BALL_RADIUS, BALL_VELOCITY)

    def collision(self):
        """
        Handles the collision of the ball

        Attributes:
            racket_middle: Integer, y-axis value of the middle of the racket
            angle: Integer, y-axis ball speed value depending on which part of the racket hit

        """

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

    def move_p2(self, keys):
        """
        Movement of the racket_p2

        
        Args:

            keys (pygame.keys.get_pressed): holds the values of current pressed keys

        """
        if keys[pygame.K_w]:
            self.racket_p2.movement(VELOCITY, dir_up=True)

        elif keys[pygame.K_s]:
            self.racket_p2.movement(VELOCITY, dir_up=False)

    def move_p1(self, keys):
        """
        Movement of the racket_p1

        
        Args:

            keys (pygame.keys.get_pressed): holds the values of current pressed keys

        """
        if keys[pygame.K_UP]:
            self.racket_p1.movement(VELOCITY, dir_up=True)

        elif keys[pygame.K_DOWN]:
            self.racket_p1.movement(VELOCITY, dir_up=False)


    def ai_movement(self):
        """
        Movement of the rackets if playing against ai

        """
        if self.ball.y_pos < self.racket_p2.y_pos + 4:
            self.racket_p2.movement_ai(dir_up = True)

        if self.ball.y_pos > self.racket_p2.y_pos + RACKET_HEIGHT - 4:
            self.racket_p2.movement_ai(dir_up = False)
