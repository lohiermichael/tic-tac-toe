from objects.player_objects import Player

from config import *


class Game:
    def __init__(self,
                 player_1: Player = None,
                 player_2: Player = None,
                 starting_player: Player = None):

        assert starting_player.name in [player_1.name, player_2.name]

        self.player_1 = player_1
        self.player_2 = player_2
        self.starting_player = starting_player
        self.playing_player = starting_player

        self._define_players_signs()
        self._define_player_colors()

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

    def _define_players_signs(self):

        if self.starting_player == self.player_1:
            self.player_1.sign = 'cross'
            self.player_2.sign = 'circle'
        elif self.starting_player == self.player_2:
            self.player_2.sign = 'cross'
            self.player_1.sign = 'circle'

    def _define_player_colors(self):
        self.player_1.color = RED
        self.player_2.color = GREEN


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

    def choose_next_starting_player(self):
        assert self.list_games, "One game needs to be played"

        self.last_game = self.list_games[-1]

        if self.last_game.starting_player == self.last_game.player_1:
            return self.last_game.player_2
        else:
            return self.last_game.player_1
