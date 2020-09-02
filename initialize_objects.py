import pygame

from config import *
from visual_objects import Square, Grid
from player_objects import Player
from game_objects import Game


class Initializer:
    def __init__(self, view_name):
        self.view_name = view_name

        if self.view_name == 'base':
            self.initialize_window()
        elif self.view_name == 'main_view':
            self.initialize_window()
            self.initialize_big_square()
            self.initialize_grid()
            self.initialize_players()
            self.initialize_game()

    def initialize_window(self):
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_LENGTH))
        self.window.fill(GREY)

        return self.window

    def initialize_big_square(self):
        self.big_square = Square(window=self.window,
                                 tl=BIG_SQUARE_TL,
                                 tr=BIG_SQUARE_TR)

        return self.big_square

    def initialize_grid(self):
        self.grid = Grid(window=self.window, big_square=self.big_square)

        return self.grid

    def initialize_players(self):
        """Create two players"""
        self.player_1 = Player(name='player_1', sign='cross', playing=True)
        self.player_2 = Player(name='player_2', sign='circle', playing=False)

    def initialize_game(self):
        self.game = Game(player_1=self.player_1,
                         player_2=self.player_2,
                         playing_player=self.player_1)

        return self.game
