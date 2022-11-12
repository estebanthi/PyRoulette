import matplotlib.pyplot as plt

from src.player import Player
from src.analyzers.analyzer import Analyzer


class PlayerAnalyzer(Analyzer):

    def __init__(self, player: Player):
        self.player = player

    def get_analysis(self):
        wins = sum([1 for win in self.player.winnings_history if win > 0])
        losses = sum([1 for win in self.player.winnings_history if win == 0])
        win_rate = wins / (wins + losses)

        biggest_win = max(self.player.winnings_history)

        biggest_win_streak = self.get_biggest_win_streak()
        biggest_loss_streak = self.get_biggest_loss_streak()

        risk_over_time = [sum([bet.amount for bet in round]) for round in self.player.bets_history]
        max_risk = max(risk_over_time)

        drawdown_over_time = [self.player.cash_history[i] - max(self.player.cash_history[:i + 1]) for i in
                                range(len(self.player.cash_history))]
        max_drawdown = max(drawdown_over_time)
        max_drawdown_percentage = max_drawdown / self.player.cash_history[0]

        return {
            "wins": wins,
            "losses": losses,
            "win_rate": win_rate,
            "biggest_win": biggest_win,
            "biggest_win_streak": biggest_win_streak,
            "biggest_loss_streak": biggest_loss_streak,
            "risk_over_time": risk_over_time,
            "max_risk": max_risk,
            "drawdown_over_time": drawdown_over_time,
            "max_drawdown": max_drawdown,
            "max_drawdown_percentage": max_drawdown_percentage,
            "cash_history": self.player.cash_history,
        }

    def get_biggest_win_streak(self):
        biggest_win_streak = 0
        current_win_streak = 0
        for win in self.player.winnings_history:
            if win > 0:
                current_win_streak += 1
            else:
                if current_win_streak > biggest_win_streak:
                    biggest_win_streak = current_win_streak
                current_win_streak = 0
        return biggest_win_streak

    def get_biggest_loss_streak(self):
        biggest_loss_streak = 0
        current_loss_streak = 0
        for win in self.player.winnings_history:
            if win == 0:
                current_loss_streak += 1
            else:
                if current_loss_streak > biggest_loss_streak:
                    biggest_loss_streak = current_loss_streak
                current_loss_streak = 0
        return biggest_loss_streak

    def plot_analysis(self, analysis):
        plt.plot(analysis["cash_history"])
        plt.title("Cash over time")
        plt.show()

        plt.plot(analysis["risk_over_time"])
        plt.title("Risk over time")
        plt.show()

        plt.plot(analysis["drawdown_over_time"])
        plt.title("Drawdown over time")
        plt.show()

    def print_analysis(self, analysis):
        print("Wins: {}".format(analysis["wins"]))
        print("Losses: {}".format(analysis["losses"]))
        print("Win rate: {}".format(analysis["win_rate"]))
        print("Biggest win: {}".format(analysis["biggest_win"]))
        print("Biggest win streak: {}".format(analysis["biggest_win_streak"]))
        print("Biggest loss streak: {}".format(analysis["biggest_loss_streak"]))
        print("Max risk: {}".format(analysis["max_risk"]))
        print("Max drawdown: {}".format(analysis["max_drawdown"]))
        print("Max drawdown percentage: {}".format(analysis["max_drawdown_percentage"]))
        print("Final cash: {}".format(analysis["cash_history"][-1]))
