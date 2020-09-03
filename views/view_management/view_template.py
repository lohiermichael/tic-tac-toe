import pygame

from views.view_management.view_initialization import Initializer

from config import *


class View:
    """Parent object"""

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
