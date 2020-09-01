import pygame
import sys


WINDOW_WIDTH = 1200
WINDOW_LENGTH = 800


# Colors
GREY = (247, 247, 247)
BLACK = (0, 0, 0)

# Make the window
pygame.init()

# FONTS
# arial_font = pygame.font.SysFont("arial", 20)


window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_LENGTH))
window.fill(GREY)


def draw_grid():
    # Horizontal lines
    pygame.draw.line(window, BLACK, (300, 300), (900, 300), 1)
    pygame.draw.line(window, BLACK, (300, 500), (900, 500), 1)

    # Vertical lines
    pygame.draw.line(window, BLACK, (500, 100), (500, 700), 1)
    pygame.draw.line(window, BLACK, (700, 100), (700, 700), 1)


playing = True

# Main loop
while playing:

    draw_grid()

    # an event is a click on the mouth or on the key of the keyboard or else
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            print('closed manually')

        # Handle MOUSEBUTTONUP
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)

    # Make the most recently drawn screen visible.
    pygame.display.flip()

pygame.quit()
