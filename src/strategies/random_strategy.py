import random

from src.strategies.strategy import Strategy
import src.bets


class RandomStrategy(Strategy):

    def __init__(self, initial_bet):
        super().__init__(initial_bet)
        self.bets = [src.bets.Number.ONE, src.bets.Number.TWO, src.bets.Number.THREE, src.bets.Number.FOUR,
                     src.bets.Number.FIVE, src.bets.Number.SIX, src.bets.Number.SEVEN, src.bets.Number.EIGHT,
                     src.bets.Number.NINE, src.bets.Number.TEN, src.bets.Number.ELEVEN, src.bets.Number.TWELVE,
                     src.bets.Number.THIRTEEN, src.bets.Number.FOURTEEN, src.bets.Number.FIFTEEN,
                     src.bets.Number.SIXTEEN, src.bets.Number.SEVENTEEN, src.bets.Number.EIGHTEEN,
                     src.bets.Number.NINETEEN, src.bets.Number.TWENTY, src.bets.Number.TWENTY_ONE,
                     src.bets.Number.TWENTY_TWO, src.bets.Number.TWENTY_THREE, src.bets.Number.TWENTY_FOUR,
                     src.bets.Number.TWENTY_FIVE, src.bets.Number.TWENTY_SIX, src.bets.Number.TWENTY_SEVEN,
                     src.bets.Number.TWENTY_EIGHT, src.bets.Number.TWENTY_NINE, src.bets.Number.THIRTY,
                     src.bets.Number.THIRTY_ONE, src.bets.Number.THIRTY_TWO, src.bets.Number.THIRTY_THREE,
                     src.bets.Number.THIRTY_FOUR, src.bets.Number.THIRTY_FIVE, src.bets.Number.THIRTY_SIX]

    def make_bets(self, player, wheel):
        bet_type = random.choice(self.bets)
        bet_amount = self.initial_bet

        random_bet = src.bets.Bet(bet_type, bet_amount)
        return [random_bet]
