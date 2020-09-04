import pygame

from views.view_management.view_initialization import Initializer
from views.start import StartView
from views.main import MainView
from views.final import FinalView

from objects.player_objects import Player
from objects.game_objects import Game, Match

# FYI
from config import set_counter_message, set_final_message_win
from config import *


class ViewFlow:
    def __init__(self):
        self.set_new_view(new_view=StartView())

        # After the start view we create a game object that we pass to the main view

        while True:

            self.current_match = Initializer().initialize_match(match_view=self.current_view)
            if self.current_view.close_window:
                return

            # Condition to continue playing:
            # Condition 1 : the match still have some games to be played
            # Condition 2 : there is not a winner yet
            while (self.current_match.game_number < self.current_match.n_games) and (not self.current_match.there_is_winner):

                self.display_main_view()

                if self.current_view.close_window:
                    return

            self.display_final_view()
            if self.current_view.close_window:
                return
            self.display_start_view()
            if self.current_view.close_window:
                return

    def display_start_view(self):
        assert self.current_view.name == 'final_view'
        if self.current_view.restart_game:
            self.set_new_view(StartView())

    def display_main_view(self):

        assert self.current_view.name in ['start_view', 'main_view']

        if self.current_view.name == 'main_view':
            self.current_match.game_number += 1
            # Update the match after the game is played
            self.current_match = self.current_view.match
            new_game = Game(player_1=self.current_match.player_1,
                            player_2=self.current_match.player_2,
                            starting_player=self.current_match.choose_next_starting_player())  # TODO To test
            self.current_match.list_games.append(new_game)

        self.set_new_view(MainView(match=self.current_match))

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
