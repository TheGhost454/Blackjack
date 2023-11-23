"""
Blackjack (a.k.a. 21)
The player attempts to beat the dealer by getting a
hand value as close to 21 as possible, without going over 21.

<Preston Rizzo>
"""
import random
import time
import cards

# Constants to identify winner of hand
TIE = 0
DEALER = 1
PLAYER = 2

# Dealer stands at 17
DEALER_MAX = 17

# The game max value for a hand
MAX = 21

# Player enters one of these two values when prompted.
HIT = 'h'
STAND = 's'


class BlackjackException(Exception):
    """Raise this exception when appropriate"""


def create_card_deck():
    """
    Creates a standard deck of cards.
    Each of the 4 suits has 13 cards.
    Use nested FOR loops to create the cards using cards.SUITS and cards.RANKS.
    (see cards.py)

    :return: a standard deck of 52 cards
    :rtype: list
    """
    # Use nested FOR loops to create the cards
    # using cards.SUITS and cards.RANKS. The SUITS
    # and RANKS constants are lists of the card suits
    # and ranks. For example, this creates one card:
    # cards.Card(cards.SUITS[0], cards.RANKS[0])
    # (see cards.py)
    card_deck = []
    for suit in cards.SUITS:
        for rank in cards.RANKS:
            card_deck.append(cards.Card(suit, rank))

    return card_deck


def get_hand_value(hand):
    """
    Computes the value of a hand using ``card.value``.
    If an Ace (worth 11 by default) is present and the total hand value
    exceeds the MAX, then count the Ace as 1 instead of 11.

    :param hand: the cards that are held by the player or dealer
    :type hand: list
    :return: the value of the hand
    :rtype: int
    """

    value = 0
    aces = []
    for card in hand:
        value += card.value
    if value > MAX:
        for card in hand:
            if card.is_ace():
                value -= 10
                if value < MAX:
                    break
    return value
    # If the value of the hand exceeds the MAX and
    # the player holds an Ace, count the Ace as a
    # value of 1 instead of 11.
    # Use a loop that subtracts 10 from the hand value for every
    # Ace held by the user until there are no more Aces or the hand value
    # is less than or equal to MAX.


def get_player_choice():
    """
    :return: the player's decision to hit or stand.
    :rtype: str
    """
    # accepted are HIT and STAND. Use the named constants.
    choice = ""
    while choice == "":
        choice = input("Do you want to hit or stand? (Type h or s): ")
        if choice.lower() == HIT:
            return HIT
        elif choice.lower() == STAND:
            return STAND
        else:
            choice = ""


def deal_cards(deck: list, dealer_hand: list, player_hand: list):
    """
    Each player is dealt two cards. Player gets the first card.
    Alternate dealing between player and dealer until each has two cards.
    The dealers second card needs to be dealt face down.

    :param deck: the deck of cards to deal from
    :param dealer_hand: an empty list representing the dealer's hand
    :param player_hand: an empty list representing the player's hand
    :rtype: None
    """
    # and put in the player_hand list. Then, take a card from the deck and
    # put it in the dealer_hand list. Do that one more time in that order
    # so that the dealer and player have each two cards.
    # Make sure the dealers second card is face down. Call
    # card.face_down() to put the card face down.
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    dealer_hand[1].face_down()


def dealer_turn(dealer_hand, deck, player_hand_value, delay=1):
    """
    Dealer receives cards if player has not busted.
    Dealer must stand at 17. Dealer must draw cards at 16 and under.
    Display the value of the hand display all the dealer's cards on
    after each card is dealt.

    :param dealer_hand: the cards held by the dealer
    :type dealer_hand: list
    :param deck: the deck of cards to deal from
    :type deck: list
    :param player_hand_value: the value of the player's hand
    :type player_hand_value: int
    :param delay: a delay for visual affect
    :type delay: int
    :return: the value of the dealer's hand
    :rtype: int
    """

    # call to get_hand_value function instead of assigning 0.
    hand_value = get_hand_value(dealer_hand)

    print('Dealer:', hand_value)

    time.sleep(delay)

    # The dealer should only take a card from the deck if the player's hand
    # value is <= MAX and the dealer's hand value < DEALER_MAX.
    # HINT: This code should be implemented in a while loop that executes
    # until the described compound expression is False. The dealer should
    # receive a card from the deck on each iteration of the loop.
    dealer_hand[1].face_up()
    cards.display_cards(dealer_hand)

    while player_hand_value <= MAX and hand_value < DEALER_MAX:
        dealer_hand.append(deck.pop())
        hand_value = get_hand_value(dealer_hand)
        print('Dealer:', hand_value)
        cards.display_cards(dealer_hand)
        if hand_value > MAX:
            print("BUSTED!")
            break
    return hand_value


def player_turn(player_hand, deck):
    """
    Allow the player to draw a card (hit or stand).
    Return the value of the player's hand.

    :param player_hand: the cards held by the player
    :type player_hand: list
    :param deck: the deck of cards to deal from
    :type deck: list
    :return: the value of the players hand
    :rtype: int
    """
    hand_value = get_hand_value(player_hand)
    print('Player:', hand_value)
    cards.display_cards(player_hand)
    choice = None
    if hand_value < MAX:
        choice = get_player_choice()

    while choice == HIT:
        player_hand.append(deck.pop())
        hand_value = get_hand_value(player_hand)
        cards.display_cards(player_hand)
        if hand_value <= MAX:
            print('Player:', hand_value)
            choice = get_player_choice()
        else:
            print('Player:', hand_value)
            print("BUSTED!")
            break
        # The player should get a card and their hand_value needs to be recalculated.
        # If their hand_value is <= MAX, display their hand value and ask to HIT or STAND
        # Otherwise, display the hand value and the word 'BUSTED!'
    return hand_value


def determine_winner(dealer_hand_value, player_hand_value):
    """
    Returns the winner of the round based on hand value

    :param dealer_hand_value: dealer's hand value
    :type dealer_hand_value: int
    :param player_hand_value: player's hand value
    :type player_hand_value: int
    :return: either TIE, DEALER or PLAYER
    :rtype: int
    """
    winner = TIE
    if dealer_hand_value > MAX and player_hand_value > MAX:
        raise BlackjackException
    elif player_hand_value <= MAX and dealer_hand_value < player_hand_value:
        winner = PLAYER
    elif dealer_hand_value > MAX and player_hand_value <= MAX:
        winner = PLAYER
    elif dealer_hand_value <= MAX and player_hand_value < dealer_hand_value:
        winner = DEALER
    elif player_hand_value > MAX and dealer_hand_value <= MAX:
        winner = DEALER
    return winner


def main():
    """ Controls the process of playing Blackjack """
    deck = create_card_deck()

    random.shuffle(deck)

    play_again = 'y'
    while play_again == 'y':
        # This list holds the cards that will be dealt to the dealer
        dealer_hand = []
        # This list holds the cards that will be dealt to the player
        player_hand = []
        try:
            # to the dealer and player
            deal_cards(deck, dealer_hand, player_hand)

            print('Dealer: ??')
            cards.display_cards(dealer_hand)

            player_turn(player_hand, deck)

            player_hand_value = get_hand_value(player_hand)

            dealer_turn(dealer_hand, deck, player_hand_value, delay=1)

            dealer_hand_value = get_hand_value(dealer_hand)

            winner = determine_winner(dealer_hand_value, player_hand_value)

            if winner == DEALER:
                print("Dealer wins!")
            elif winner == PLAYER:
                print("Player wins!")
            else:
                print("Tie!")
            play_again = input('\nPlay again (y/n)? ')
            print()
        except IndexError:
            print('Deck is empty. Starting over!\n')
            input('Press any key to continue...')
            deck = create_card_deck()
            random.shuffle(deck)


if __name__ == '__main__':
    main()
