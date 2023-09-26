# PyRoulette
---
PyRoulette is a program you can use to simulate roulette game to calculate probabilities and analyze strategies.

```python
from src.strategies import Martingale
from src.analyzers import PlayerAnalyzer
from src.player import Player
from src.auto_roulette import AutoRoulette
from src.player import OutOfMoneyException


initial_balance = 100

strategy = Martingale(1)
player = Player("Player", strategy, initial_balance)
roulette = AutoRoulette([player])

try:
    roulette.play_n_times(100)
except OutOfMoneyException:
    print("Out of money... Game stopped.")

player_analyzer = PlayerAnalyzer(player)
player_analyzer.plot_analysis(player_analyzer.get_analysis())
```

Find more on Medium: [How to Play Smart Roulette using Python](https://medium.com/@estebanthi/how-to-play-smart-roulette-using-python-1a94b4609b32)
