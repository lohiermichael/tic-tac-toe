import pygame

from config import *
from visual_objects import Square, Grid
from player_objects import Player
from game_object import Game
from initialize_objects import *


pygame.init()

window = initialize_window()
big_square = initialize_big_square()
grid = initialize_grid()

player_1, player_2 = initialize_players()
game = initialize_game()
playing_player = game.playing_player
# Main loop
while game.on:

    # Draw the grid
    grid.draw(line_width=2)

    # An event is a click on the mouth or on the key of the keyboard or else
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            print('closed manually')

        elif event.type == pygame.MOUSEBUTTONUP:
            pos_click = pygame.mouse.get_pos()
            for i in range(3):
                for j in range(3):
                    if grid[i][j].is_clicked(pos_click):
                        game.playing_player.play(in_grid=grid,
                                                 on_square=(i, j))
                        game.change_playing_player()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

pygame.quit()
