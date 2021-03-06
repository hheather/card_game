from typing import List
import random

from card_game.card import Card


class Deck:
    def __init__(self, cards: List[Card]):
        self.cards = cards

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw(self) -> str:
        human_friendly_cards = [card.card_name() for card in self.cards]
        choices = random.sample(human_friendly_cards, k=2)
        return ', '.join(choices)
