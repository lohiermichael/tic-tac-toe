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


class Square:
    def __init__(self, tl, tr):

        # Top left corner
        self.tl_x, self.tl_y = tl
        # Top right corner
        self.tr_x, self.tr_y = tr
        # Distance of the square
        self.size = self.tr_x - self.tl_x

        # Bottom left corner
        self.bl_x, self.bl_y = self.tl_x, self.tl_y + dist
        self.bl = self.bl_x, self.bl_y
        # Bottom right corner
        self.br_x, self.br_y = self.tr_x, self.tr_y + dist
        self.br = self.br_x, self.br_y

    def is_clicked(self, pos_click):

        pc_x, pc_y = pos_click

        return (self.tl_x < pc_x < self.tr_x) and (self.tl_y < pc_y < self.bl_y)


class Grid(list):
    def __init__(self, big_square: Square):
        """Build it from the big square that wraps him up

           It will be a list of 3 lists, each one having three Square elements
        """

        self.big_square = big_square

        size = self.big_square / 3

        # First layer
        square_1 = Square(tl=big_square.tl,
                          tr=(big_square.tl_x+size, big_square.tl_y))
        square_2 = Square(tl=square_1.tr,
                          tr=(square_1.tr_x+size, square_1, tr_y))
        square_3 = Square(tl=square_2.tr,
                          tr=(square_2.tr_x+size, square_2, tr_y))

        # Second layer
        square_4 = Square(tl=(square_1.tl_x, square_1.tl_y+size),
                          tr=(square_1.tr_x, square_1.tr_y+size))
        square_5 = Square(tl=square_4.tr,
                          tr=(square_4.tr_x+size, square_4, tr_y))
        square_6 = Square(tl=square_5.tr,
                          tr=(square_5.tr_x+size, square_5, tr_y))

        # Third layer
        square_7 = Square(tl=(square_4.tl_x, square_4.tl_y+size),
                          tr=(square_4.tr_x, square_4.tr_y+size))
        square_8 = Square(tl=square_7.tr,
                          tr=(square_7.tr_x+size, square_7, tr_y))
        square_9 = Square(tl=square_8.tr,
                          tr=(square_8.tr_x+size, square_8, tr_y))

        self.append([square_1, square_2, square_3])
        self.append([square_4, square_5, square_6])
        self.append([square_7, square_8, square_9])





big_square = Square(top_left_corner=(300, 100), top_right_corner=(900, 100))
grid = Grid(big_square=big_square)


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
            pos_click = pygame.mouse.get_pos()
            print(pos)

    # Make the most recently drawn screen visible.
    pygame.display.flip()

pygame.quit()
