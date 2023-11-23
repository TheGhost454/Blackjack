"""Test cards.py module"""
import pytest

from cards import Card, CLUBS, SPADES, HEARTS, DIAMONDS
from cards import TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN
from cards import ACE, KING, QUEEN, JACK


def test_create_card():
    card = Card(CLUBS, SEVEN)
    assert card.value == 7
    assert card.suit == CLUBS
    assert card.name == '7'


@pytest.mark.parametrize("card, suit, value, name",
                         [(Card(HEARTS, KING), HEARTS, 10, 'K'),
                          (Card(DIAMONDS, QUEEN), DIAMONDS, 10, 'Q'),
                          (Card(SPADES, JACK), SPADES, 10, 'J'),
                          (Card(CLUBS, TEN), CLUBS, 10, '10'),
                          (Card(HEARTS, NINE), HEARTS, 9, '9'),
                          (Card(DIAMONDS, EIGHT), DIAMONDS, 8, '8'),
                          (Card(SPADES, SEVEN), SPADES, 7, '7'),
                          (Card(CLUBS, SIX), CLUBS, 6, '6'),
                          (Card(HEARTS, FIVE), HEARTS, 5, '5'),
                          (Card(DIAMONDS, FOUR), DIAMONDS, 4, '4'),
                          (Card(SPADES, THREE), SPADES, 3, '3'),
                          (Card(CLUBS, TWO), CLUBS, 2, '2'),
                          (Card(HEARTS, ACE), HEARTS, 11, 'A')])
def test_create_cards(card, suit, value, name):
    assert card.suit == suit
    assert card.value == value
    assert card.name == name


def test_compare_when_equal_to_other():
    card1 = Card(SPADES, SEVEN)
    card2 = Card(SPADES, SEVEN)

    assert card1 == card2


def test_compare_cards_when_card_greater_than_other():
    card = Card(DIAMONDS, SEVEN)
    other = Card(HEARTS, TWO)

    assert (card > other) is True


def test_compare_when_card_less_than_other():
    card = Card(DIAMONDS, FOUR)
    other = Card(CLUBS, EIGHT)

    assert (card < other) is True


def test_compare_when_ACE_greater_than_KING():
    ace = Card(HEARTS, ACE)
    king = Card(CLUBS, KING)

    assert (ace > king) is True


def test_is_ace_when_ACE():
    assert Card(HEARTS, ACE).is_ace() is True


def test_is_ace_when_not_ACE():
    assert Card(HEARTS, KING).is_ace() is False


def test_face_up_is_True_when_card_created():
    card = Card(HEARTS, KING)
    assert card.is_face_up() is True


def test_face_down():
    card = Card(HEARTS, KING)
    card.face_up()

    assert card.is_face_up() is True


def test_is_face_up():
    card = Card(HEARTS, KING)
    card.face_up()
    card.face_down()

    assert card.is_face_up() is False


def test_is_face_up_when_face_up_called_twice():
    card = Card(HEARTS, KING)
    card.face_down()
    card.face_up()
    card.face_up()

    assert card.is_face_up() is True


def test_is_face_up_when_face_down_called_twice():
    card = Card(HEARTS, KING)
    card.face_down()
    card.face_down()

    assert card.is_face_up() is False


@pytest.mark.parametrize("card, expected",
                         [(Card(HEARTS, KING), True),
                          (Card(HEARTS, QUEEN), True),
                          (Card(HEARTS, JACK), True),
                          (Card(HEARTS, ACE), False),
                          (Card(HEARTS, TEN), False)])
def test_card_is_face_card(card, expected):
    assert card.is_face_card() is expected
