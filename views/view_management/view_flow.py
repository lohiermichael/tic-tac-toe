import pygame

from views.view_management.view_initialization import Initializer
from views.start import StartView
from views.main import MainView
from views.final import FinalView

from objects.game_objects import Match

# FYI
from config import set_counter_message, set_final_message_win
from config import *


class ViewFlow:
    def __init__(self):
        self.set_new_view(new_view=StartView())

        self.current_match = Match(n_games=self.current_view.n_games)

        while True:
            if self.current_view.close_window:
                break
            self.display_main_view()
            if self.current_view.close_window:
                break
            self.display_final_view()
            if self.current_view.close_window:
                break
            self.display_start_view()
            if self.current_view.close_window:
                break

    def display_start_view(self):
        assert self.current_view.name == 'final_view'
        if self.current_view.restart_game:
            self.set_new_view(StartView())

    def display_main_view(self):
        assert self.current_view.name == 'start_selection_view'
        if self.current_view.start_game:
            self.set_new_view(
                MainView(counter_message=set_counter_message(self.current_view.n_games)))

    def display_final_view(self):
        assert self.current_view.name == 'main_view'
        if self.current_view.game.won:
            winner_name = self.current_view.game.winner.name
            self.set_new_view(
                FinalView(final_message=set_final_message_win(winner_name)))
        elif self.current_view.game.tied:
            self.set_new_view(FinalView(final_message=FINAL_MESSAGE_TIE))

    def set_new_view(self, new_view):
        self.current_view = new_view
        self.current_view.start_main_loop()
