import cards
import random

my_card = cards.Card(cards.CLUBS, cards.TWO)

print(my_card)
print(my_card.is_face_up())

my_card.face_down()
print(my_card.is_face_up())
print(my_card.value)
hand = [my_card]
print(hand)
hand.append(cards.Card(cards.HEARTS, cards.ACE))
hand[0].face_up()
print(hand)
cards.display_cards(hand)
hand.append(cards.Card(cards.SPADES, cards.FIVE))
cards.display_cards(hand)
my_card.face_up()
cards.display_cards(hand)
hand.append(cards.Card(cards.DIAMONDS, cards.FOUR))
hand.append(cards.Card(cards.DIAMONDS, cards.JACK))
cards.display_cards(hand)
hand_value = 0
for card in hand:
    hand_value += card.value
print(hand_value)

deck = []
for suit in cards.SUITS:
    for rank in cards.RANKS:
        deck.append(cards.Card(suit, rank))
cards.display_cards(deck)

deck_value = 0
for card in deck:
    deck_value += card.value
print(deck_value)

random.shuffle(deck)
cards.display_cards(deck)

player_hand = []
dealer_hand = []
card = deck.pop()

player_hand.append(card)
dealer_hand.append(deck.pop())
cards.display_cards(player_hand)
cards.display_cards(dealer_hand)
player_hand.append(deck.pop())
dealer_hand.append(deck.pop())
cards.display_cards(player_hand)
cards.display_cards(dealer_hand)
dealer_hand[1].face_down()
cards.display_cards(dealer_hand)

card = cards.Card(cards.CLUBS, cards.ACE)
if card.is_ace():
    print("It's an Ace")
