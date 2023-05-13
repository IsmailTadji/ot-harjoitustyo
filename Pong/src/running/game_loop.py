import pygame
from ui.menu_buttons import Buttons
from ui.draw import Draw
from config import FPS
from logic.score_logic import Score

class GameLoop:
    """
    Class for the game loop

    Attributes:
        score: Score class, to display current score of the game
        button: Buttons class, to draw buttons on the main menu
        draw: Draw class, draws everything on the screen
        player_name: Stores the name of the player when sumbitting a single player score


    """
    def __init__(self, screen, clock, pong, db_scores):
        """
        Class constructor

        Args:
            screen (pygame.surface): Pygame window where all elements are drawn
            clock (pygame.time.Clock): used to determine the refresh rate of the game
            pong: Pong class, used to reset the board and move rackets
            db_scores: Db_scores class, used to display and save scores to the leaderboard

        """
        self.pong = pong
        self.screen = screen
        self.clock = clock
        self.score = Score(self.pong.ball)
        self.button = Buttons()
        self.draw = Draw(self.screen, self.pong, self.score, self.button)
        self.db_scores = db_scores
        self.player_name = ""

    def game_loop(self):
        """
        Game loop


        Attributes:

            running: Bool, determines if game i running
            pre_game: Bool, determines if game is in pre_game state
            post_game: Bool, determines if game is in post_game screen
            menu: Bool, determines if game is in main menu
            drawn: Bool, determines if the elements are drawn while in pre_game state
            leaderboard: Bool, determines if game is in leaderboards
            single_p: Bool, determines if game is in single player mode
            score_sp: Integer, stores the single player score
            key (pygame.key.get_pressed): stores the currently pressed keys
            time: Float, stores the start time of the game

        """
        running = True
        pre_game = False
        post_game = False
        menu = True
        drawn = True
        leaderboard = False
        single_p = False
        score_sp = 0
        while running:
            self.clock.tick(FPS)
            self.events(single_p, post_game)
            if menu and not leaderboard:
                post_game = False
                self.draw.draw_buttons()
                if self.button.single_player_click():
                    single_p = True
                    menu = False
                    pre_game = True
                    drawn = False

                if self.button.two_player_click():
                    single_p = False
                    menu = False
                    pre_game = True
                    drawn = False
                if self.button.leaderboard_click():
                    leaderboard = True


            if leaderboard:
                self.draw.leaderboard(self.db_scores.top5_scores())
                key = pygame.key.get_pressed()
                if key[pygame.K_SPACE]:
                    leaderboard = False

            if not drawn:
                self.draw.draw()
                drawn = True
            # draw press single_pace to start
            if pre_game:
                self.draw.start()
                key = pygame.key.get_pressed()
                if key[pygame.K_SPACE]:
                    pre_game = False
                    self.reset(restart=False)
                if single_p:
                    time = self.score.start_time()


            if not menu and not pre_game and not post_game:
                self.pong.ball.move()
                self.pong.collision()
                self.score.point()
                self.draw.draw()
                if single_p:
                    self.pong.ai_movement()
                    self.draw.draw_score_sp(time)
                if not single_p:
                    self.draw.draw_score_tp()

            if not single_p:
            # if player scores resets the playing field
                if self.score.score_bool:
                    self.score.score_bool = False
                    self.reset(restart=False)
                # if a player reaches 5 points game ends
                if self.score.score_p1 == 5 or self.score.score_p2 == 5:
                    post_game = True

            if single_p and self.score.score_bool:
                self.score.score_bool = False
                post_game = True
                score_sp = self.score.score_sp(time)

            if post_game:
                menu = self.post_game(single_p, score_sp, post_game)




    def post_game(self, single_p, score_sp, post_game):
        """
        Post game window


        Attributes:

            key (pygame.key.get_pressed): Stores currently pressed keys


        Args:

            single_p: Bool, determines whether game is in single player
            score_sp: Integer, single player score
            post_game: determines whether post game screen is on


        Returns:

            whether menu returns to main menu or not
        """
        if post_game:
            key = pygame.key.get_pressed()
            if single_p:
                self.draw.end_screen_sp(score_sp, self.player_name)
                if key[pygame.K_RETURN]:
                    post_game = False
                    self.reset(restart=True)
                    self.player_name = self.player_name[:-1]
                    self.db_scores.new_score(self.player_name, score_sp)
                    self.player_name = ""
                    return True

            if not single_p:
                self.draw.end_screen()
                if key[pygame.K_RETURN]:
                    post_game = False
                    self.reset(restart=True)
                    return True

        return False

    def events(self,single_p, post_game):
        """
        Game events


        Attributes:

            keys (pygame.key.get_pressed): hold currently pressed keys


        Args:            

            single_p: Bool, determines whether game is in single player
            post_game: Bool, determines whether post game window is up

        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if single_p and post_game and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.player_name = self.player_name[:-1]
                else:
                    if len(self.player_name) <= 20:
                        self.player_name += event.unicode


        keys = pygame.key.get_pressed()
        self.pong.move_p1(keys)
        if not single_p:
            self.pong.move_p2(keys)



    def reset(self, restart):
        """
        Resets the score and position of elements


        Args:

            restart: Bool, whether score needs to be reset
        """
        if restart:
            self.score.score_p1 = 0
            self.score.score_p2 = 0
            restart = False
        self.pong.ball.x_pos = self.pong.ball.original_x_pos
        self.pong.ball.y_pos = self.pong.ball.original_y_pos
        self.pong.ball.x_speed = self.pong.ball.original_x_speed
        self.pong.ball.y_speed = 0
        self.pong.racket_p1.x_pos = self.pong.racket_p1.original_x_pos
        self.pong.racket_p1.y_pos = self.pong.racket_p1.original_y_pos
        self.pong.racket_p2.x_pos = self.pong.racket_p2.original_x_pos
        self.pong.racket_p2.y_pos = self.pong.racket_p2.original_y_pos
