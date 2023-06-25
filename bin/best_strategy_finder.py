from src.probabilities_calculator import ProbabilitiesCalculator
from src.strategies import *
import src.bets


if __name__ == "__main__":
    initial_balance = 100
    objective = 1000
    simulations = 1000000

    strategies = [Martingale(1), Martingale(10), Martingale(100), Dalembert(1), Dalembert(10), Dalembert(100),
                  Paroli(1), Paroli(10), Paroli(100), Fibonacci(1), Fibonacci(10), Fibonacci(100),
                  AllIn(src.bets.RedBlack.RED)]
    best_strategy, best_proba = ProbabilitiesCalculator.find_best_strategy_to_reach_x(objective, initial_balance,
                                                                                      strategies, simulations)
    print("Best strategy to reach {} is {} with a probability of {}".format(objective, best_strategy, best_proba))