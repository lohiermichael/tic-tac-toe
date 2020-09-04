from objects.player_objects import Player


class Game:
    def __init__(self,
                 player_1: Player = None,
                 player_2: Player = None,
                 playing_player: Player = None):

        assert playing_player in [player_1, player_2]

        # Only one of the players should be playing
        assert (player_1.playing and not player_2.playing) or (
            player_2.playing and not player_1.playing)

        self.player_1 = player_1
        self.player_2 = player_2
        self.playing_player = playing_player

        self.won = False
        self.winner = None
        self.tied = False

    def change_playing_player(self):

        if self.player_1.playing:
            self.player_1.playing = False
            self.player_2.playing = True
            self.playing_player = self.player_2

        elif self.player_2.playing:
            self.player_2.playing = False
            self.player_1.playing = True
            self.playing_player = self.player_1


class Match:
    def __init__(self,
                 n_games: int,
                 player_1: Player = None,
                 player_2: Player = None):

        self.n_games = n_games
        self.player_1 = player_1
        self.player_2 = player_2

        self.game_number = 0
        self.list_games = []

        # {'game_1': 'player_1', 'game_1': 'playing',
        #     'game_3': 'pending'}
        self.status_by_game = None

        self.there_is_winner = False
