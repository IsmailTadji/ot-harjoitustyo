import pygame
from logic.button_logic import Button
from config import WIDTH, WHITE, FONT_END, BLACK
pygame.init()


class Buttons():
    """
    Class for buttons


    Attributes:
        sp_button: Button class, makes a single player button
        sp_text: String, text that goes on of top single player button
        tp_button: Button class, makes a two player button
        tp_text: String, text that goes on top of two player button
        lb_button: Button class, makes a leaderboard button
        lb_text: String, text that goes on top of leaderboard button

    """
    def __init__(self):
        """
        Class constructor
        """
        self.sp_button = Button(WHITE, (WIDTH//2 -75 , 60, 150, 60))
        self.sp_text = "Single player"
        self.tp_button = Button(WHITE, (WIDTH//2 - 75, 160, 150, 60))
        self.tp_text = "Two player"
        self.lb_button = Button(WHITE, (WIDTH//2 - 75, 260, 150, 60))
        self.lb_text = "Leaderboard"

    def single_player(self, screen):
        """
        Drawing single player button

        Attributes:
            sp_text (FONT_END.render): renders self.sp_text

        Args:
            screen (pygame.surface): Pygame window where all elements are drawn

        """
        self.sp_button.draw_button_rect(screen)
        sp_text = FONT_END.render(f"{self.sp_text}", 1, BLACK)
        screen.blit(sp_text, (WIDTH//2 - sp_text.get_width() // 2, 80))

      
    def single_player_click(self):  
        """
        Returns:
            Bool value whether button has been clicked
        """
        return self.sp_button.click()
    
    def two_player(self, screen):
        """
        Drawing two player button

        Attributes:
            tp_text (FONT_END.render): renders self.tp_text

        Args:
            screen (pygame.surface): Pygame window where all elements are drawn
        """
        self.tp_button.draw_button_rect(screen)
        tp_text = FONT_END.render(f"{self.tp_text}", 1, BLACK)
        screen.blit(tp_text, (WIDTH//2 - tp_text.get_width() // 2, 180))

    def two_player_click(self):
        """
        Returns:
            Bool value whether button has been clicked
        """
        return self.tp_button.click()
    
    def leaderboard(self, screen):
        """
        Draws leaderboard button

        Attributes:
            lb_text (FONT_END.render): renders self.lb_text

        Args:
            screen (pygame.surface): Pygame window where all elements are drawn

        """
        self.lb_button.draw_button_rect(screen)
        lb_text = FONT_END.render(f"{self.lb_text}", 1, BLACK)
        screen.blit(lb_text, (WIDTH//2 - lb_text.get_width() // 2, 280))

    def leaderboard_click(self):
        """
        Returns:
            Bool value whether button has been clicked
        """
        return self.lb_button.click()
