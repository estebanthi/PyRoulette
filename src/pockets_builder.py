from src import bets


class PocketsBuilder:
    def __init__(self, numbers):
        self.numbers = numbers

    def build_pockets(self):
        pockets = {}
        for i in self.numbers:
            pockets[i] = []
            if i == -1:
                pockets[i].append(bets.Number.DOUBLE_ZERO)
            if i == 0:
                pockets[i].append(bets.Number.ZERO)
            if i == 1:
                pockets[i].append(bets.Number.ONE)
                pockets[i].append(bets.RedBlack.RED)
            if i == 2:
                pockets[i].append(bets.Number.TWO)
                pockets[i].append(bets.RedBlack.BLACK)
            if i == 3:
                pockets[i].append(bets.Number.THREE)
                pockets[i].append(bets.RedBlack.RED)
            if i == 4:
                pockets[i].append(bets.Number.FOUR)
                pockets[i].append(bets.RedBlack.BLACK)
            if i == 5:
                pockets[i].append(bets.Number.FIVE)
                pockets[i].append(bets.RedBlack.RED)
            if i == 6:
                pockets[i].append(bets.Number.SIX)
                pockets[i].append(bets.RedBlack.BLACK)
            if i == 7:
                pockets[i].append(bets.Number.SEVEN)
                pockets[i].append(bets.RedBlack.RED)
            if i == 8:
                pockets[i].append(bets.Number.EIGHT)
                pockets[i].append(bets.RedBlack.BLACK)
            if i == 9:
                pockets[i].append(bets.Number.NINE)
                pockets[i].append(bets.RedBlack.RED)
            if i == 10:
                pockets[i].append(bets.Number.TEN)
                pockets[i].append(bets.RedBlack.BLACK)
            if i == 11:
                pockets[i].append(bets.Number.ELEVEN)
                pockets[i].append(bets.RedBlack.BLACK)
            if i == 12:
                pockets[i].append(bets.Number.TWELVE)
                pockets[i].append(bets.RedBlack.RED)
            if i == 13:
                pockets[i].append(bets.Number.THIRTEEN)
                pockets[i].append(bets.RedBlack.BLACK)
            if i == 14:
                pockets[i].append(bets.Number.FOURTEEN)
                pockets[i].append(bets.RedBlack.RED)
            if i == 15:
                pockets[i].append(bets.Number.FIFTEEN)
                pockets[i].append(bets.RedBlack.BLACK)
            if i == 16:
                pockets[i].append(bets.Number.SIXTEEN)
                pockets[i].append(bets.RedBlack.RED)
            if i == 17:
                pockets[i].append(bets.Number.SEVENTEEN)
                pockets[i].append(bets.RedBlack.BLACK)
            if i == 18:
                pockets[i].append(bets.Number.EIGHTEEN)
                pockets[i].append(bets.RedBlack.RED)
            if i == 19:
                pockets[i].append(bets.Number.NINETEEN)
                pockets[i].append(bets.RedBlack.RED)
            if i == 20:
                pockets[i].append(bets.Number.TWENTY)
                pockets[i].append(bets.RedBlack.BLACK)
            if i == 21:
                pockets[i].append(bets.Number.TWENTY_ONE)
                pockets[i].append(bets.RedBlack.RED)
            if i == 22:
                pockets[i].append(bets.Number.TWENTY_TWO)
                pockets[i].append(bets.RedBlack.BLACK)
            if i == 23:
                pockets[i].append(bets.Number.TWENTY_THREE)
                pockets[i].append(bets.RedBlack.RED)
            if i == 24:
                pockets[i].append(bets.Number.TWENTY_FOUR)
                pockets[i].append(bets.RedBlack.BLACK)
            if i == 25:
                pockets[i].append(bets.Number.TWENTY_FIVE)
                pockets[i].append(bets.RedBlack.RED)
            if i == 26:
                pockets[i].append(bets.Number.TWENTY_SIX)
                pockets[i].append(bets.RedBlack.BLACK)
            if i == 27:
                pockets[i].append(bets.Number.TWENTY_SEVEN)
                pockets[i].append(bets.RedBlack.RED)
            if i == 28:
                pockets[i].append(bets.Number.TWENTY_EIGHT)
                pockets[i].append(bets.RedBlack.BLACK)
            if i == 29:
                pockets[i].append(bets.Number.TWENTY_NINE)
                pockets[i].append(bets.RedBlack.BLACK)
            if i == 30:
                pockets[i].append(bets.Number.THIRTY)
                pockets[i].append(bets.RedBlack.RED)
            if i == 31:
                pockets[i].append(bets.Number.THIRTY_ONE)
                pockets[i].append(bets.RedBlack.BLACK)
            if i == 32:
                pockets[i].append(bets.Number.THIRTY_TWO)
                pockets[i].append(bets.RedBlack.RED)
            if i == 33:
                pockets[i].append(bets.Number.THIRTY_THREE)
                pockets[i].append(bets.RedBlack.BLACK)
            if i == 34:
                pockets[i].append(bets.Number.THIRTY_FOUR)
                pockets[i].append(bets.RedBlack.RED)
            if i == 35:
                pockets[i].append(bets.Number.THIRTY_FIVE)
                pockets[i].append(bets.RedBlack.BLACK)
            if i == 36:
                pockets[i].append(bets.Number.THIRTY_SIX)
                pockets[i].append(bets.RedBlack.RED)

        return pockets
