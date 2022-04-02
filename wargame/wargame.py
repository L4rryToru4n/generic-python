"""
Create a classes of card, deck and player
Card values would be initialized
Global variables are values, suit, rank
"""
import random

suits = {"Heart", "Diamonds", "Spades", "Clubs"}
ranks = {"Two", "Three", "Four", "Five", "Six", "Seven",
         "Eight", "Nine", "Ten", "Jack", "Queen", "King",
         "Ace"}
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5,
          "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9,
          "Ten": 10, "Jack": 11, "Queen": 12, "King": 13,
          "Ace": 14}


class Card:
    """
    Has all the attribute values of a single card
    The attribute values are suit, rank and card value
    """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.values = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    """
    Instantiate a new deck
     - Create all Card objects
     - Hold them as a list of Card objects
    Shuffle a Deck through a method call
     - Random library shuffle() func
    Deal cards from the Deck object
     - Pop method from cards list
    Deck Class
     - We will see that the Deck class holds a list of Card objects
     - This means deck class will return Card class object instances,
        not just normal python data types.
    """

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create the Card Object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        try:
            return self.all_cards.pop()
        except IndexError:
            print("No more cards in the deck")


class Player:
    """
    Hold a player's current list of cards
    A player should be able to add or remove cards from their "hand"
    (list of Card objects).
     - We will want the player to be able to add as single card or multiple
       cards to their list, so we will also explore how to do this in one
       method call.
     - The last thing we need to think about is translating a Deck or a
       hand of cards with a top and bottom, to a Python list.
    """

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            return self.all_cards.extend(new_cards)
        else:
            return self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."
