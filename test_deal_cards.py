"""Test blackjack.deal_cards"""

import cards
import blackjack


def test_deal_cards():
    deck = []
    for suit in cards.SUITS:
        for rank in cards.RANKS:
            deck.append(cards.Card(suit, rank))
    dealer_hand = []
    player_hand = []

    blackjack.deal_cards(deck, dealer_hand, player_hand)

    assert len(dealer_hand) == 2
    assert len(player_hand) == 2
    assert dealer_hand[0].is_face_up() is True
    assert dealer_hand[1].is_face_up() is False, "Dealer's second card should be face down."
    assert player_hand[0].is_face_up() is True
    assert player_hand[1].is_face_up() is True


def test_deal_cards_alternates_between_player_and_dealer():
    card1 = cards.Card(cards.SPADES, cards.SIX)
    card2 = cards.Card(cards.HEARTS, cards.SEVEN)
    card3 = cards.Card(cards.CLUBS, cards.EIGHT)
    card4 = cards.Card(cards.DIAMONDS, cards.NINE)

    deck = [card4, card3, card2, card1]

    dealer_hand = []
    player_hand = []
    blackjack.deal_cards(deck, dealer_hand, player_hand)

    assert len(dealer_hand) == 2
    assert len(player_hand) == 2
    assert player_hand[0] is card1, 'Player 1st card should be Six of Spades'
    assert player_hand[1] is card3, 'Player 2nd card should be Eight of Clubs'
    assert dealer_hand[0] is card2, 'Dealer 1st card should be Seven of Hearts'
    assert dealer_hand[1] is card4, 'Dealer 2nd card should be Nine of Diamonds'