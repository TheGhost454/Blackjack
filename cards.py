"""Card class"""

_HEARTS_CHR = chr(9829)  # Character 9829 is '♥'.
_DIAMONDS_CHR = chr(9830)  # Character 9830 is '♦'.
_SPADES_CHR = chr(9824)  # Character 9824 is '♠'.
_CLUBS_CHR = chr(9827)  # Character 9827 is '♣'.

SPADES = 'Spades'
HEARTS = 'Hearts'
CLUBS = 'Clubs'
DIAMONDS = 'Diamonds'
SUITS = (SPADES, HEARTS, CLUBS, DIAMONDS)

TWO = ('2', 2)
THREE = ('3', 3)
FOUR = ('4', 4)
FIVE = ('5', 5)
SIX = ('6', 6)
SEVEN = ('7', 7)
EIGHT = ('8', 8)
NINE = ('9', 9)
TEN = ('10', 10)
JACK = ('J', 10)
QUEEN = ('Q', 10)
KING = ('K', 10)
ACE = ('A', 11)
RANKS = (TWO, THREE, FOUR, FIVE, SIX, SEVEN,
         EIGHT, NINE, TEN, JACK, QUEEN, KING, ACE)
FACE_CARDS = (JACK, QUEEN, KING)

_MAX_VALUE = 10
_ACE_MAX_VALUE = 11


class Card:
    """A representation of a playing card"""

    def __init__(self, suit, rank):
        self._suit = suit
        if rank not in RANKS:
            raise Exception('Invalid card rank.')
        self._rank = rank
        if self._suit == HEARTS:
            self._suit_chr = _HEARTS_CHR
        elif self._suit == DIAMONDS:
            self._suit_chr = _DIAMONDS_CHR
        elif self._suit == CLUBS:
            self._suit_chr = _CLUBS_CHR
        else:
            self._suit_chr = _SPADES_CHR
        self._face_up = True

    @property
    def suit(self):
        """The card's suit"""
        return self._suit

    @property
    def name(self):
        """The card's name (e.g. Ace, King,...,2)"""
        return self._rank[0]

    @property
    def value(self):
        """The card's value"""
        return self._rank[1]

    @property
    def suit_chr(self):
        """The character representing the suit"""
        return self._suit_chr

    def is_ace(self):
        """Returns True if this card is an Ace"""
        return self._rank == ACE

    def is_face_card(self):
        """Returns True if this card is a King, Queen or Jack"""
        return self._rank in FACE_CARDS

    def face_down(self):
        self._face_up = False

    def face_up(self):
        self._face_up = True

    def is_face_up(self):
        return self._face_up

    def __repr__(self):
        return '[' + self.name + ' of ' + self.suit + ']'

    def __str__(self):
        return '[' + self.name + ' of ' + self.suit + ']'

    def __eq__(self, other):
        return (self is other) or (self._rank, self._suit) == (other._rank, other._suit)

    def __lt__(self, other):
        return self._rank[1] < other._rank[1]

    def __gt__(self, other):
        return self._rank[1] > other._rank[1]


def display_cards(cards):
    """Display all the cards in the cards list."""
    rows = ['', '', '', '', '']  # The text to display on each row.

    for card in cards:
        rows[0] += ' ___  '  # Print the top line of the card.
        if not card.is_face_up():
            # Print a card's back:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            rows[1] += f'|{card.name:<2} | '
            rows[2] += f'| {card.suit_chr} | '
            rows[3] += f'|_{card.name:_>2}| '

    # Print each row on the screen:
    for row in rows:
        print(row)
