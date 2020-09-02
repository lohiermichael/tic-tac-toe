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

# Main loop
while game.on:

    # Draw the grid
    grid.draw(line_width=2)

    # An event is a click on the mouth or on the key of the keyboard or else
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.on = False
            break
            print('closed manually')

        elif event.type == pygame.MOUSEBUTTONUP:
            pos_click = pygame.mouse.get_pos()
            for i in range(3):
                for j in range(3):
                    if grid[i][j].is_clicked(pos_click) and grid[i][j].state == 'empty':
                        print(game.playing_player.name)
                        game.playing_player.play(in_grid=grid,
                                                 on_square=(i, j))

                        # End of the game

                        # First: check one player has not won
                        if grid.there_is_a_winner() != 'not':
                            print(f'{game.playing_player.name} won')
                            game.on = False

                        # Second: check if the grid is not full
                        elif grid.is_full():
                            print(f'It is a tie')
                            game.on = False

                        game.change_playing_player()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

pygame.quit()
