import pygame

from config import *
from visual_objects import Square, Grid, Button
from player_objects import Player
from game_objects import Game


class Initializer:
    def __init__(self, view_name):
        self.view_name = view_name

        self._initialize_window()

        if self.view_name == 'base':
            pass

        elif self.view_name == 'main_view':
            self._initialize_main_view()

        elif self.view_name == 'start_selection_view':
            self._initialize_start_selection_view()

    def _initialize_window(self):
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_LENGTH))
        self.window.fill(GREY)

        return self.window

    def _initialize_main_view(self):
        # Initialize big square
        self.big_square = Square(window=self.window,
                                 tl=BIG_SQUARE_TL,
                                 tr=BIG_SQUARE_TR)
        # Initialize the grid
        self.grid = Grid(window=self.window, big_square=self.big_square)

        # Initialize the two players
        self.player_1 = Player(name='player_1',
                               sign='cross',
                               playing=True)
        self.player_2 = Player(name='player_2',
                               sign='circle',
                               playing=False)

        # Initialize the game
        self.game = Game(player_1=self.player_1,
                         player_2=self.player_2,
                         playing_player=self.player_1)

    def _initialize_start_selection_view(self):
        self.central_start_button = Button(window=self.window,
                                           center=WINDOW_CENTER,
                                           width=START_BUTTON_WIDTH,
                                           height=START_BUTTON_HEIGHT)
