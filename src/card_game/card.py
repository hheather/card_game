from dataclasses import dataclass

from card_game.rank import Rank
from card_game.suit import Suit


@dataclass
class Card:
    suit: Suit
    rank: Rank

    def __str__(self) -> str:
        return f'{self.rank.value} of {self.suit.value}'
