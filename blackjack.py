import random

# Deck of Cards

deck_of_cards = []

# list of suits

list_of_suits = ["Hearts", "Diamonds", "Spades", "Clubs"]

for suit in list_of_suits:
    for card_value in range(1,12):
        deck_of_cards.append((suit, card_value))

random.shuffle(deck_of_cards)

# Dealer Cards and Player Cards

dcards = []

pcards = []



# Method for Dealing Dealer Cards


while len(dcards) != 2:
    dcards.append(deck_of_cards.pop())
    if len(dcards) == 2:
        print("The Dealer has Blank Card &", dcards[1])

# Method for Dealing Player Cards

while len(pcards) != 2:
    pcards.append(deck_of_cards.pop())
    if len(pcards) == 2:
        print("You have", pcards)

# Sum of Dealer Method

dealer_sum = 0
for dval in dcards:
    dealer_sum += dval[1]



if dealer_sum == 21:
    print("Dealer has 21! ")
elif dealer_sum > 21:
    print("Dealer has busted! ")

         



# Sum of Player Method

player_sum = 0
for pval in pcards:
    player_sum += pval[1]

while player_sum < 21:

    player_move = str(input("What would you like to do? 'H' for HIT, 'S' for STAND: ")).lower()

    if player_move == 'h':
        pcards.append(deck_of_cards.pop())
        player_sum += pcards[-1][1]
        print("You now have " + str(player_sum) + " from the cards below: " + str(pcards))
        if player_sum > 21:
            print("You busted!")
        
        elif player_sum == 21:
            break

    
    elif player_move == 's':
        # dealer will add cards to the sum of 16
        # sum of dcard add card from deck >= 16
        while dealer_sum <= 16:
            dcards.append(deck_of_cards.pop())
            dealer_sum += dcards[-1][1]

        # When the Dealer Wins

        print("Here are the Dealers cards: " + str(dcards))
        print("Dealer has " + str(dealer_sum))

        if dealer_sum < 22 and dealer_sum > player_sum:
            print("Here is the result:  The Dealer has won!")

        # /////// When the Player Wins ////////

        print("Here are your cards: " + str(pcards))
        print("You have " + str(player_sum))

        if player_sum < 22 and player_sum > dealer_sum:
            print("Here is the result:  You have won!")

        # ////// When the Player & the Dealer Tie ///////

        if player_sum < 22 and player_sum == dealer_sum:
            print("You have " + str(player_sum))
            print("Dealer has " + str(dealer_sum))
            print("Here is the result: You Tied (push)")

        if player_sum == 21:
            print("You have 21!")
        
        if dealer_sum == 21:
            print("Dealer has 21!")
        break


# add a push method & add a results section



