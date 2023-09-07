import random
import click

suits = ["hearts", "diamonds", "clubs", "spades"]
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
cards_values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "jack":10, "queen":10, "king":10, "ace": 11}

# Generate the deck (52 cards) :[('2', 'hearts'), ('3', 'hearts'), ('4', 'hearts')...]
deck = []
for suit in suits:
    for card in cards:
        deck.append((card, suit))

# Dealing cards : ('3', 'diamonds')
def deal_card():

    selected_card = random.choice(deck)
    return selected_card

# calculate the score to determine winner.. sum of dictionary keys??

def calculate_score(cards):
    if sum([cards_values[cards[i][0]] for i in range(len(cards))]) == 21 and len(cards) == 2:
        return 0
    # If ace is selected and sum is over 21, replace 11 with 1
    if 11 in cards and sum([cards_values[cards[i][0]] for i in range(len(cards))]) > 21:
        cards.remove(11)
        cards.append(1)
    return sum([cards_values[cards[i][0]] for i in range(len(cards))])

# check for winner

def check_winner(user_score, dealer_score):
    if user_score == 0:
        print("You win, you got blackjack")

    if dealer_score == 0:
        print("You lose, dealer got blackjack")

    elif 16 < user_score < 21 and 16 < dealer_score < 21 and user_score == dealer_score:
        print("Push")

    elif user_score > 21:
        print("You lose, it went over 21")

    elif dealer_score > 21:
        print("You win, Dealer went over 21")

    elif user_score > dealer_score:
        print("You win")

    elif dealer_score > user_score:
        print("You lose")


# game play

def play_game():

    #Deal the user and dealer 2 cards each using deal_card()

    is_game_over = False
    print("Dealing card...")
    user_cards = []
    dealer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not is_game_over:

        # calculate the score. If either one has blackjack or over 21, the game ends

        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"   Your cards: {user_cards}, current score: {user_score}") 
        print(f"   Dealer's card: {dealer_cards}, current score: {dealer_score}")

        if user_score == 0 or dealer_score == 0 or user_score > 20:
            break
        else:
            while user_score < 21:
                user_choice = input("Hit or Stand? ")
                if user_choice == "Hit":
                    user_cards.append(deal_card())
                    user_score = calculate_score(user_cards)
                    print(f"   Your cards: {user_cards}, Your score: {user_score}")
                    if user_score > 20:
                        is_game_over = True
                        return check_winner(user_score, dealer_score)
                else:
                    is_game_over = True
                    break


    # Dealer should keep drawing cards until the score hit 17 or more.

    while dealer_score < 17 and user_score < 22 and (user_score != 21 or dealer_score !=21):
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)
        print(f"   Your cards: {user_cards}, Your score: {user_score}") 
        print(f"   Dealer's cards: {dealer_cards}, Dealer's score: {dealer_score}")
        if dealer_score > 16:
            return check_winner(user_score, dealer_score)

    is_game_over = True
    check_winner(user_score, dealer_score)
        
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    click.clear()
    play_game()

