"""Test blackjack.determine_winner"""

import blackjack


def test_determine_winner_when_player_score_higher():
    assert blackjack.determine_winner(
        dealer_hand_value=20, player_hand_value=21) == blackjack.PLAYER


def test_determine_winner_when_dealer_score_higher():
    assert blackjack.determine_winner(
        dealer_hand_value=21, player_hand_value=20) == blackjack.DEALER


def test_determine_winner_when_tie_score():
    assert blackjack.determine_winner(
        dealer_hand_value=19, player_hand_value=19) == blackjack.TIE


def test_determine_winner_when_dealer_busted():
    assert blackjack.determine_winner(
        dealer_hand_value=22, player_hand_value=19) == blackjack.PLAYER


def test_determine_winner_when_player_busted():
    assert blackjack.determine_winner(
        dealer_hand_value=20, player_hand_value=22) == blackjack.DEALER


def test_determine_winner_when_player_dealer_busted():
    try:
        blackjack.determine_winner(
            dealer_hand_value=22, player_hand_value=22) == blackjack.DEALER
        assert False, 'Expected blackjack.BlackjackException'
    except blackjack.BlackjackException:
        assert True
