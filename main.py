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


playing = True


class Square:
    def __init__(self, tl, tr):

        # Top left corner
        self.tl = tl
        self.tl_x, self.tl_y = self.tl
        # Top right corner
        self.tr = tr
        self.tr_x, self.tr_y = self.tr
        # Distance of the square
        self.size = self.tr_x - self.tl_x

        # Bottom left corner
        self.bl_x, self.bl_y = self.tl_x, self.tl_y + self.size
        self.bl = self.bl_x, self.bl_y
        # Bottom right corner
        self.br_x, self.br_y = self.tr_x, self.tr_y + self.size
        self.br = self.br_x, self.br_y

    def is_clicked(self, pos_click):

        pc_x, pc_y = pos_click

        return (self.tl_x < pc_x < self.tr_x) and (self.tl_y < pc_y < self.bl_y)


class Grid(list):
    def __init__(self, window, big_square: Square):
        """Build it from the big square that wraps him up

           It will be a list of 3 lists, each one having three Square elements
        """
        self.window = window

        self.big_square = big_square

        size = self.big_square.size / 3

        # First layer
        square_1 = Square(tl=big_square.tl,
                          tr=(big_square.tl_x+size, big_square.tl_y))
        square_2 = Square(tl=square_1.tr,
                          tr=(square_1.tr_x+size, square_1.tr_y))
        square_3 = Square(tl=square_2.tr,
                          tr=(square_2.tr_x+size, square_2.tr_y))

        # Second layer
        square_4 = Square(tl=(square_1.tl_x, square_1.tl_y+size),
                          tr=(square_1.tr_x, square_1.tr_y+size))
        square_5 = Square(tl=square_4.tr,
                          tr=(square_4.tr_x+size, square_4.tr_y))
        square_6 = Square(tl=square_5.tr,
                          tr=(square_5.tr_x+size, square_5.tr_y))

        # Third layer
        square_7 = Square(tl=(square_4.tl_x, square_4.tl_y+size),
                          tr=(square_4.tr_x, square_4.tr_y+size))
        square_8 = Square(tl=square_7.tr,
                          tr=(square_7.tr_x+size, square_7.tr_y))
        square_9 = Square(tl=square_8.tr,
                          tr=(square_8.tr_x+size, square_8.tr_y))

        self.append([square_1, square_2, square_3])
        self.append([square_4, square_5, square_6])
        self.append([square_7, square_8, square_9])

    def draw(self, line_width=1):
        # Horizontal lines
        pygame.draw.line(self.window, BLACK,
                         self[0][0].bl, self[0][2].br, line_width)
        pygame.draw.line(self.window, BLACK,
                         self[2][0].tl, self[2][2].tr, line_width)

        # Vertical lines
        pygame.draw.line(self.window, BLACK,
                         self[0][0].tr, self[2][0].br, line_width)
        pygame.draw.line(self.window, BLACK,
                         self[0][2].tl, self[2][2].bl, line_width)


big_square = Square(tl=(300, 100), tr=(900, 100))
grid = Grid(big_square=big_square, window=window)


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
                        print(i, j)

    # Make the most recently drawn screen visible.
    pygame.display.flip()

pygame.quit()
