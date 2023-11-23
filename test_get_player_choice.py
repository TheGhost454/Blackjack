"""Test blackjack.get_player_choice"""

import blackjack


def test_get_player_choice_when_hit_lower():
    input_values = ['x', '1', 'h']
    blackjack.input = lambda _: input_values.pop(0)

    assert blackjack.get_player_choice() == 'h'


def test_get_player_choice_when_stand_lower():
    input_values = ['', '9', '#', 's']
    blackjack.input = lambda _: input_values.pop(0)

    assert blackjack.get_player_choice() == 's'


def test_get_player_choice_when_hit_upper():
    input_values = ['x', '1', 'hh', 'H']
    blackjack.input = lambda _: input_values.pop(0)

    assert blackjack.get_player_choice() == 'h'


def test_get_player_choice_when_stand_upper():
    input_values = ['', '9', '#', 'ss', 'S']
    blackjack.input = lambda _: input_values.pop(0)

    assert blackjack.get_player_choice() == 's'
