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

def splitDeck(shuffledDeck): #This splits the shuffled deck in 2 and returns 2 decks for 2 players
    half = len(shuffledDeck)//2
    return shuffledDeck[:half], shuffledDeck[half:]

shuffledDeck = shuffle(officialDeck) #shuffles the original deck
p1Deck, p2Deck = splitDeck(shuffledDeck)

def playGame(p1, p2):
    while (len(p1) != 52) or (len(p2) != 52): # established the endgame rules for War, where one player needs the whole deck to win
        currentPot = [] # Sets up an empty list at the beginning of each round for the cards that will be used in that round
        # Below, we first establish the two values to be tuples that are stand ins before the round begins. These will be replaced in the
        # following while loop
        p1Card = ("No Card", 0) 
        p2Card = ("No Card", 0)
        while p1Card[1] == p2Card[1]: #this while loop makes sure that the cards do not have the same value. If they do, the next cards will be drawn
            p1Card = p1.pop(0)
            p2Card = p2.pop(0)
            currentPot.extend((p1Card, p2Card))
            if p1Card[1] > p2Card[1]: #if player one has the bigger card, he gets the pot
                for i in range(0, len(currentPot)):
                    p1.append(currentPot[i])
                    print("Player one wins the round!")
            elif p1Card[1] < p2Card[1]: #if player two has the bigger card, he gets the pot
                for i in range(0, len(currentPot)):
                    p2.append(currentPot[i])
                    print("Player two wins the round!")

    if len(p1) == 52:
        print("Player 1 has won!")
    else:
        print("Player 2 has won!")

playGame(p1Deck, p2Deck)