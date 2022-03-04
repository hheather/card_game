from card_game.card import Card
import pytest
from card_game.suit import Suit
from card_game.rank import Rank


class TestCard:

    @pytest.fixture
    def under_test(self):
        return Card(suit=Suit.HEARTS, rank=Rank.QUEEN)

    def test_card(self, under_test):
        assert under_test.rank.value == "Queen"
        assert under_test.suit.value == "Hearts"
