import pygame
from config import *


class Square:
    def __init__(self, tl=None, tr=None, state='empty', color=BLACK):
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

    def draw(self, window, line_width=1):
        # Left, Top, Width, height
        pygame.draw.rect(window, self.color,
                         (self.left, self.top, self.size, self.size), line_width)

    def is_under(self, mouse_position):

        mp_x, mp_y = mouse_position
        return (self.tl_x < mp_x < self.tr_x) and (self.tl_y < mp_y < self.bl_y)

    def change_state(self, window, new_state):

        self.state = new_state

        if self.state == 'circle':
            #  Draw a circle in the square
            Circle(center=self.center,
                   radius=int(self.size/4)).draw(window=window)

        elif self.state == 'cross':
            # Draw a cross in the square
            cross_tl = (self.tl_x + int(self.size/4),
                        self.tl_y + int(self.size/4))
            Cross(tl=cross_tl,
                  size=int(self.size/2)).draw(window=window)


class Grid(list):
    def __init__(self, big_square: Square = None, color=BLACK):
        """Build it from the big square that wraps him up

           It will be a list of 3 lists, each one having three Square elements
        """

        self.color = color

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

    def draw(self, window, line_width=1):
        # Horizontal lines
        pygame.draw.line(window, self.color,
                         self[0][0].bl, self[0][2].br, line_width)
        pygame.draw.line(window, self.color,
                         self[2][0].tl, self[2][2].tr, line_width)

        # Vertical lines
        pygame.draw.line(window, self.color,
                         self[0][0].tr, self[2][0].br, line_width)
        pygame.draw.line(window, self.color,
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
    def __init__(self, color=BLACK, center=None, radius=None):
        self.center = center
        self.radius = radius
        self.color = color

    def draw(self, window, line_width=1):
        pygame.draw.circle(window, self.color,
                           self.center, self.radius, line_width)


class Cross:
    def __init__(self, color=BLACK, tl=None, size=None):
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

    def draw(self, window, line_width=1):
        """Draw two crossing diagonal lines"""

        pygame.draw.line(window, self.color, self.tl, self.br, line_width)
        pygame.draw.line(window, self.color, self.tr, self.bl, line_width)


class RectangularButton():
    def __init__(self, font, color=BLACK, center=None, border=True, x=None, y=None, height=None, width=None, text=''):
        self.color = color
        self.font = font
        self.border = border

        self.width = width
        self.height = height

        # You can define the position of the button by center...
        if center:
            self.center = center
            self.center_x, self.center_y = self.center
            self.x = self.center_x - int(self.width/2)
            self.y = self.center_y - int(self.height/2)

        # ...or x and y
        if x and y:
            self.x = x
            self.y = y
            self.center = (self.x + int(self.width/2),
                           self.y + int(self.height/2))

        self.text = text

    def draw(self, window, outline=True, outline_thinkness=2):
        """Call this method to draw a button on the screen"""

        line_width = 1 if self.border else -1

        if outline:
            pygame.draw.rect(window, outline, (self.x-outline_thinkness,
                                               self.y - outline_thinkness,
                                               self.width+outline_thinkness*2,
                                               self.height+outline_thinkness*2), line_width)

        pygame.draw.rect(window, self.color, (self.x,
                                              self.y,
                                              self.width,
                                              self.height), line_width)

        if self.text != '':
            text = self.font.render(self.text, line_width, BLACK)
            window.blit(text, (self.x + (self.width/2 - text.get_width()/2),
                               self.y + (self.height/2 - text.get_height()/2)))

    def undraw(self, window):
        pygame.draw.rect(window, GREY, (self.x,
                                        self.y,
                                        self.width,
                                        self.height), 0)

    def is_under(self, mouse_position):

        mp_x, mp_y = mouse_position
        return (self.x < mp_x < self.x+self.width) and (self.y < mp_y < self.y+self.height)


class CollectionRadioButtons:
    """Multiple circular buttons and some text with it"""

    def __init__(self, collection_messages=None, font=None, color=BLACK, width=None, height=None, center=None):

        self.color = color
        self.width = width
        self.height = height
        self.collection_messages = collection_messages
        self.font = font

        self.center = center
        self.center_x, self.center_y = self.center

        self.x = self.center_x - int(self.width/2)
        self.y = self.center_y - int(self.height/2)

        self.list_buttons = self._define_buttons()

        self.selected_button = None

    def _define_buttons(self):

        self.number_buttons = len(self.collection_messages)
        self.width_button = int(self.width/self.number_buttons)

        return [
            RectangularButton(font=self.font,
                              color=self.color,
                              border=False,
                              x=self.x + i_button * self.width_button,
                              y=self.y,
                              width=self.width_button,
                              height=self.height,
                              text=self.collection_messages[i_button])
            for i_button in range(self.number_buttons)
        ]

    def draw(self, window):

        for button in self.list_buttons:
            button.draw(window=window, outline=False)

    def is_under(self, mouse_position, index_button):

        button = self.list_buttons[index_button]
        mp_x, mp_y = mouse_position
        return (button.x < mp_x < button.x+button.width) and (button.y < mp_y < button.y+button.height)

    def draw_selected(self, window, index_selected_button):
        for index_button, button in enumerate(self.list_buttons):
            if index_button == index_selected_button:
                button.border = True
                self.selected_button = button
            else:
                button.undraw(window=window)
                button.border = False
                button.draw(window=window)

    def draw_hovered(self, window, index_hovered_button):
        for index_button, button in enumerate(self.list_buttons):
            if index_button == index_hovered_button:
                button.border = True
            elif button == self.selected_button:
                button.border = True
            else:
                button.undraw(window=window)
                button.border = False
                button.draw(window=window)


class Arrow:
    def __init__(self, center):

        self.image = pygame.image.load(ARROW_IMAGE_PATH)
        self.image = pygame.transform.scale(self.image, ARROW_DIMENSIONS)

        self.width, self.height = ARROW_DIMENSIONS
        self.center = center
        self.c_x, self.c_y = self.center

        self.x = self.c_x - int(self.width/2)
        self.y = self.c_y - int(self.height/2)

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def undraw(self, window):
        pygame.draw.rect(window, GREY, (self.x,
                                        self.y,
                                        self.width,
                                        self.height), 0)
