import pygame

from views.view_management.view_template import View
from views.view_management.view_initialization import Initializer


class MainView(View):
    def __init__(self):
        self.close_window = False
        self.active = True

        self.name = 'main_view'

        self.initializer = Initializer(view_name=self.name)

        self.window = self.initializer.window
        self.big_square = self.initializer.big_square
        self.grid = self.initializer.grid
        self.game = self.initializer.game

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
