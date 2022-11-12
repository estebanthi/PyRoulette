import matplotlib.pyplot as plt
import pandas as pd

import src.bets as bets
from src.analyzers.analyzer import Analyzer


class RouletteAnalyzer(Analyzer):
    def __init__(self, roulette):
        self.roulette = roulette

    def get_analysis(self):
        roulette = self.roulette
        wheel = roulette.wheel

        number_hits = {number: 0 for number in roulette.numbers}
        for spin in wheel:
            number_hits[spin] += 1

        color_hits = {bets.RedBlack.BLACK: 0, bets.RedBlack.RED: 0}
        for spin in wheel:
            pocket = roulette.get_pocket(spin)
            color = bets.RedBlack.RED if bets.RedBlack.RED in pocket else bets.RedBlack.BLACK
            color_hits[color] += 1

        biggest_color_streaks = {bets.RedBlack.BLACK: 0, bets.RedBlack.RED: 0}
        current_color_streaks = {bets.RedBlack.BLACK: 0, bets.RedBlack.RED: 0}
        current_color = None
        for spin in wheel:
            pocket = roulette.get_pocket(spin)
            color = bets.RedBlack.RED if bets.RedBlack.RED in pocket else bets.RedBlack.BLACK
            if color == current_color:
                current_color_streaks[color] += 1
            else:
                current_color_streaks[color] = 1
                current_color = color
            if current_color_streaks[color] > biggest_color_streaks[color]:
                biggest_color_streaks[color] = current_color_streaks[color]

        biggest_number_streaks = {number: 0 for number in roulette.numbers}
        current_number_streaks = {number: 0 for number in roulette.numbers}
        current_number = None
        for spin in wheel:
            if spin == current_number:
                current_number_streaks[spin] += 1
            else:
                current_number_streaks[spin] = 1
                current_number = spin
            if current_number_streaks[spin] > biggest_number_streaks[spin]:
                biggest_number_streaks[spin] = current_number_streaks[spin]

        dataframes = []
        for name, hits in [("Number", number_hits), ("Color", color_hits)]:
            df = pd.DataFrame.from_dict(hits, orient="index", columns=["Hits"])
            df.index.name = name

            df["Percentage"] = df["Hits"] / df["Hits"].sum() * 100

            dataframes.append(df)

        for name, streaks in [("Biggest Number Streaks", biggest_number_streaks), ("Biggest Color Streaks", biggest_color_streaks)]:
            df = pd.DataFrame.from_dict(streaks, orient="index", columns=["Streaks"])
            df.index.name = name
            dataframes.append(df)

        return dataframes

    @staticmethod
    def plot_analysis(analysis):
        dataframes = analysis

        numbers_dataframe = dataframes[0]
        color_dataframe = dataframes[1]
        biggest_number_streaks_dataframe = dataframes[2]
        biggest_color_streaks_dataframe = dataframes[3]

        numbers_dataframe.plot.bar(y="Percentage", title="Number Hits")
        color_dataframe.plot.bar(y="Percentage", title="Color Hits", color=["black", "red"])
        biggest_number_streaks_dataframe.plot.bar(y="Streaks", title="Biggest Number Streaks")
        biggest_color_streaks_dataframe.plot.bar(y="Streaks", title="Biggest Color Streaks", color=["black", "red"])
        plt.show()

    def print_analysis(self, analysis):
        dataframes = analysis

        numbers_dataframe = dataframes[0]
        color_dataframe = dataframes[1]
        biggest_number_streaks_dataframe = dataframes[2]
        biggest_color_streaks_dataframe = dataframes[3]

        print(numbers_dataframe)
        print(color_dataframe)
        print(biggest_number_streaks_dataframe)
        print(biggest_color_streaks_dataframe)