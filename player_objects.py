from visual_objects import Grid


class Player:
    def __init__(self, name: str, sign: str, playing: bool):
        assert sign in ['cross', 'circle']
        self.name = name
        self.sign = sign
        self.playing = playing

    def play(self, window, in_grid: Grid, on_square):
        i, j = on_square
        if self.sign == 'cross':
            # Draw a cross
            in_grid[i][j].change_state(window=window, new_state='cross')
        elif self.sign == 'circle':
            # Draw a circle
            in_grid[i][j].change_state(window=window, new_state='circle')
