import pygame

from views.view_management.view_template import View
from views.view_management.view_initialization import Initializer


class FinalView(View):
    def __init__(self, final_message):
        self.close_window = False
        self.active = True
        self.name = 'final_view'

        self.initializer = Initializer()
        self.initializer.initialize_final_view(
            final_message_text=final_message)

        self.window = self.initializer.window

        # Finale message
        self.final_message = self.initializer.final_message
        self.final_message.draw(window=self.window)

        # Restart button
        self.restart_button = self.initializer.restart_button
        self.restart_button.draw(window=self.window)

        self.restart_game = False

    def _mouse_press(self):
        if self.restart_button.is_under(self.press_position):
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
