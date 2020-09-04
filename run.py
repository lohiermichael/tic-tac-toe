import pygame

from views.view_management.view_flow import ViewFlow

from config import GAME_NAME


def run_game():
    pygame.init()
    pygame.display.set_caption(GAME_NAME)
    ViewFlow()


if __name__ == "__main__":
    run_game()
