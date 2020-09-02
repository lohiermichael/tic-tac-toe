import pygame

from initialize_objects import Initializer


class View:
    def __init__(self, window):
        self.active = True
        self.name = 'base'

        self.initializer = Initializer(view_name=self.name)

        self.window = self.initializer.window

    def _quit_window(self):
        self.active = False

    def start_main_loop(self):
        while self.active:
            self._main_loop()

    def _main_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_window()
        pygame.display.flip()


class MainView(View):
    def __init__(self):
        self.name = 'main_view'

        self.initializer = Initializer(view_name=self.name)

        self.window = self.initializer.window
        self.big_square = self.initializer.big_square
        self.grid = self.initializer.grid
        self.game = self.initializer.game

        self.active = True

    def _check_click_square(self, i_square, j_square):
        if self.grid[i_square][j_square].is_clicked(self.press_position) and self.grid[i_square][j_square].state == 'empty':
            print(self.game.playing_player.name)
            # Player plays
            self.game.playing_player.play(in_grid=self.grid,
                                          on_square=(i_square, j_square))

            # Test end of the game

            # First: check one player has not won
            if self.grid.there_is_a_winner() != 'not':
                print(f'{self.game.playing_player.name} won')
                self._quit_window()

            # Second: check if the grid is not full
            elif self.grid.is_full():
                print(f'It is a tie')
                self._quit_window()

            self.game.change_playing_player()

    def _mouse_press(self):
        # Loop over all the squares
        for i_square in range(3):
            for j_square in range(3):
                self._check_click_square(i_square=i_square, j_square=j_square)

    # Override
    def _main_loop(self):

        # Draw the grid
        self.grid.draw(line_width=2)

        for event in pygame.event.get():
            # Close the window
            if event.type == pygame.QUIT:
                self._quit_window()  # Inherited
            # Mouse click
            elif event.type == pygame.MOUSEBUTTONUP:
                self.press_position = pygame.mouse.get_pos()
                self._mouse_press()

        pygame.display.flip()
