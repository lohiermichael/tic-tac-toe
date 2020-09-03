import pygame

pygame.font.init()

# Window size
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
WINDOW_CENTER = (int(WINDOW_WIDTH/2), int(WINDOW_HEIGHT/2))

# Colors
GREY = (247, 247, 247)
BLACK = (0, 0, 0)

############################## START SELECTION VIEW ###############################

# Start button
START_BUTTON_TEXT = 'Start playing'
START_BUTTON_WIDTH = 200
START_BUTTON_HEIGHT = 100
START_BUTTON_CENTER = (int(WINDOW_WIDTH/2), int((3/4)*WINDOW_HEIGHT))
START_BUTTON_FONT = pygame.font.SysFont('Comic Sans MS', 30)

QUESTION_GAMES_TEXT = 'Choose how many games you want to play...'
QUESTION_GAMES_FONT = pygame.font.SysFont('Comic Sans MS', 40)
QUESTION_GAMES_CENTER = (int(WINDOW_WIDTH/2), int((1/5)*WINDOW_HEIGHT))
QUESTION_GAMES_WIDTH = 600
QUESTION_GAMES_HEIGHT = 50


# Number of games
NUMBER_GAMES_COLLECTION = ['1', '3', '5']
NUMBER_GAMES_FONT = pygame.font.SysFont('Comic Sans MS', 30)
NUMBER_GAMES_WIDTH = 50
NUMBER_GAMES_HEIGHT = 150
NUMBER_GAMES_CENTER = (int(WINDOW_WIDTH/2), int((2/5)*WINDOW_HEIGHT))


#################################### MAIN VIEW ####################################

# BIG SQUARE OF THE GRID
BIG_SQUARE_TL = (100, 100)
BIG_SQUARE_TR = (700, 100)


################################## FINAL VIEW #####################################

# Button final message
FINAL_MESSAGE_WIDTH = 400
FINAL_MESSAGE_HEIGHT = 200
FINAL_MESSAGE_FONT = pygame.font.SysFont('Comic Sans MS', 40)


# Restart button
RESTART_BUTTON_TEXT = 'Restart'
RESTART_BUTTON_CENTER = (int(WINDOW_WIDTH/2), 3*int(WINDOW_HEIGHT/4))
RESTART_BUTTON_WIDTH = 200
RESTART_BUTTON_HEIGHT = 100

# Final messages
FINAL_MESSAGE_TIE = 'It is a tie'


def final_message_win(winner_name):
    return f'{winner_name} won the game'
