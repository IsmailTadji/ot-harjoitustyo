import pygame
pygame.init()

class Button():
    """
    Class for the clicking logic and drawing of buttons

    Attributes:

        rect (pygame.Rect): Rectangle that gets drawn on the screen
        clicked: Bool, stores the information if the button is clicked

    """

    def __init__(self, colour, rect_tuple):
        """
        Class constructor

        Args:

            colour: Tuple, holds the colour of the buttons
            rect_tuple: Tuple, stores x, y, width and height values of rectangle

        """
        self.colour = colour
        self.tple = rect_tuple
        self.rect = pygame.Rect(self.tple)
        self.clicked = False

    def draw_button_rect(self, screen):
        """
        Draws the rectangles on the screen

        
        Args:

            screen (pygame.surface): Pygame window where all elements are drawn

        """
        pygame.draw.rect(screen, self.colour, self.rect)


    def click(self):
        """
        Clicking logic of buttons

        Attributes:

            result: Bool, stores the information to run action after the button has been clicked
            pos (pygame.mouse.get_pos): Holds the mouse x and y values

        Returns:
            Boolean value whether the action after a button being clicked should run

        """
        result = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                result = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return result
