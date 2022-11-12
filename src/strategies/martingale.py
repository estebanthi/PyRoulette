from src.strategies.strategy import Strategy
import src.bets


class Martingale(Strategy):
    def __init__(self, initial_bet):
        super().__init__(initial_bet)

    def win(self, player, winnings, wheel):
        self.bet = self.initial_bet

    def lose(self, player, wheel):
        self.bet *= 2

    def make_bets(self, player, wheel):
        bet_type = src.bets.RedBlack.RED
        return [src.bets.Bet(bet_type, self.bet)]

    def reset(self):
        self.bet = self.initial_bet