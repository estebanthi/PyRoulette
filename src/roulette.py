import random

from src.pockets_builder import PocketsBuilder


class Roulette:

    def __init__(self, two_zeroes=False):
        self.numbers = range(0, 37)
        if two_zeroes:
            self.numbers = range(-1, 37)

        self.pockets_builder = PocketsBuilder(self.numbers)
        self.pockets = self.pockets_builder.build_pockets()

        self.ball = None
        self.wheel = []

    def spin_wheel(self):
        self.ball = random.choice(self.numbers)
        self.wheel.append(self.ball)

    def get_current(self):
        return self.ball

    def get_wheel(self):
        return self.wheel

    def get_pocket(self, number):
        return self.pockets[number]
