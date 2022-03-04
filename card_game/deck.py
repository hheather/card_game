from typing import List
from card_game.card import Card


class Deck:
    def __init__(self, cards: List[Card]):
        self.cards = cards

    def shuffle(self):
        """
        Performs shuffle on cards list
        :return: None
        """
        raise NotImplementedError

    def draw(self):
        """
        Randomly choose 2 cards and return as str
        :return: str
        """