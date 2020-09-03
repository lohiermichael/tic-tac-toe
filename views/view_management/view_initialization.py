import pygame

from objects.visual_objects import Square, Grid, RectangularButton, CollectionRadioButtons
from objects.player_objects import Player
from objects.game_objects import Game

from config import *


class Initializer:
    def __init__(self, view_name, final_message=None):
        self.view_name = view_name
        self.final_message = final_message

        self._initialize_window()

        if self.view_name == 'base':
            pass

        elif self.view_name == 'start_selection_view':
            self._initialize_start_selection_view()

        elif self.view_name == 'main_view':
            self._initialize_main_view()

        elif self.view_name == 'final_view':
            self._initialize_final_view()

    def _initialize_window(self):
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.window.fill(GREY)

        return self.window

    def _initialize_start_selection_view(self):
        self.start_button = RectangularButton(text=START_BUTTON_TEXT,
                                              font=START_BUTTON_FONT,
                                              center=START_BUTTON_CENTER,
                                              width=START_BUTTON_WIDTH,
                                              height=START_BUTTON_HEIGHT)

        self.question_games = RectangularButton(text=QUESTION_GAMES_TEXT,
                                                font=QUESTION_GAMES_FONT,
                                                border=False,
                                                center=QUESTION_GAMES_CENTER,
                                                width=QUESTION_GAMES_WIDTH,
                                                height=QUESTION_GAMES_HEIGHT)

        self.number_games_selection = CollectionRadioButtons(collection_messages=NUMBER_GAMES_COLLECTION,
                                                             font=NUMBER_GAMES_FONT,
                                                             width=NUMBER_GAMES_WIDTH,
                                                             height=NUMBER_GAMES_HEIGHT,
                                                             center=NUMBER_GAMES_CENTER)

    def _initialize_main_view(self):
        # Initialize big square
        self.big_square = Square(tl=BIG_SQUARE_TL,
                                 tr=BIG_SQUARE_TR)
        # Initialize the grid
        self.grid = Grid(big_square=self.big_square)

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

    def _initialize_final_view(self):
        self.final_message = RectangularButton(text=self.final_message,
                                               color=GREY,
                                               font=FINAL_MESSAGE_FONT,
                                               border=False,
                                               center=WINDOW_CENTER,
                                               width=FINAL_MESSAGE_WIDTH,
                                               height=FINAL_MESSAGE_HEIGHT)

        self.restart_button = RectangularButton(text=RESTART_BUTTON_TEXT,
                                                font=START_BUTTON_FONT,
                                                center=RESTART_BUTTON_CENTER,
                                                width=RESTART_BUTTON_WIDTH,
                                                height=RESTART_BUTTON_HEIGHT)
