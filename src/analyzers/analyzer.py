from abc import ABC, abstractmethod


class Analyzer(ABC):

    @abstractmethod
    def get_analysis(self):
        pass

    @abstractmethod
    def plot_analysis(self, analysis):
        pass

    @abstractmethod
    def print_analysis(self, analysis):
        pass
