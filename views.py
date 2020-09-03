import pygame

from initialize_objects import Initializer
from config import *


class View:
    def __init__(self):
        self.active = True
        self.name = 'base'
        self.close_window = False

        self.initializer = Initializer(view_name=self.name)

        self.window = self.initializer.window

    def _reset_screen(self):
        self.window.fill(GREY)

    def _quit_window(self):
        self.active = False

    def start_main_loop(self):
        while self.active:
            self._main_loop()

    def _main_loop(self):
        self._reset_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close_window = True
                self._quit_window()
        pygame.display.flip()


class StartSelectionView(View):
    def __init__(self):
        self.active = True
        self.close_window = False
        self.name = 'start_selection_view'

        self.initializer = Initializer(view_name=self.name)

        self.window = self.initializer.window

        # Start button
        self.start_button = self.initializer.start_button

        # Number games selection
        self.number_games_selection = self.initializer.number_games_selection

        self.start_game = False

        self.count1 = 0
        self.count2 = 0

    def _mouse_press(self):
        if self.start_button.is_over(self.press_position):
            self.start_game = True
            self._quit_window()

    def _mouse_over(self):
        for index_button in range(len(self.number_games_selection.list_buttons)):
            if self.number_games_selection.is_over(mouse_position=self.press_position, index_button=index_button):
                self.number_games_selection.list_buttons[index_button].border = True
            else:
                self.number_games_selection.list_buttons[index_button].border = False
            self.number_games_selection.draw(window=self.window)

    def _main_loop(self):

        self._reset_screen()
        self.number_games_selection.draw(window=self.window)
        self.start_button.draw(window=self.window)

        self.press_position = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close_window = True
                self._quit_window()

            elif event.type == pygame.MOUSEBUTTONUP:
                self._mouse_press()

            self._mouse_over()

        pygame.display.flip()


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
        if self.grid[i_square][j_square].is_over(self.press_position) and self.grid[i_square][j_square].state == 'empty':
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


class FinalView(View):
    def __init__(self, final_message):
        self.close_window = False
        self.active = True
        self.name = 'final_view'

        self.final_message = final_message

        self.initializer = Initializer(
            view_name=self.name, final_message=self.final_message)

        self.window = self.initializer.window

        # Finale message
        self.final_message = self.initializer.final_message
        self.final_message.draw(window=self.window)

        # Restart button
        self.restart_button = self.initializer.restart_button
        self.restart_button.draw(window=self.window)

        self.restart_game = False

    def _mouse_press(self):
        if self.restart_button.is_over(self.press_position):
            self.restart_game = True
            self._quit_window()

    def _main_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close_window = True
                self._quit_window()
            # Mouse click
            elif event.type == pygame.MOUSEBUTTONUP:
                self.press_position = pygame.mouse.get_pos()
                self._mouse_press()

        pygame.display.flip()


class ViewManager:
    def __init__(self):
        self.set_new_view(new_view=StartSelectionView())
        while True:
            if self.current_view.close_window:
                break
            self.display_main_view()
            if self.current_view.close_window:
                break
            self.display_final_view()
            if self.current_view.close_window:
                break
            self.display_start_selection_view()
            if self.current_view.close_window:
                break

    def display_main_view(self):
        assert self.current_view.name == 'start_selection_view'
        if self.current_view.start_game:
            self.set_new_view(MainView())

    def display_final_view(self):
        assert self.current_view.name == 'main_view'
        if self.current_view.game.won:
            winner_name = self.current_view.game.winner.name
            self.set_new_view(
                FinalView(final_message=final_message_win(winner_name)))
        elif self.current_view.game.tied:
            self.set_new_view(FinalView(final_message=FINAL_MESSAGE_TIE))

    def display_start_selection_view(self):
        assert self.current_view.name == 'final_view'
        if self.current_view.restart_game:
            self.set_new_view(StartSelectionView())

    def set_new_view(self, new_view):
        self.current_view = new_view
        self.current_view.start_main_loop()
