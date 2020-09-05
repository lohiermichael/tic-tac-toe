import pygame

pygame.font.init()

GAME_NAME = 'Tic Tac Toe'


# Window size
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
WINDOW_CENTER = (int(WINDOW_WIDTH/2), int(WINDOW_HEIGHT/2))

# Colors
GREY = (247, 247, 247)
BLACK = (0, 0, 0)
RED = (254, 30, 30)
GREEN = (30, 91, 54)

# Images

# Arrow
ARROW_IMAGE_PATH = './img/arrow.png'
ARROW_DIMENSIONS = (50, 15)

# Color display
COLOR_DISPLAY_PLAYER_1_IMAGE_PATH = './img/color_display_player_1.png'
COLOR_DISPLAY_PLAYER_2_IMAGE_PATH = './img/color_display_player_2.png'
COLOR_DISPLAY_DIMENSIONS = (60, 50)

############################## START SELECTION VIEW ###############################

# Question on the number of games to play
QUESTION_GAMES_TEXT = 'Choose how many games you want to play...'
QUESTION_GAMES_FONT = pygame.font.SysFont('Comic Sans MS', 40)
QUESTION_GAMES_CENTER = (int(WINDOW_WIDTH/2), int((4/10)*WINDOW_HEIGHT))
QUESTION_GAMES_WIDTH = 600
QUESTION_GAMES_HEIGHT = 50


# Number of games
NUMBER_GAMES_COLLECTION = ['1', '3', '5']
NUMBER_GAMES_FONT = pygame.font.SysFont('Comic Sans MS', 30)
NUMBER_GAMES_WIDTH = 150
NUMBER_GAMES_HEIGHT = 50
NUMBER_GAMES_CENTER = (int(WINDOW_WIDTH/2), int((5/10)*WINDOW_HEIGHT))

# Start button
START_BUTTON_TEXT = 'Start playing'
START_BUTTON_WIDTH = 200
START_BUTTON_HEIGHT = 100
START_BUTTON_CENTER = (int(WINDOW_WIDTH/2), int((8/10)*WINDOW_HEIGHT))
START_BUTTON_FONT = pygame.font.SysFont('Comic Sans MS', 30)


#################################### MAIN VIEW ####################################

# Big square of the grid
BIG_SQUARE_TL = (100, 100)
BIG_SQUARE_TR = (700, 100)

# Counter message
COUNTER_MESSAGE_FONT = pygame.font.SysFont('Comic Sans MS', 40)
COUNTER_MESSAGE_CENTER = (950, 100)
COUNTER_MESSAGE_WIDTH = 200
COUNTER_MESSAGE_HEIGHT = 100


def set_counter_message(n_games, game_number):
    return f'You are playing game {game_number}/{n_games}'


# Player 1 display
PLAYER_1_DISPLAY_FONT = pygame.font.SysFont('Comic Sans MS', 30)
PLAYER_1_DISPLAY_CENTER = (950, 300)
PLAYER_1_DISPLAY_WIDTH = 100
PLAYER_1_DISPLAY_HEIGHT = 50

PLAYER_1_ARROW_CENTER = (
    PLAYER_1_DISPLAY_CENTER[0] - 75, PLAYER_1_DISPLAY_CENTER[1])

PLAYER_1_COLOR_DISPLAY_CENTER = (
    PLAYER_1_DISPLAY_CENTER[0] + 90, PLAYER_1_DISPLAY_CENTER[1])

# Player 2 display
PLAYER_2_DISPLAY_FONT = pygame.font.SysFont('Comic Sans MS', 30)
PLAYER_2_DISPLAY_CENTER = (950, 350)
PLAYER_2_DISPLAY_WIDTH = 100
PLAYER_2_DISPLAY_HEIGHT = 50

PLAYER_2_ARROW_CENTER = (
    PLAYER_2_DISPLAY_CENTER[0] - 75, PLAYER_2_DISPLAY_CENTER[1])

PLAYER_2_COLOR_DISPLAY_CENTER = (
    PLAYER_2_DISPLAY_CENTER[0] + 90, PLAYER_2_DISPLAY_CENTER[1])


# Game summary
GAME_SUMMARY_CENTER = (900, 150)
GAME_SUMMARY_HEIGHT = 70
GAME_SIZE = 40


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


def set_final_message_win(winner_name):
    return f'{winner_name} won the game'
