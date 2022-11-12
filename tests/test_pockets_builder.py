import unittest

from src.pockets_builder import PocketsBuilder
from src import bets


class TestPocketsBuilder(unittest.TestCase):

    def test_build_pockets(self):
        numbers = range(-1, 37)
        pockets_builder = PocketsBuilder(numbers)
        pockets = pockets_builder.build_pockets()
        self.assertEqual(len(pockets), 38)
        self.assertEqual(pockets[-1], [bets.Number.DOUBLE_ZERO])
        self.assertEqual(pockets[1], [bets.Number.ONE, bets.RedBlack.RED])


if __name__ == '__main__':
    unittest.main()
