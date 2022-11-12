import unittest
from unittest.mock import patch, MagicMock, create_autospec

from src.analyzers.player_analyzer import PlayerAnalyzer
from src.roulette_game import RouletteGame
from src.roulette import Roulette
from src.player import Player
from src.strategies.martingale import Martingale


class TestPlayerAnalyzer(unittest.TestCase):

    players = [Player("Player 1", Martingale(1))]
    roulette_game = RouletteGame(players)
    for i in range(10):
        roulette_game.play()

    def test_player_analyzer(self):
        player_analyzer = PlayerAnalyzer(self.players[0])
        analysis = player_analyzer.get_analysis()
        self.assertTrue(True)

    def test_plot(self):
        player_analyzer = PlayerAnalyzer(self.players[0])
        analysis = player_analyzer.get_analysis()
        player_analyzer.plot_analysis(analysis)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
