from card_game.card import Card
import pytest

from card_game.deck import Deck
from card_game.suit import Suit
from card_game.rank import Rank


class TestDeck:

    @pytest.fixture
    def under_test(self):
        cards = [Card(Suit.HEARTS, Rank.QUEEN),
                 Card(Suit.HEARTS, Rank.KING)]
        return Deck(cards)

    def test_shuffle(self, under_test):
        under_test.shuffle()
        assert len(under_test.cards) == 2

    def test_draw(self, under_test):
        result = under_test.draw()
        assert 'Queen of Hearts' in result
        assert 'King of Hearts' in result
