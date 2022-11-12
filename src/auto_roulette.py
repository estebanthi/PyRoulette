from src.roulette_game import RouletteGame
from src.player import Player


class AutoRoulette:
    def __init__(self, players):
        self.players = players
        self.game = RouletteGame(players)

    def play(self):
        self.game.play()

    def play_n_times(self, n):
        for i in range(n):
            self.play()

    def play_until(self, amount):
        while True:
            self.play()
            for player in self.players:
                if player.balance >= amount:
                    return

    def reset(self):
        for player in self.players:
            player.reset()
