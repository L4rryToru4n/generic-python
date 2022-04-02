import blackjack as bj
import os
import time


def initializeDeck():
    deck_cards = bj.Deck()
    deck_cards.shuffleCards()
    return deck_cards


def initializePlayer(player_name, player_credits, player_value):
    return bj.Player(player_name, player_credits, player_value)


def printInfo(player):
    print("----------------")
    for card in player.getCards():
        print(card)


def addHands(deck_cards):
    return deck_cards.dealCard()


def addValue(player):
    for card in player.getCards():
        player.value += card.getValue()


def addHidden(cards_list, deck_cards):
    return cards_list.append(deck_cards.dealCard())


def player_hit(player,deck_cards):
    card = addHands(deck_cards)
    player.addRevealedCard(card)
    addValue(player)
    swapAce(player)


def swapAce(player):

    # Swap the Ace value if player's
    # hand value is more than 21
    ace_status = 0
    listCards = player.getCards()
    for card in listCards:
        if card.rank == "Ace" and player.value > 21:
            ace_status = 1
            player.value -= 10
        else:
            pass


def take_bet(total, bet):
    return total-bet


def give_bet(total, bet):
    return total+bet


def emptyHand(player):
    for i in range(len(player.hand)):
        player.hand.pop(0)


def play():
    game = True
    play_game = True
    sub_menu = 1
    dealer_cards = []

    deck_cards = initializeDeck()

    print("You'll be playing against a dealer only")
    name = input("Enter your name                : ")

    while True:
        try:
            credit = int(input("Enter your total credits       : "))
        except TypeError:
            print("Please enter an integer")
        else:
            break

    while play_game:
        while True:
            try:
                bet = int(input("How much you're going to bet ? : "))
            except TypeError:
                print("Please enter an integer")
            else:
                if bet > credit:
                    print(f"Sorry, you don't have enough chips ! You have : {credit}")
                else:
                    break

        player = initializePlayer(name, credit, 0)
        dealer = initializePlayer("Dealer", credit, 0)

        player.addRevealedCard(addHands(deck_cards))
        dealer.addRevealedCard(addHands(deck_cards))
        player.addRevealedCard(addHands(deck_cards))

        addHidden(dealer_cards, deck_cards)

        addValue(player)
        addValue(dealer)

        while game and credit > 0:

            # TODO - print all information of the beginning of a game
            os.system('cls')
            print(player.__str__())
            printInfo(player)
            print(f"Player's value : {player.value}")

            print(dealer.__str__())
            printInfo(dealer)
            print("[Hidden Card]")
            print(f"Dealer's value : {dealer.value}")

            # TODO - Game logic
            # First step, we will decide if the player hit or stay
            # then, calculate all the player's cards value.
            # If it's a bust then the game ends, otherwise continue

            print("\nPlayer's turn")
            print("[1] Hit")
            print("[2] Stay")
            print("[0] Exit to main menu")
            sub_menu = int(input("Enter your input : "))

            if sub_menu == 1:
                os.system('cls')
                print("Player choose to hit\n")
                player.value = 0
                player_hit(player, deck_cards)
                print(player.__str__())
                print("Player's card : ")
                printInfo(player)
                print(f"Player's value : {player.value}")
                if player.value > 21:
                    print("\n> Player Busts <")
                    temp_total = take_bet(credit, bet)
                    credit = temp_total
                    game = False
                else:
                    pass
            elif sub_menu == 2:
                os.system('cls')
                print("Player choose to stay\n")
                print(player.__str__())
                print("Player's card : ")
                printInfo(player)
                print(f"Player's value : {player.value}")
            elif sub_menu == 0:
                break

            print("\nDealer's turn")
            if len(dealer_cards) > 0:
                print("Revealing card..")
                card = dealer_cards.pop(0)
                dealer.addRevealedCard(card)
                dealer.value = 0
                time.sleep(2)
                print(dealer.__str__())
                print("Dealer's card : ")
                printInfo(dealer)
                addValue(dealer)

                # Swap the ace value
                swapAce(dealer)

                print(f"Dealer's value {dealer.value}")

                if dealer.value > 21:
                    print("\n> Dealer Busts <")
                    temp_total = give_bet(credit, bet)
                    credit = temp_total
                    game = False
                elif dealer.value < 18:
                    dealer_cards.append(addHands(deck_cards))
                    game = True
            else:
                card = deck_cards.dealCard()
                dealer.addRevealedCard(card)
                dealer.value = 0
                addValue(dealer)

                # Swap the ace value
                swapAce(dealer)

                print("Dealer's card : ")
                printInfo(dealer)
                print(f"Dealer's value : {dealer.value}")
                if dealer.value > 21:
                    print("\n> Dealer Busts < ")
                    temp_total = give_bet(credit, bet)
                    credit = temp_total
                    game = False
                elif dealer.value < 18:
                    dealer_cards.append(addHands(deck_cards))
                    game = True

            if (17 < dealer.value < 22) and player.value < 22:
                if player.value > dealer.value:
                    print("\n> Player Wins <")
                    temp_total = give_bet(credit, bet)
                    credit = temp_total
                    game = False
                elif player.value < dealer.value:
                    print("\n> Dealer wins <")
                    temp_total = take_bet(credit, bet)
                    credit = temp_total
                    game = False

        emptyHand(player)
        emptyHand(dealer)
        play_menu = input("Wanna continue playing [Y/N] ? : ")
        if play_menu.lower() == "y":
            play_game = True
            game = True
            player.value = 0
            dealer.value = 0
        else:
            play_game = False


def main():
    menu = "1"

    while menu != "0":
        os.system('cls')
        print("WELCOME TO Larry's BlackJack")
        print("[1] Play")
        print("[0] Exit")
        menu = str(input("Input Choice : ")).strip()

        if menu == "1":
            play()
            time.sleep(4)
            print("Returning to main menu in ... 3")
            time.sleep(1)
            print("Returning to main menu in ... 2")
            time.sleep(1)
            print("Returning to main menu in ... 1")
            time.sleep(1)
        else:
            print("Have a nice day :)")


main()
