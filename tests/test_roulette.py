import unittest
from unittest.mock import patch, MagicMock, create_autospec

from src.roulette import Roulette


class TestRoulette(unittest.TestCase):

    def test_spin_wheel(self):
        roulette = Roulette()
        roulette.spin_wheel()
        self.assertIn(roulette.get_current(), roulette.numbers)
        self.assertIn(roulette.get_current(), roulette.get_history())


if __name__ == '__main__':
    unittest.main()
