import pygame

from config import *
from visual_objects import Square, Grid
from initialize_objects import *


pygame.init()

window = initialize_window()
big_square = initialize_big_square()
grid = initialize_grid()


playing = True

# Main loop
while playing:

    grid.draw(line_width=2)

    # an event is a click on the mouth or on the key of the keyboard or else
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            print('closed manually')

        # Handle MOUSEBUTTONUP
        if event.type == pygame.MOUSEBUTTONUP:
            pos_click = pygame.mouse.get_pos()
            for i in range(3):
                for j in range(3):
                    if grid[i][j].is_clicked(pos_click):
                        grid[i][j].change_state(new_state='circle')

    # Make the most recently drawn screen visible.
    pygame.display.flip()

pygame.quit()
