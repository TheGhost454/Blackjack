"""Test blackjack.dealer_turn"""

import cards
import blackjack


def test_dealer_turn_when_hand_value_is_seventeen():
    dealer_hand = [cards.Card(cards.DIAMONDS, cards.SEVEN),
                   cards.Card(cards.CLUBS, cards.JACK)]
    assert blackjack.dealer_turn(
        dealer_hand, deck=[], player_hand_value=16, delay=0) == 17


def test_dealer_turn_when_hand_value_less_than_seventeen():
    deck = [cards.Card(cards.DIAMONDS, cards.THREE),
            cards.Card(cards.HEARTS, cards.TWO)]
    dealer_hand = [cards.Card(cards.DIAMONDS, cards.SIX),
                   cards.Card(cards.CLUBS, cards.TEN)]
    assert blackjack.dealer_turn(
        dealer_hand, deck, player_hand_value=16, delay=0) == 18


def test_dealer_turn_when_busts_after_two_cards_drawn():
    deck = [cards.Card(cards.DIAMONDS, cards.SIX),
            cards.Card(cards.HEARTS, cards.TWO)]
    dealer_hand = [cards.Card(cards.DIAMONDS, cards.FOUR),
                   cards.Card(cards.CLUBS, cards.QUEEN)]
    assert blackjack.dealer_turn(
        dealer_hand, deck, player_hand_value=16, delay=0) == 22


def test_dealer_turn_first_card_is_turned_face_up():
    dealer_hand = [cards.Card(cards.DIAMONDS, cards.SEVEN),
                   cards.Card(cards.CLUBS, cards.JACK)]
    blackjack.dealer_turn(dealer_hand, deck=[], player_hand_value=16, delay=0)

    assert dealer_hand[0].is_face_up() == True

def test_dealer_turn_when_hand_value_less_than_seventeen_and_then_busts():
    deck = [cards.Card(cards.HEARTS, cards.TEN)]
    dealer_hand = [cards.Card(cards.DIAMONDS, cards.SIX),
                   cards.Card(cards.CLUBS, cards.TEN)]
    assert blackjack.dealer_turn(
        dealer_hand, deck, player_hand_value=16, delay=0) == 26
