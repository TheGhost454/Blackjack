"""Test blackjack.create_card_deck"""

import cards
import blackjack


def test_create_deck_has_52_cards():
    # Arrange
    expected_deck = []
    for suit in cards.SUITS:
        for rank in cards.RANKS:
            expected_deck.append(cards.Card(suit, rank))
    expected_deck.sort()

    deck = blackjack.create_card_deck()
    deck.sort()

    assert deck == expected_deck
