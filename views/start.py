import pygame

from views.view_management.view_template import View
from views.view_management.view_initialization import Initializer


class StartView(View):
    def __init__(self):
        self.active = True
        self.close_window = False
        self.name = 'start_view'

        self.initializer = Initializer()
        self.initializer.initialize_start_view()

        self.window = self.initializer.window

        # Game title
        self.game_title = self.initializer.game_title
        self.game_title.draw(window=self.window)

        # Game logo
        self.game_logo = self.initializer.game_logo
        self.game_logo.draw(window=self.window)

        # Start button
        self.start_button = self.initializer.start_button
        self.start_button.draw(window=self.window)

        # Question game
        self.question_games = self.initializer.question_games
        self.question_games.draw(window=self.window)

        # Number games selection
        self.number_games_selection = self.initializer.number_games_selection

        self.start_game = False
        self.n_games = None

    def _mouse_press(self):
        # Start a game
        if self.start_button.is_under(self.mouse_position) and self.n_games:
            self.start_game = True
            self._quit_window()

        # Select a new number of games in the upcoming match
        for index_button, button in enumerate(self.number_games_selection.list_buttons):
            if self.number_games_selection.is_under(mouse_position=self.mouse_position, index_button=index_button):
                self.number_games_selection.draw_selected(window=self.window,
                                                          index_selected_button=index_button)
                self.n_games = int(
                    self.number_games_selection.list_buttons[index_button].text)

    def _mouse_over(self):

        # Hover over the number of games
        for index_button in range(len(self.number_games_selection.list_buttons)):
            if self.number_games_selection.is_under(mouse_position=self.mouse_position, index_button=index_button):
                self.number_games_selection.draw_hovered(window=self.window,
                                                         index_hovered_button=index_button)

    def _main_loop(self):

        self.number_games_selection.draw(window=self.window)

        self.mouse_position = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close_window = True
                self._quit_window()

            elif event.type == pygame.MOUSEBUTTONUP:
                self._mouse_press()

            self._mouse_over()

        pygame.display.flip()
