from dataclasses import dataclass
from typing import Union


@dataclass
class Card:
    suit: str
    rank: Union[str, int]

    def __str__(self):
        return f'{self.rank} of {self.suit}'
