from card_game.card import Card
from card_game.deck import Deck
from card_game.suit import Suit
from card_game.rank import Rank


if __name__ == "__main__":
    cards = [Card(suit, rank) for suit in Suit for rank in Rank]
    deck = Deck(cards)
    deck.shuffle()
    result = deck.draw()
    print(result)
