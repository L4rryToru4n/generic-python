"""
Game logic :
Create two instances of Player class
Create an instance of a deck of cards, shuffled
Split the deck for two player
First part, check if the game still moving. If it doesn't,
 the game should be ended. This check happens every round
The attribute to be checked is the number of cards
 each of the player has. If any of the player doesn't have
 any cards left, that player lose.
Second part, each dealt card from both of the players would
 be compared, if one of the card has more value than the
 other then the player who has that card would take both
 of the cards. However if both of the cards has the same
 value (war) then all player must deal another 3 cards

Game rules :
 - If there is a tie, each player needs to draw 5 additional
   cards
 - A player will lose if they don't have at least 5 cards to
   play the war
"""

import wargame as w

#Game Setup
# name_pone = input("Player 1, enter your name : ")
# name_ptwo = input("Player 2, enter your name : ")

player_one = w.Player("name_pone")
player_two = w.Player("name_ptwo")

new_deck = w.Deck()
new_deck.shuffle()

for i in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0
while game_on:

    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print("player One is out of cards! Player Two wins !")
        game_on = False
        break
    elif len(player_two.all_cards) == 0:
        print("player Two is out of cards! Player One wins !")
        game_on = False
        break

    # START A NEW ROUND

    player_one_cards = []
    player_two_cards = []

    player_one_cards.append(player_one.remove_one())
    print(player_one_cards[-1])
    player_two_cards.append(player_two.remove_one())
    print(player_two_cards[-1])

    at_war = True

    while at_war:

        if player_one_cards[-1].values > player_two_cards[-1].values:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
        elif player_two_cards[-1].values > player_one_cards[-1].values:
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)
            at_war = False
        else:
            print("WAR !")

            if len(player_one.all_cards) < 5:
                print("Player One unable to declare war")
                print("Player Two wins !")
                game_on = False
                break
            elif len(player_two.all_cards) < 5:
                print("Player Two unable to declare war")
                print("Player One wins !")
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

