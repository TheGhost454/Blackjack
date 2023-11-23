"""Test blackjack.get_hand_value"""

import cards
import blackjack


def test_get_hand_value_when_two_cards():
    hand = []
    twoClubs = cards.Card(cards.CLUBS, cards.TWO)
    hand.append(twoClubs)
    tenSpades = cards.Card(cards.SPADES, cards.TEN)
    hand.append(tenSpades)

    assert blackjack.get_hand_value(hand) == 12


def test_get_hand_value_when_ace_does_not_bust():
    hand = []
    hand.append(cards.Card(cards.DIAMONDS, cards.TWO))
    hand.append(cards.Card(cards.SPADES, cards.ACE))

    assert blackjack.get_hand_value(hand) == 13


def test_get_hand_value_when_ace_would_bust():
    hand = []
    hand.append(cards.Card(cards.SPADES, cards.THREE))
    hand.append(cards.Card(cards.DIAMONDS, cards.ACE))
    hand.append(cards.Card(cards.SPADES, cards.JACK))

    assert blackjack.get_hand_value(hand) == 14


def test_get_hand_value_when_four_aces_would_bust():
    hand = []
    hand.append(cards.Card(cards.SPADES, cards.ACE))
    hand.append(cards.Card(cards.DIAMONDS, cards.ACE))
    hand.append(cards.Card(cards.HEARTS, cards.ACE))
    hand.append(cards.Card(cards.HEARTS, cards.TWO))
    hand.append(cards.Card(cards.SPADES, cards.JACK))
    hand.append(cards.Card(cards.CLUBS, cards.ACE))

    assert blackjack.get_hand_value(hand) == 16


def test_get_hand_value_when_ace_jack():
    hand = []
    hand.append(cards.Card(cards.DIAMONDS, cards.ACE))
    hand.append(cards.Card(cards.SPADES, cards.JACK))

    assert blackjack.get_hand_value(hand) == 21


def test_get_hand_value_when_ace_ten():
    hand = []
    hand.append(cards.Card(cards.DIAMONDS, cards.ACE))
    hand.append(cards.Card(cards.SPADES, cards.TEN))

    assert blackjack.get_hand_value(hand) == 21


def test_get_hand_value_that_busted():
    hand = []
    hand.append(cards.Card(cards.DIAMONDS, cards.EIGHT))
    hand.append(cards.Card(cards.SPADES, cards.THREE))
    hand.append(cards.Card(cards.SPADES, cards.NINE))
    hand.append(cards.Card(cards.SPADES, cards.TWO))
    assert blackjack.get_hand_value(hand) == 22


def test_get_hand_value_when_one_ace_causes_bust():
    hand = []
    hand.append(cards.Card(cards.DIAMONDS, cards.TWO))
    hand.append(cards.Card(cards.SPADES, cards.ACE))
    hand.append(cards.Card(cards.HEARTS, cards.ACE))
    assert blackjack.get_hand_value(hand) == 14
