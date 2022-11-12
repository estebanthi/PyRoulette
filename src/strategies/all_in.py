from src.strategies.strategy import Strategy
import src.bets


class AllIn(Strategy):
    def __init__(self, bet_type):
        super().__init__(initial_bet=0)
        self.bet_type = bet_type

    def make_bets(self, player, wheel):
        return [src.bets.Bet(self.bet_type, player.balance)]
