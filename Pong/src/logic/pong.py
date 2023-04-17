import pygame
from logic.racket_logic import Racket
from logic.ball_logic import Ball

width, height = 450,400 
white = (255,255,255)
black = (0,0,0)
ball_radius = 5
racket_height = 60
racket_width = 15
velocity_ball = 4

class Pong():

    def __init__(self):
        self.racket_p2 = Racket(10, height // 2 - racket_height // 2, racket_width, racket_height, white)
        self.racket_p1 = Racket(width - 20, height // 2 - racket_height // 2, racket_width, racket_height, white)
        self.ball = Ball(width // 2, height // 2, ball_radius, white, velocity_ball)
        

    def collision(self):

        if self.ball.y + self.ball.rad >= height:
            self.ball.y_speed *= -1
        elif self.ball.y - self.ball.rad <= 0:
            self.ball.y_speed *= -1        

        # ball going right
        if self.ball.x_speed > 0:
            if self.ball.y >= self.racket_p1.y and self.ball.y <= self.racket_p1.y + racket_height:
                if self.ball.x + self.ball.rad >= self.racket_p1.x:
                    self.ball.x_speed *= -1
                    self.ball.x_speed -= 0.2
            
                    #ball redirection
                    racket_middle = self.racket_p1.y + racket_height // 2
                    angle = (self.ball.y - racket_middle) / (racket_height / 2 / velocity_ball)
                    self.ball.y_speed = angle 

        #ball going left
        else: 
            if self.ball.y >= self.racket_p2.y and self.ball.y <= self.racket_p2.y + racket_height:
                if self.ball.x - self.ball.rad <= self.racket_p2.x + racket_width:
                    self.ball.x_speed *= -1
                    self.ball.x_speed += 0.2

                    #ball redirection
                    racket_middle = self.racket_p2.y + racket_height // 2
                    angle = (self.ball.y - racket_middle) / (racket_height / 2 / velocity_ball)
                    self.ball.y_speed = angle 
        

    def move(self, keys):
        if keys[pygame.K_w]:
            self.racket_p2.movement(up=True)
            
        elif keys[pygame.K_s]:
            self.racket_p2.movement(up=False)
            
        elif keys[pygame.K_UP]:
            self.racket_p1.movement(up=True)

        elif keys[pygame.K_DOWN]:
            self.racket_p1.movement(up=False)