from src.strategies.strategy import Strategy
import src.bets


class Paroli(Strategy):
    def __init__(self, initial_bet, max_bet=1000):
        super().__init__(initial_bet)
        self.max_bet = max_bet
        self.bet = initial_bet
        self.wins = 0

    def win(self, player, winnings, wheel):
        super().win(player, winnings, wheel)
        self.wins += 1
        if self.wins == 2:
            self.bet = self.initial_bet
            self.wins = 0

    def lose(self, player, wheel):
        super().lose(player, wheel)
        self.bet = min(self.bet * 2, self.max_bet)
        self.wins = 0

    def make_bets(self, player, wheel):
        bet_type = src.bets.RedBlack.RED
        return [src.bets.Bet(bet_type, self.bet)]

    def reset(self):
        super().reset()
        self.bet = self.initial_bet
        self.wins = 0

    def __str__(self):
        return f"Paroli({self.initial_bet}, {self.max_bet})"