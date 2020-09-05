import pygame

from views.view_management.view_template import View
from views.view_management.view_initialization import Initializer

from objects.game_objects import Match


class MainView(View):
    def __init__(self, match: Match):

        self.match = match
        self.game = match.list_games[-1]

        self.close_window = False
        self.active = True

        self.name = 'main_view'

        self.initializer = Initializer()
        self.initializer.initialize_main_view(match=self.match)

        self.window = self.initializer.window
        self.big_square = self.initializer.big_square

        self.grid = self.initializer.grid

        # Counter message
        self.counter_message = self.initializer.counter_message
        self.counter_message.draw(window=self.window)

        # Player 1
        self.player_1_display = self.initializer.player_1_display
        self.player_1_display.draw(window=self.window)

        self.player_1_arrow = self.initializer.player_1_arrow

        self.player_1_color_display = self.initializer.player_1_color_display
        self.player_1_color_display.draw(window=self.window)

        # Player 2
        self.player_2_display = self.initializer.player_2_display
        self.player_2_display.draw(window=self.window)

        self.player_2_arrow = self.initializer.player_2_arrow

        self.player_2_color_display = self.initializer.player_2_color_display
        self.player_2_color_display.draw(window=self.window)

        # Game summary
        self.game_summary = self.initializer.game_summary

        # Draw the grid
        self.grid.draw(window=self.window, line_width=2)

    def _check_click_square(self, i_square, j_square):
        if self.grid[i_square][j_square].is_under(self.press_position) and self.grid[i_square][j_square].state == 'empty':
            # Player plays
            self.game.playing_player.play(window=self.window,
                                          in_grid=self.grid,
                                          on_square=(i_square, j_square))

            # Test end of the game

            # First: check one player has not won
            if self.grid.there_is_a_winner() != 'not':
                self.game.won = True
                self.game.winner = self.game.playing_player
                self._quit_window()

            # Second: check if the grid is full, in this case the game is tied
            elif self.grid.is_full():
                self.game.tied = True
                self._quit_window()

            self.game.change_playing_player()

    def _mouse_press(self):
        # Loop over all the squares
        for i_square in range(3):
            for j_square in range(3):
                self._check_click_square(i_square=i_square, j_square=j_square)

    # Override
    def _main_loop(self):
        self.game_summary.draw(window=self.window)

        if self.game.playing_player.name == 'Player_1':
            self.player_1_arrow.draw(window=self.window)
            self.player_2_arrow.undraw(window=self.window)
        elif self.game.playing_player.name == 'Player_2':
            self.player_2_arrow.draw(window=self.window)
            self.player_1_arrow.undraw(window=self.window)

        for event in pygame.event.get():
            # Close the window
            if event.type == pygame.QUIT:
                self.close_window = True
                self._quit_window()  # Inherited
            # Mouse click
            elif event.type == pygame.MOUSEBUTTONUP:
                self.press_position = pygame.mouse.get_pos()
                self._mouse_press()

        pygame.display.flip()
