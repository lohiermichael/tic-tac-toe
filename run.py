import pygame

from views.view_management.view_flow import ViewFlow


def run_game():
    pygame.init()
    ViewFlow()


if __name__ == "__main__":
    run_game()
