from src.player import Player
from src.strategies import *
from src.probabilities_calculator import ProbabilitiesCalculator
from src.auto_roulette import AutoRoulette


if __name__ == "__main__":
    initial_balance = 100
    objective = 200
    simulations = 100000

    strategy = Martingale(10)
    player = Player("Player", strategy, initial_balance)
    roulette = AutoRoulette([player])

    probabilities_calculator = ProbabilitiesCalculator(roulette, simulations)
    proba = probabilities_calculator.reaching_x(objective)
    print("Probability of reaching {} with {} is {}".format(objective, strategy, proba))
