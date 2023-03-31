import pygame

class Racket():
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def move_setup(self, dir):
        if dir == "left":
            self.left = True
        if dir == "right":
            self.right = True
        if dir == "up":
            self.up = True
        if dir == "down":
            self.down = True
    
    def movement(self):
        if self.left:
            x += 4
            # Stop from going out of bounds
            if x > 640:
                x = 640
        if self.right:
            x -=4
            # Stop from going out of bounds
            if x < 0:
                x = 0
        if self.up:
            y -= 4
            # Stop from going out of bounds
            if y < 0:
                y = 0
        if self.down:
            y += 4
            # Stop from going out of bounds
            if y > 480:
                y = 480
    
