import pygame

from config import *
from visual_objects import Square, Grid


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
