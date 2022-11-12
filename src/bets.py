from enum import Enum


class Bet:
    def __init__(self, bet_type, amount):
        self.bet_type = bet_type
        self.amount = amount
        if self.amount < 0:
            raise ValueError("Bet amount must be positive")

    def calculate_winnings(self, roulette):
        if self.win(roulette):
            return self.amount * self.bet_type.odds.value + self.amount
        return 0

    def win(self, roulette):
        pockets = roulette.pockets
        current = roulette.get_current()
        return self.bet_type in pockets[current]


class Number(Enum):
    odds = 35
    DOUBLE_ZERO = "00"
    ZERO = "0"
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    ELEVEN = "11"
    TWELVE = "12"
    THIRTEEN = "13"
    FOURTEEN = "14"
    FIFTEEN = "15"
    SIXTEEN = "16"
    SEVENTEEN = "17"
    EIGHTEEN = "18"
    NINETEEN = "19"
    TWENTY = "20"
    TWENTY_ONE = "21"
    TWENTY_TWO = "22"
    TWENTY_THREE = "23"
    TWENTY_FOUR = "24"
    TWENTY_FIVE = "25"
    TWENTY_SIX = "26"
    TWENTY_SEVEN = "27"
    TWENTY_EIGHT = "28"
    TWENTY_NINE = "29"
    THIRTY = "30"
    THIRTY_ONE = "31"
    THIRTY_TWO = "32"
    THIRTY_THREE = "33"
    THIRTY_FOUR = "34"
    THIRTY_FIVE = "35"
    THIRTY_SIX = "36"


class Column(Enum):
    odds = 2
    FIRST = "first"
    SECOND = "second"
    THIRD = "third"


class Dozen(Enum):
    odds = 2
    FIRST = "1-12"
    SECOND = "13-24"
    THIRD = "25-36"


class EvenOdd(Enum):
    odds = 1
    EVEN = 1
    ODD = 2


class RedBlack(Enum):
    odds = 1
    RED = "red"
    BLACK = "black"


class LowHigh(Enum):
    odds = 1
    LOW = "low"
    HIGH = "high"
