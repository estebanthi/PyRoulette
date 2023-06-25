from src.strategies import *
from src.analyzers import PlayerAnalyzer
from src.player import Player
from src.auto_roulette import AutoRoulette
from src.player import OutOfMoneyException


if __name__ == "__main__":
    initial_balance = 100

    strategy = Martingale(1)
    player = Player("Player", strategy, initial_balance)
    roulette = AutoRoulette([player])

    try:
        roulette.play_n_times(100)
    except OutOfMoneyException:
        print("Out of money...")

    player_analyzer = PlayerAnalyzer(player)
    player_analyzer.plot_analysis(player_analyzer.get_analysis())

