import pygame

pygame.font.init()

# Window size
WINDOW_WIDTH = 1200
WINDOW_LENGTH = 800
WINDOW_CENTER = (int(WINDOW_WIDTH/2), int(WINDOW_LENGTH/2))

# Colors
GREY = (247, 247, 247)
BLACK = (0, 0, 0)

# BIG SQUARE OF THE GRID
BIG_SQUARE_TL = (300, 100)
BIG_SQUARE_TR = (900, 100)


# Start button
START_BUTTON_WIDTH = 200
START_BUTTON_HEIGHT = 100

# Button final message
FINAL_MESSAGE_WIDTH = 400
FINAL_MESSAGE_HEIGHT = 200

# Fonts
BUTTON_FONT = pygame.font.SysFont('Comic Sans MS', 30)
FINAL_MESSAGE_FONT = pygame.font.SysFont('Comic Sans MS', 50)
