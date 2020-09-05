from objects.visual_objects import Grid, Square


class Player:
    def __init__(self,
                 name: str,
                 sign: str = None,
                 color=None,
                 playing: bool = None):

        self.name = name
        self.sign = sign
        self.playing = playing
        self.color = color

    def play(self, window, in_grid: Grid, on_square: Square):
        i, j = on_square
        if self.sign == 'cross':
            # Draw a cross
            in_grid[i][j].change_state(window=window, new_state='cross')
        elif self.sign == 'circle':
            # Draw a circle
            in_grid[i][j].change_state(window=window, new_state='circle')
