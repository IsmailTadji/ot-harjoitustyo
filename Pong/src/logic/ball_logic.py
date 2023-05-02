import pygame

WIDTH, HEIGHT = 450, 400

class Ball():
    def __init__(self, x_pos, y_pos, rad, colour, velocity):
        #save original position for resetting the window after a point
        self.x_pos = self.original_x_pos = x_pos
        self.y_pos = self.original_y_pos = y_pos
        #ball size
        self.rad = rad
        #save original speed to reset it after a point
        self.x_speed = self.original_x_speed = velocity
        self.y_speed = 0
        self.colour = colour

    # draw the ball on the screen
    def draw_ball(self, screen):
        pygame.draw.circle(screen, self.colour, (self.x_pos, self.y_pos), self.rad)

    # movement logic of the ball
    def move(self):
        self.x_pos += self.x_speed
        self.y_pos += self.y_speed
