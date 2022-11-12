import unittest
from unittest.mock import patch, MagicMock, create_autospec

from src.auto_roulette import AutoRoulette
from src.player import Player
from src.roulette import Roulette
from src.strategies.random_strategy import RandomStrategy


class TestAutoRoulette(unittest.TestCase):

    def test_play_1000_times(self):
        player = Player("PLayer 1", RandomStrategy())
        auto_roulette = AutoRoulette([player])
        auto_roulette.play_n_times(1000)
        self.assertEqual(player.games_played, 1000)

    @patch('src.roulette_game.RouletteGame.calculate_winnings')
    def test_play_until_1100(self, mock_calculate_winnings):
        mock_calculate_winnings.return_value = 10
        player = Player("PLayer 1", RandomStrategy())
        auto_roulette = AutoRoulette([player])
        auto_roulette.play_until(1100)
        self.assertTrue(player.balance >= 1100)
        self.assertEqual(player.games_played, 12)


if __name__ == '__main__':
    unittest.main()
