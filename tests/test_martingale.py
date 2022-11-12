import unittest
from unittest.mock import patch, MagicMock, create_autospec

from src.strategies.martingale import MartingaleStrategy
from src.roulette_game import RouletteGame
from src.roulette import Roulette
from src.player import Player


class TestMartingale(unittest.TestCase):

    def test_martingale(self):
        roulette = Roulette()
        player = Player("Player", MartingaleStrategy(10))
        game = RouletteGame([player])
        for i in range(3):
            game.play()
        self.assertIn(player.balance, range(0, 1100))


if __name__ == '__main__':
    unittest.main()
