from enum import Enum, unique


@unique
class Suit(Enum):
    HEARTS = 'Hearts'
    SPADES = 'Spades'
    DIAMONDS = 'Diamonds'
    CLUBS = 'Clubs'
