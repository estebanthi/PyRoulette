from src.roulette import Roulette


class RouletteGame:
    def __init__(self, players):
        self.players = players
        self.roulette = Roulette()
        self.bets = {}

    def play(self):
        wheel = self.roulette.wheel

        for player in self.players:
            self.bets[player] = player.make_bets(wheel)

        self.roulette.spin_wheel()

        for player in self.players:
            player_winnings = self.calculate_winnings(player)
            player.win(player_winnings, wheel) if player_winnings > 0 else player.lose(wheel)
            player.receive_winnings(player_winnings, wheel)

    def calculate_winnings(self, player):
        player_bets = self.bets[player]
        player_winnings = 0
        for bet in player_bets:
            player_winnings += bet.calculate_winnings(self.roulette)
        return player_winnings
