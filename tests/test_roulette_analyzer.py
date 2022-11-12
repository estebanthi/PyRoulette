import unittest

from src.roulette import Roulette
from src.analyzers.roulette_analyzer import RouletteAnalyzer


class TestRouletteAnalyzer(unittest.TestCase):

    roulette = Roulette()
    for i in range(10000000):
        roulette.spin_wheel()

    roulette_analyzer = RouletteAnalyzer(roulette)

    def test_get_analysis(self):
        analysis = self.roulette_analyzer.get_analysis()
        self.assertEqual(len(analysis), 4)

    def test_plot(self):
        analysis = self.roulette_analyzer.get_analysis()
        self.roulette_analyzer.plot_analysis(analysis)
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
