from src.strategies.strategy import Strategy
import src.bets


class Labouchere(Strategy):
    def __init__(self, initial_bet):
        super().__init__(initial_bet)
        self.sequence = [1, 1]

    def win(self, player, winnings, wheel):
        self.sequence.pop(0)
        self.sequence.pop(-1)

    def lose(self, player, wheel):
        self.sequence.append(self.bet)
        self.sequence.append(self.bet)

    def make_bets(self, player, wheel):
        if len(self.sequence) == 0:
            return []
        amount = self.sequence[0]
        bet = src.bets.Bet(src.bets.RedBlack.RED, amount)
        return [bet]

    def reset(self):
        pass
