"""
Create classes
Create global variables
"""
import random
import random as rand

values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5,
              "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
              "Jack": 10, "Queen": 10, "King": 10, "Ace": (11)}

suits = {"Heart", "Diamonds", "Spades", "Clubs"}

ranks = {"Two", "Three", "Four", "Five",
         "Six", "Seven", "Eight", "Nine", "Ten",
         "Jack", "Queen", "King", "Ace"}


class Card:

    """
    A Card class has attributes of suit, rank and status
    Suit would be the suit of the card, rank would be the
    rank of the card and status would be the status of card
    being revealed or not.
    """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.values = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

    def getValue(self):
        return self.values


class Deck:

    """
    A class of Deck has many objects of card (essentially
    a deck of cards). There are a total of 52 cards (obj)
    and would be shuffled.
    """

    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffleCards(self):
        random.shuffle(self.deck)

    def dealCard(self):
        if len(self.deck) >= 0:
            try:
                dealt = self.deck.pop(0)
            except IndexError:
                return "No more objects to be popped"
            return dealt
        else:
            print("No more cards in the deck")


class Player:

    def __init__(self, name, bank, value):
        self.name = name
        self.bank = bank
        self.value = value
        self.hand = []

    def addRevealedCard(self, new_card):
        self.hand.append(new_card)

    def getCards(self):
        return self.hand

    def __str__(self):
        return f"\n{self.name}" \
               f"\n{self.bank} credits"

# Not using this class because some of the functions
# are already incorporated in another function
# class Hand:
#
#     def __init__(self):
#         self.cards = []
#         self.value = 0
#         self.aces = 0
#
#     def add_card(self,card):
#         self.cards.append(card)
#         self.value += values[card.rank]
#         if card.rank == 'Ace':
#             self.aces += 1
#
#     def adjust_for_ace(self):
#         while self.value > 21 and self.aces:
#             self.value -= 10
#             self.aces -= 1


class Chips:

    def __init__(self, total):
        self.total = total
        self.bet = 0

    def win_bent(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

