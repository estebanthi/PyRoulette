import matplotlib.pyplot as plt

from src.auto_roulette import AutoRoulette
from src.player import OutOfMoneyException
import src.player


class ProbabilitiesCalculator:
    def __init__(self, roulette_game, number_of_simulations):
        self.roulette_game = roulette_game
        self.number_of_simulations = number_of_simulations

    def multiply_balance_by_x(self, x, initial_balance):
        success = 0
        for i in range(self.number_of_simulations):
            try:
                self.roulette_game.reset()
                self.roulette_game.play_until(initial_balance * x)
                success += 1
            except OutOfMoneyException:
                pass
        return success / self.number_of_simulations

    def reaching_x(self, x):
        success = 0
        for i in range(self.number_of_simulations):
            try:
                self.roulette_game.reset()
                self.roulette_game.play_until(x)
                success += 1
            except OutOfMoneyException:
                pass
        return success / self.number_of_simulations

    @staticmethod
    def find_best_strategy_to_reach_x(x, initial_balance, strategies, number_of_simulations=1000):
        best_proba = 0
        best_strategy = None
        for strategy in strategies:
            roulette_game = AutoRoulette([src.player.Player("John", strategy, initial_balance)])
            probabilities_calculator = ProbabilitiesCalculator(roulette_game, number_of_simulations)
            proba = probabilities_calculator.reaching_x(x)
            if proba > best_proba:
                best_proba = proba
                best_strategy = strategy
        return best_strategy, best_proba

    def plot_proba_of_reaching_x_times_the_initial_balance(self, initial_balance, n_steps=30):
        probabilities = []
        for i in range(n_steps):
            probabilities.append(self.multiply_balance_by_x(1 + i / n_steps, initial_balance))
        plt.plot(probabilities)
        plt.title("Probability of reaching x times the initial balance")
        plt.xlabel("x")
        plt.ylabel("Probability")

        n_x_ticks = 5
        plt.xticks([i * (n_steps // n_x_ticks) for i in range(n_x_ticks + 1)], [1 + i * (n_steps // n_x_ticks) / n_steps for i in range(n_x_ticks + 1)])

        plt.show()

    def plot_proba_of_reaching_x(self, initial_balance, n_steps=30):
        probabilities = []
        for i in range(n_steps):
            probabilities.append(self.reaching_x(initial_balance + i))
        plt.plot(probabilities)
        plt.title("Probability of reaching x")
        plt.xlabel("x")
        plt.ylabel("Probability")

        n_x_ticks = 5
        plt.xticks([i * (n_steps // n_x_ticks) for i in range(n_x_ticks + 1)], [initial_balance + i * (n_steps // n_x_ticks) for i in range(n_x_ticks + 1)])

        plt.show()
