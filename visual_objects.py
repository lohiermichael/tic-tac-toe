import pygame
from config import *


class Square:
    def __init__(self, window, tl=None, tr=None, state='empty', color=BLACK):

        self.window = window
        self.color = color
        self.state = state

        # Top left corner
        self.tl = tl
        self.tl_x, self.tl_y = self.tl
        # Top right corner
        self.tr = tr
        self.tr_x, self.tr_y = self.tr

        # Size of the square
        self.size = self.tr_x - self.tl_x

        # Bottom left corner
        self.bl_x, self.bl_y = self.tl_x, self.tl_y + self.size
        self.bl = self.bl_x, self.bl_y
        # Bottom right corner
        self.br_x, self.br_y = self.tr_x, self.tr_y + self.size
        self.br = self.br_x, self.br_y

        # For the draw function
        self.left = self.bl_x
        self.top = self.tl_y

        # Center
        self.center = int((self.tl_x + self.tr_x) /
                          2), int((self.tl_y + self.bl_y)/2)
        self.center_x, self.center_y = self.center

    def is_clicked(self, pos_click):

        pc_x, pc_y = pos_click

        return (self.tl_x < pc_x < self.tr_x) and (self.tl_y < pc_y < self.bl_y)

    def draw(self, line_width=1):
        # Left, Top, Width, Height
        pygame.draw.rect(self.window, self.color,
                         (self.left, self.top, self.size, self.size), line_width)

    def change_state(self, new_state):

        self.state = new_state

        if self.state == 'circle':
            #  Draw a circle in the square
            Circle(window=self.window, center=self.center,
                   radius=int(self.size/4)).draw()

        elif self.state == 'cross':
            # Draw a cross in the square
            cross_tl = (self.tl_x + int(self.size/4),
                        self.tl_y + int(self.size/4))
            Cross(window=self.window, tl=cross_tl,
                  size=int(self.size/2)).draw()


class Grid(list):
    def __init__(self, window, big_square: Square = None, color=BLACK):
        """Build it from the big square that wraps him up

           It will be a list of 3 lists, each one having three Square elements
        """

        self.window = window
        self.color = color

        self.big_square = big_square

        size = self.big_square.size / 3

        # First layer
        square_1 = Square(window=self.window, tl=big_square.tl,
                          tr=(big_square.tl_x+size, big_square.tl_y))
        square_2 = Square(window=self.window, tl=square_1.tr,
                          tr=(square_1.tr_x+size, square_1.tr_y))
        square_3 = Square(window=self.window, tl=square_2.tr,
                          tr=(square_2.tr_x+size, square_2.tr_y))

        # Second layer
        square_4 = Square(window=self.window, tl=(square_1.tl_x, square_1.tl_y+size),
                          tr=(square_1.tr_x, square_1.tr_y+size))
        square_5 = Square(window=self.window, tl=square_4.tr,
                          tr=(square_4.tr_x+size, square_4.tr_y))
        square_6 = Square(window=self.window, tl=square_5.tr,
                          tr=(square_5.tr_x+size, square_5.tr_y))

        # Third layer
        square_7 = Square(window=self.window, tl=(square_4.tl_x, square_4.tl_y+size),
                          tr=(square_4.tr_x, square_4.tr_y+size))
        square_8 = Square(window=self.window, tl=square_7.tr,
                          tr=(square_7.tr_x+size, square_7.tr_y))
        square_9 = Square(window=self.window, tl=square_8.tr,
                          tr=(square_8.tr_x+size, square_8.tr_y))

        self.append([square_1, square_2, square_3])
        self.append([square_4, square_5, square_6])
        self.append([square_7, square_8, square_9])

    def draw(self, line_width=1):
        # Horizontal lines
        pygame.draw.line(self.window, self.color,
                         self[0][0].bl, self[0][2].br, line_width)
        pygame.draw.line(self.window, self.color,
                         self[2][0].tl, self[2][2].tr, line_width)

        # Vertical lines
        pygame.draw.line(self.window, self.color,
                         self[0][0].tr, self[2][0].br, line_width)
        pygame.draw.line(self.window, self.color,
                         self[0][2].tl, self[2][2].bl, line_width)


class Circle:
    def __init__(self, window, color=BLACK, center=None, radius=None):
        self.window = window
        self.center = center
        self.radius = radius
        self.color = color

    def draw(self, line_width=1):
        pygame.draw.circle(self.window, self.color,
                           self.center, self.radius, line_width)


class Cross:
    def __init__(self, window, color=BLACK, tl=None, size=None):
        self.window = window
        # The size of the square in witch the cross is included
        self.size = size
        self.color = color

        # Top left corner
        self.tl = tl
        self.tl_x, self.tl_y = self.tl

        # Top right corner
        self.tr_x = self.tl_x + size
        self.tr_y = self.tl_y
        self.tr = self.tr_x, self.tr_y

        # Bottom left corner
        self.bl_x = self.tl_x
        self.bl_y = self.tl_y + size
        self.bl = self.bl_x, self.bl_y

        # Bottom right corner
        self.br_x = self.tr_x
        self.br_y = self.tr_y + size
        self.br = self.br_x, self.br_y

    def draw(self, line_width=1):
        """Draw two crossing diagonal lines"""

        pygame.draw.line(self.window, self.color, self.tl, self.br, line_width)
        pygame.draw.line(self.window, self.color, self.tr, self.bl, line_width)
