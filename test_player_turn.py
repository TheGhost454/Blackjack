"""Test blackjack.player_turn"""

import cards
import blackjack


def test_player_turn_when_has_blackjack():
    player_hand = [cards.Card(cards.DIAMONDS, cards.ACE),
                   cards.Card(cards.CLUBS, cards.JACK)]
    assert blackjack.player_turn(player_hand, deck=[]) == 21


def test_player_turn_when_busts():
    input_values = ['h']
    blackjack.input = lambda _: input_values.pop(0)
    player_hand = [cards.Card(cards.DIAMONDS, cards.TEN),
                   cards.Card(cards.CLUBS, cards.JACK)]
    assert blackjack.player_turn(
        player_hand, deck=[cards.Card(cards.SPADES, cards.TWO)]) == 22


def test_player_turn_when_stands():
    input_values = ['h', 'h', 's']
    blackjack.input = lambda _: input_values.pop(0)
    player_hand = [cards.Card(cards.DIAMONDS, cards.THREE),
                   cards.Card(cards.CLUBS, cards.QUEEN)]
    deck = [cards.Card(cards.SPADES, cards.TWO),
            cards.Card(cards.HEARTS, cards.TWO),
            cards.Card(cards.HEARTS, cards.FOUR)]
    assert blackjack.player_turn(player_hand, deck) == 19
