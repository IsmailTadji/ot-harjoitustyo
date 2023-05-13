import pygame
from config import WIDTH, HEIGHT, BLACK, WHITE, FONT, FONT_END
#initialise pygame to update the screen
pygame.init()


class Draw:
    """
    Class for drawing all elements on the screen

    """
    def __init__(self, screen, pong, score, button):
        """
        Class constructor

        Args:
        
            screen (pygame.surface): Pygame window where all elements are drawn
            pong: Pong class, used to draw all pong elements
            score: Score class, used to get game scores
            button: Button class, used to draw menu buttons

        """
        self.screen = screen
        self.pong = pong
        self.score = score
        self.button = button


    def draw_buttons(self):
        """
        Drawing main menu buttons
        """
        self.screen.fill(BLACK)
        self.button.single_player(self.screen)
        self.button.two_player(self.screen)
        self.button.leaderboard(self.screen)
        pygame.display.update()


    def draw(self):
        """
        Draw ball and rackets
        """
        self.screen.fill((BLACK))
        self.pong.racket_p1.draw_racket(self.screen)
        self.pong.racket_p2.draw_racket(self.screen)
        self.pong.ball.draw_ball(self.screen)
        pygame.display.update()

    def draw_score_tp(self):
        """
        Draw two player scores mid game

        
        Attributes:
        
            p1_score (FONT.render): used to render p1_score
            p2_score (FONT.render): used to render p2_score

        """
        p1_score = FONT.render(f"{self.score.score_p1}", 1, WHITE)
        p2_score = FONT.render(f"{self.score.score_p2}", 1, WHITE)
        self.screen.blit(p1_score, (WIDTH * (3 / 4) - p1_score.get_width() // 2, 15))
        self.screen.blit(p2_score, (WIDTH // 4 - p2_score.get_width() // 2, 15))
        pygame.display.update()


    def draw_score_sp(self, time):
        """
        Draw single player score mid game


        Attributes:

            p1_score (FONT.render): used to render p1_score

        
        Args:

            time: Int, time spent ingame
        """
        p1_score = FONT.render(f"{self.score.score_sp(time)}", 1, WHITE)
        self.screen.blit(p1_score, (WIDTH // 2 - p1_score.get_width() // 2, 15))
        pygame.display.update()

    def end_screen(self):
        """
        Draws end screen for two player mode

        
        Attributes:

            end_text (FONT_END.render): renders game end text
            new_game (FONT_END.render): renders new game text

        """
        self.screen.fill(BLACK)
        if self.score.score_p1 > self.score.score_p2:
            winner = "Player 1"
        else:
            winner = "Player 2"
        end_text = FONT_END.render(f"{winner} wins! Final score: {self.score.score_p1} - {self.score.score_p2}", 1, WHITE)
        new_game = FONT_END.render("Press Enter to return to main menu", 1, WHITE)
        self.screen.blit(end_text, (WIDTH // 2 - end_text.get_width() // 2,\
                                     HEIGHT // 2 - end_text.get_height() // 2))
        self.screen.blit(new_game, (WIDTH // 2 - new_game.get_width() // 2,\
                                     HEIGHT // 2 + 40 - new_game.get_height() // 2))
        pygame.display.update()

    def end_screen_sp(self, time, player_name):
        """
        End screen for single player mode


        Attributes:

            player_name_text (FONT_END.render): renders instructions to enter name
            player name input box (pygame.Rect): defines a box for the name
            end_text (FONT_END.render): renders game end text
            new_game (FONT_END.render): renders new game text
        
        Args:

            time: Int, final score for single player
            player_name: String, name of the player
        """
        self.screen.fill(BLACK)

        player_name_text = FONT_END.render("Enter your name to save your score:", 1, WHITE)
        
        player_name_input_box = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 40, 300, 40)
        pygame.draw.rect(self.screen, WHITE, player_name_input_box, 2)

        # Render player name text
        player_name = FONT_END.render(player_name, 1, WHITE)
        self.screen.blit(player_name_text, (WIDTH // 2 - player_name_text.get_width() // 2, HEIGHT //2 - 5))
        self.screen.blit(player_name, (player_name_input_box.x + 5, player_name_input_box.y + 5))

        end_text = FONT_END.render(f"You lost! Final score: {time}", 1, WHITE)
        new_game = FONT_END.render("Press Enter to return to main menu", 1, WHITE)

        self.screen.blit(end_text, (WIDTH // 2 - end_text.get_width() // 2,\
                                    HEIGHT // 2 - 100))
        self.screen.blit(new_game, (WIDTH // 2 - new_game.get_width() // 2,\
                                    HEIGHT // 2 +150 - new_game.get_height() // 2))     
        pygame.display.update()   

    def start(self):
        """
        Game start screen


        Attributes:
            start_text (FONT_END.render): renders the start text
        """
        start_text = FONT_END.render("Press space to start", 1, WHITE)
        self.screen.blit(start_text,(WIDTH // 2 - start_text.get_width() // 2,\
                                      HEIGHT//2 - 40 - start_text.get_height() // 2))
        pygame.display.update()

    def leaderboard(self, lb_scores):
        """
        Leaderboard screen


        Args:
        
            lb_scores: List, holds the names of players and their scores
        """
        self.screen.fill(BLACK)
        leaderboards_header = FONT_END.render("Single player leaderboards:",1,WHITE)
        return_text = FONT_END.render("Press space to return to main menu",1,WHITE)
        self.screen.blit(leaderboards_header, (WIDTH//2 - leaderboards_header.get_width() // 2, 50))
        self.screen.blit(return_text, (WIDTH//2 - return_text.get_width()//2, 300))

        lb_y = 100
        placement = 1
        for values in lb_scores:
            temp_string = FONT_END.render(f"{placement}. {values[0]}: {values[1]}", 1, WHITE)
            self.screen.blit(temp_string, (100 //2, lb_y))
            lb_y += 30
            placement += 1
        pygame.display.update()

