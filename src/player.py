class Player:
    def __init__(self, name, strategy, starting_balance=1000):
        self.name = name
        self.strategy = strategy
        self.balance = starting_balance

        self.games_played = 0
        self.cash_history = [starting_balance]
        self.bets_history = []
        self.winnings_history = []

    def receive_winnings(self, winnings, wheel):
        self.balance += winnings
        self.cash_history.append(self.balance)
        if self.balance <= 0:
            raise OutOfMoneyException("Player {} is out of money!".format(self.name))

    def win(self, winnings, wheel):
        self.strategy.win(self, winnings, wheel)
        self.winnings_history.append(winnings)

    def lose(self, wheel):
        self.strategy.lose(self, wheel)
        self.winnings_history.append(0)

    def make_bets(self, wheel):
        bets = self.strategy.make_bets(self, wheel)
        bets_amount = sum([bet.amount for bet in bets])
        self.pay(bets_amount)

        self.games_played += 1
        self.bets_history.append(bets)
        return bets

    def pay(self, amount):
        self.balance -= amount
        if self.balance < 0:
            raise OutOfMoneyException("Player {} is out of money!".format(self.name))

    def reset(self):
        self.games_played = 0
        self.cash_history = [self.cash_history[0]]
        self.bets_history = []
        self.winnings_history = []
        self.balance = self.cash_history[0]
        self.strategy.reset()


class OutOfMoneyException(Exception):
    pass
