import unittest
from mock import patch, MagicMock

from src.roulette import Roulette
from src.roulette_game import RouletteGame
from src.strategies.random_strategy import RandomStrategy
from src.player import Player
from src.player import OutOfMoneyException
from src.bets import Bet, RedBlack


class TestRouletteGame(unittest.TestCase):

    def test_play(self):
        players = [Player("Player1", RandomStrategy())]
        game = RouletteGame(players)
        game.play()
        self.assertTrue(game.roulette.get_current() in range(0, 37))

    @patch('src.roulette_game.RouletteGame.calculate_winnings')
    def test_player_win(self, mock_calculate_winnings):
        mock_calculate_winnings.return_value = 10
        players = [Player("Player1", RandomStrategy())]
        game = RouletteGame(players)
        game.play()
        self.assertEqual(players[0].balance, 1009)


if __name__ == '__main__':
    unittest.main()
