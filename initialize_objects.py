import pygame

from config import *
from visual_objects import Square, Grid
from player_objects import Player
from game_object import Game


def initialize_window():
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_LENGTH))
    window.fill(GREY)
    return window


window = initialize_window()


def initialize_big_square():
    big_square = Square(window=window, tl=(300, 100), tr=(900, 100))
    return big_square


big_square = initialize_big_square()


def initialize_grid():
    grid = Grid(window=window, big_square=big_square)
    return grid


def initialize_players():
    """Create two players"""
    player_1 = Player(name='player_1', sign='cross', playing=True)
    player_2 = Player(name='player_2', sign='circle', playing=False)
    return player_1, player_2


player_1, player_2 = initialize_players()


def initialize_game():
    game = Game(player_1=player_1,
                player_2=player_2,
                playing_player=player_1)

    return game
