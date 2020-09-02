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

    def is_clicked(self, press_position):

        pp_x, pp_y = press_position
        return (self.tl_x < pp_x < self.tr_x) and (self.tl_y < pp_y < self.bl_y)

    def draw(self, line_width=1):
        # Left, Top, Width, height
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

    def is_full(self):
        # All the squares are not empty
        return set(self[i][j].state != 'empty' for i in range(3) for j in range(3)) == {True}

    def there_is_a_winner(self) -> str:
        """Tells if the grid has a winner or not

        Returns:
            str: if not winner: 'not',
                 if winner: 'cross' or 'circle'
        """

        # Check rows
        for i in range(3):
            if (self[i][0].state == self[i][1].state == self[i][2].state) and (self[i][0].state != 'empty'):
                return self[i][0].state

        # Check columns
        for j in range(3):
            if (self[0][j].state == self[1][j].state == self[2][j].state) and (self[0][j].state != 'empty'):
                return self[0][j].state

        # Check diagonals
        if (self[0][0].state == self[1][1].state == self[2][2].state) and (self[1][1].state != 'empty'):
            return self[1][1].state
        if (self[0][2].state == self[1][1].state == self[2][0].state) and (self[1][1].state != 'empty'):
            return self[1][1].state

        return 'not'


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


class Button():
    def __init__(self, window, color=BLACK, center=None, height=None, width=None):
        self.window = window
        self.color = color

        self.center = center
        self.center_x, self.center_y = self.center

        self.width = width
        self.height = height

        self.x = self.center_x - int(self.width/2)
        self.y = self.center_y - int(self.height/2)

        # self.text = text

    def draw(self, outline=True, outline_depth=2, line_width=1):
        """Call this method to draw a button on the screen"""

        if outline:
            pygame.draw.rect(self.window, outline, (self.x-outline_depth,
                                                    self.y - outline_depth,
                                                    self.width+outline_depth*2,
                                                    self.height+outline_depth*2), line_width)

        pygame.draw.rect(self.window, self.color, (self.x,
                                                   self.y,
                                                   self.width,
                                                   self.height), line_width)

        # if self.text != '':
        #     text = BUTTON_FONT.render(self.text, line_width, (0, 0, 0))
        #     self.window.blit(text, (self.x + (self.width/2 - text.get_width()/2),
        #                             self.y + (self.height/2 - text.get_height()/2)))

    def is_pressed(self, press_position):

        pp_x, pp_y = press_position

        return (self.x < pp_x < self.x+self.width) and (self.y < pp_y < self.y+self.height)
