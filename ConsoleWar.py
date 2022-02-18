import random
#This is the protoype of the war game to run on console. - JS

# Below, I started the deck. I figured the best way to program it would be a list of tuples, with the key being the card designation
# and the value being the value of the card (1-13 per suit) - JS

officialDeck = [
    # Hearts
    ('A-H', 1), ('2-H', 2), ('3-H', 3), ('4-H', 4), ('5-H', 5), ('6-H', 6), ('7-H', 7), ('8-H', 8), ('9-H', 9), ('10-H', 10), ('J-H', 11), 
    ('Q-H', 12), ('K-H', 13),
    # Spades
    ('A-S', 1), ('2-S', 2), ('3-S', 3), ('4-S', 4), ('5-S', 5), ('6-S', 6), ('7-S', 7), ('8-S', 8), ('9-S', 9), ('10-S', 10), ('J-S', 11), 
    ('Q-S', 12), ('K-S', 13),
    # Diamonds
    ('A-D', 1), ('2-D', 2), ('3-D', 3), ('4-D', 4), ('5-D', 5), ('6-D', 6), ('7-D', 7), ('8-D', 8), ('9-D', 9), ('10-D', 10), ('J-D', 11), 
    ('Q-D', 12), ('K-D', 13),
    # Clubs
    ('A-C', 1), ('2-C', 2), ('3-C', 3), ('4-C', 4), ('5-C', 5), ('6-C', 6), ('7-C', 7), ('8-C', 8), ('9-C', 9), ('10-C', 10), ('J-C', 11), 
    ('Q-C', 12), ('K-C', 13)
]


# Part 1 - Shuffle
# Below is the function to shuffle the deck, and then cut the deck and deal to each player

def shuffle(deck):
    funcDeck = [] # empty deck that will be used to rebuild the official deck
    for i in deck:
        funcDeck.append(i) # this rebuilds the offical deck. 
    shuffledDeck = [] # empty deck that will be filled through this funciton
    while len(funcDeck) != 0: # While cards are still in the original deck
        cardsRemaining = len(funcDeck) # Number of cards still in the original deck
        chosenCard = random.randint(0, cardsRemaining - 1) # Choose a random card in original deck
        shuffledDeck.append(funcDeck.pop(chosenCard)) #puts the chosen card in the shuffled deck
    return shuffledDeck

# Part 2 - Split
# The below funciton cuts the shuffled deck in half and splits the cards

def splitDeck(shuffledDeck): #This splits the shuffled deck in 2 and returns 2 decks for 2 players
    half = len(shuffledDeck)//2
    return shuffledDeck[:half], shuffledDeck[half:]


# Part 3 - Playing the game
# Below are the 2 core functions of playing the game: compareFun and playGame

#The compare function is a function that compares the two current cards in play and determines a winner.
#If the cards are a draw, the function draws 4 more cards and runs recursively on the 4th card drawn

def compareFun(p1Card, p2Card, currentPot, p1Deck, p2Deck):
    if p1Card[1] > p2Card[1]: #if player one has the bigger card, he gets the pot
        winner = "p1"
        return winner, currentPot
    elif p1Card[1] < p2Card[1]: #if player two has the bigger card, he gets the pot
        winner = "p2"
        return winner, currentPot
    elif p1Card[1] == p2Card[1]: # If the cards have the samve value, draw 4 more cards and the 4th card drawn will be checked
            if len(p1Deck) >= 5 and len(p2Deck) >= 5: # Makes sure the players have at least 5 cards to draw
                for i in range(0, 3):  #Draws 3 cards and puts them into the pot
                    currentPot.append(p1Deck.pop(0))
                    currentPot.append(p2Deck.pop(0))
                p1Card2 = p1Deck.pop(0) #Draws the remanining 2 cards to be compared for who wins!
                p2Card2 = p2Deck.pop(0)
                currentPot.extend((p1Card2, p2Card2))
                winner, currentPot = compareFun(p1Card2, p2Card2, currentPot, p1Deck, p2Deck) # Runs the compare function recusively
            else:
                if len(p1Deck) > len(p2Deck): #If they do not have 5 cards, this determines who has less cards in their deck
                    shorterListLen = len(p2Deck)
                else:
                    shorterListLen = len(p1Deck)
                if shorterListLen == 0: #If there is a tie and one player has no cards remaning, the other player wins
                    if len(p1Deck) > len(p2Deck):
                        winner = "p1"
                    else:
                        winner = "p2"
                elif shorterListLen == 1: #If there is a tie and the losing player only has one card, this grabs one card from each deck and compares recusrively
                    p1Card2 = p1Deck.pop(0)
                    p2Card2 = p2Deck.pop(0)
                    currentPot.extend((p1Card2, p2Card2))
                    winner, currentPot = compareFun(p1Card2, p2Card2, currentPot, p1Deck, p2Deck)
                else:
                    for i in range(0, shorterListLen-1): #If the player has between 2 and 4 cards, this detemines that number and draws however many cards are remaning
                        currentPot.append(p1Deck.pop(0)) #minus one
                        currentPot.append(p2Deck.pop(0))
                    p1Card2 = p1Deck.pop(0) # This draws the final card for the compare function
                    p2Card2 = p2Deck.pop(0)
                    currentPot.extend((p1Card2, p2Card2))
                    winner, currentPot = compareFun(p1Card2, p2Card2, currentPot, p1Deck, p2Deck) #This runs the compare function recursively
    return winner, currentPot
            

#This is the function that plays the game. It takes the two split decks for each player, and plays the game!

def playGame(p1, p2):
    count = 0 #This counter tracks the number of rounds
    p1len = len(p1)  #Establishes the deck length variables
    p2len = len(p2)
    while p1len != 0 or p2len != 0: # established the endgame rules for War, where one player needs the whole deck to win
        if count >= 10000: #If the game goes for over 10000 rounds, it results in a draw
            print("This game has ended in a draw!!!")
            return
        if len(p2) == 0: #If Player 2 has no cards remaning, player 1 has won the game
            print("Player 1 has won the game!")
            return
        elif len(p1) == 0: #If Player 1 has no cards remaining, player 2 has won the game
            print("Player 2 has won the game!")
            return
        count += 1 #Increments the round number
        currentPot = [] # Sets up an empty list at the beginning of each round for the cards that will be used in that round
        p1Card = p1.pop(0) #These two variables grab the "top" cards from each deck
        p2Card = p2.pop(0)
        currentPot.extend((p1Card, p2Card)) #Puts the drawn cards into the pot
        winner, currentPot = compareFun(p1Card, p2Card, currentPot, p1, p2) #Calls the compare function on the drawn cards
        currentPot = shuffle(currentPot) #Shuffles the winnings before added back to the hand
        if winner == "p1": #decides the winner and gives the pot to who won
            for i in range(0, len(currentPot)):
                p1.append(currentPot[i])
            print("Player 1 has won round " + str(count) +"!")
        else:
            for i in range(0, len(currentPot)):
                p2.append(currentPot[i])
            print("Player 2 has won round " + str(count) +"!")
        p1len = len(p1) #reasses the number of cards in each deck for the determination at the beginning of the while loop
        p2len = len(p2)


shuffledDeck = shuffle(officialDeck) #shuffles the original deck
p1Deck, p2Deck = splitDeck(shuffledDeck)
playGame(p1Deck, p2Deck)
