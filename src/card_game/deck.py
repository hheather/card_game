from typing import List
import random

from card_game.card import Card


class Deck:
    def __init__(self, cards: List[Card]):
        self.cards = cards

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw(self) -> str:
        human_friendly_cards = [card.__str__() for card in self.cards]
        choices = random.choices(human_friendly_cards, k=2)
        return ', '.join(choices)
