from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def __init__(self, initial_bet):
        self.initial_bet = initial_bet
        self.bet = self.initial_bet

    @abstractmethod
    def make_bets(self, player, wheel):
        pass

    def win(self, player, winnings, wheel):
        pass

    def lose(self, player, wheel):
        pass

    def reset(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__}({self.initial_bet})"
